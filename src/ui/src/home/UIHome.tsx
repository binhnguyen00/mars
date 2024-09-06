import React from "react";
import { restful } from "@/server/RESTful";

export function UIHome() {
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);
  const [resultImageUrl, setResultImageUrl] = React.useState<string | null>(null);
  const [downloadFileName, setDownloadFileName] = React.useState<string | null>(null);

  const getFileExtension = (fileName: string) => {
    const extension = fileName.split('.').pop();
    return extension ? `.${extension}` : '';
  };

  const upload = async (event: React.MouseEvent) => {
    event.preventDefault();
    setLoading(true);
    setError(null); // Reset any previous errors
    setResultImageUrl(null); // Reset the result image

    const imageFile = (document.getElementById('image') as HTMLInputElement).files?.[0];
    if (!imageFile) {
      setError("Please select an image file.");
      setLoading(false);
      return;
    }

    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('format', "JPEG");

    try {
      const response = await restful.POST('/upload-image', formData);
      if (!response.ok) {
        throw new Error(response.statusText);
      }

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      setResultImageUrl(url);

      const processedFileName = imageFile.name.replace(/\.[^/.]+$/, "") + "_processed";
      setDownloadFileName(processedFileName);
    } catch (err: any) {
      setError(`Upload failed: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const downloadFile = () => {
    if (resultImageUrl && downloadFileName) {
      const a = document.createElement('a');
      a.href = resultImageUrl;
      a.download = downloadFileName;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }
  };

  return (
    <React.Fragment>
      
      <header>
        <hgroup style={{ margin: 0 }}>
          <h1> Image Converter </h1>
          <p>Easily convert your images to different file formats.</p>
        </hgroup>
      </header>

      <hr />
      
      <main style={{ flexGrow: 1 }}>
        <div>
          <label htmlFor="image"> Select an image file </label>
          <input type="file" id="image" name="image" accept="image/*" required/>
        </div>
        <div className="grid">
          <div>
            <label htmlFor="input-formart"> Input file format </label>
            <input name="input-formart" value={""} disabled/>
          </div>
          <div>
            <label htmlFor="select-format"> New file format </label>
            <select name="select-format" aria-label="Select new file format" required>
              <option selected disabled value=""> Select new format </option>
              <option>PNG</option>
              <option>JPG</option>
              <option>JPEG</option>
            </select>
          </div>
        </div>
        <button onClick={upload} disabled={loading} className="outline">
          {loading ? "Uploading..." : "Upload"}
        </button>

        {error && <p style={{ color: 'red' }}>{error}</p>}

        <div className="flex-v">
          <label htmlFor="resultImage"> Converted Image </label>
          {resultImageUrl ? (
            <img 
              id="resultImage" alt="Processed" src={resultImageUrl} 
              width={"100%"} height={"auto"}
            />
          ) : (
            <img 
              id="resultImage" alt="Processed" src={"../../assets/imgs/placeholder.svg"} 
              width={"100%"} height={"auto"}
            />
          )}
          {resultImageUrl && (
            <button onClick={downloadFile}>Download</button>
          )}
        </div>
      </main>

      <hr />

      <footer>
        <p>In Development</p>
      </footer>

    </React.Fragment>
  );
}
