source ./common/utils.sh

# Ensure database env
if [ ! -f "$CURRENT_DIR/common/database-env.sh" ]; then 
  cp ./common/database-env.sh.sample ./common/database-env.sh
fi

source ./common/database-env.sh

function init_user() {
  PGPASSWORD=$ADMIN_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $ADMIN_USER -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD'"
}

function init_db() {
  PGPASSWORD=$ADMIN_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $ADMIN_USER -c "DROP DATABASE IF EXISTS $DB_NAME"
  PGPASSWORD=$ADMIN_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $ADMIN_USER -c "CREATE DATABASE $DB_NAME"
  PGPASSWORD=$ADMIN_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $ADMIN_USER -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER"
  PGPASSWORD=$ADMIN_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $ADMIN_USER -c "ALTER DATABASE $DB_NAME OWNER TO $DB_USER"
  PGPASSWORD=$ADMIN_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $ADMIN_USER -c "ALTER SCHEMA public OWNER TO $DB_USER"
}

function initial() {
  init_user
  init_db
}

function dump() {
  mkdir -p "$DUMP_DIR"
  PGPASSWORD=$DB_PASSWORD pg_dump -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -F t "$DB_NAME" > "$DUMP_FILE"
}

function restore() {
  init_db

  # Find the backup file
  FILE_FOUND=false
  if [ -v "$@" ] ; then
    echo "No backup file provided."
    exit 1
  else 
    cd "$DUMP_DIR"
    for FILE in *.tar; do
      if [ "$FILE" = "$@" ]; then
        FILE_FOUND=true
        break
      fi
    done
  fi

  if [ "$FILE_FOUND" = false ] ; then
    echo "Backup file not found."
    exit 1
  else 
    PGPASSWORD=$DB_PASSWORD pg_restore -U "$DB_USER" -d "$DB_NAME" -h "$DB_HOST" -p "$DB_PORT" "$FILE"
    echo $FILE
  fi
}

function check_psql() {
  if ! command -v psql > /dev/null 2>&1; then
    echo """
IMPORTANT:
psql is not available. Please install PostgreSQL in order to use this script.
https://www.postgresql.org/download/
    """
    exit 1
  fi
}

function show_help() {
  echo """
Usage: Manipulating database 
  ./database.sh [COMMAND] [OPTION]

NOTE: You should change the value in /scripts/common/database-env.sh

REQUIREMENTS: 
  - Postgres

Dump
  ./database.sh dump

Restore
  ./database.sh restore [FILE]

Initial Database
  ./database.sh initial-db

Initial Admin User
  ./database.sh initial-user
  
Initial Admin User & Database
  ./database.sh initial
  """
}

check_psql
COMMAND=$1;
if [ -n "$COMMAND" ]; then
  shift
else
  echo "No command provided. Showing help..."
  show_help
  exit 1
fi

if [ "$COMMAND" = "dump" ] ; then
  dump
elif [ "$COMMAND" = "restore" ] ; then
  restore $@
elif [ "$COMMAND" = "initial-db" ] ; then
  init_db
elif [ "$COMMAND" = "initial-user" ] ; then
  init_user
elif [ "$COMMAND" = "initial" ] ; then
  initial
elif [ "$COMMAND" = "help" ] ; then
  show_help
else
  ./database.sh help 
fi