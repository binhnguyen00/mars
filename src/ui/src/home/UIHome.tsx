import React from "react";
import { UIWelcome } from "@/home/UIWelcome";
const UIImageConverter = React.lazy(() => import("@/container/UIImageConverter"));
const UIArchiveConverter = React.lazy(() => import("@/container/UIArchiveConverter"));

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
          <h1 
            className="clickable" style={{ color: "orangered" }}
            onClick={() => setContainer(<UIWelcome/>)}
          > 
            Mars Converter 
          </h1>
          <div className="flex-h">
            <div className="clickable" onClick={() => setContainer(<UIImageConverter/>)}>Image</div>
            <div className="clickable" onClick={() => setContainer(<UIArchiveConverter/>)}>Archive</div>
          </div>
        </div>
        <hr style={{ margin: 0 }}/>
      </header>
      <br />

      <React.Suspense>
        {renderContainer()}
      </React.Suspense>

      <footer>
        <hr />
        <p>In Development</p>
      </footer>
    </React.Fragment>
  )
}