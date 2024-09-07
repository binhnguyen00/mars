import React from "react";

const UIImageConverter = React.lazy(() => import("@/image/UIImageConverter"));
// more UI lazy load

export function UIHome() {
  const [ container, setContainer ] = React.useState<React.ReactElement>(<UIImageConverter/>);

  const renderContainer = React.useCallback(() => {
    return container;
  }, [container]);

  return(
    <React.Fragment>
      <header>
        <hgroup style={{ margin: 0 }}>
          <h1> Image Converter </h1>
          <p>Easily convert your images to different file formats.</p>
        </hgroup>
        <hr />
      </header>

      {renderContainer()}

      <footer>
        <hr />
        <p>In Development</p>
      </footer>
    </React.Fragment>
  )
}