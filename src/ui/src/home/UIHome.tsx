import React from "react";
import { UIImageConverter } from "@/container/UIImageConverter";
import { UIArchiveConverter } from "@/container/UIArchiveConverter";

export function UIHome() {
  const startPage = <UIImageConverter/>;
  const [ container, setContainer ] = React.useState(startPage);

  const renderContainer = React.useCallback(() => {
    return (container);
  }, [container]);

  return(
    <React.Fragment>
      <header>
        <div className="flex-h">
          <h1 className="clickable"> Media Converter </h1>
          <div className="flex-h">
            <div className="clickable" onClick={() => setContainer(<UIImageConverter/>)}>Image</div>
            <div className="clickable" onClick={() => setContainer(<UIArchiveConverter/>)}>Archive</div>
          </div>
        </div>
        <hr style={{ margin: 0 }}/>
      </header>
      <br />

      {renderContainer()}

      <footer>
        <hr />
        <p>In Development</p>
      </footer>
    </React.Fragment>
  )
}