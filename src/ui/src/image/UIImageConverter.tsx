import React from "react";
import { restful } from "@/server/RESTful";

function UIImageConverter() {
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);
  const [resultImageUrl, setResultImageUrl] = React.useState<string | null>(null);
  const [downloadFileName, setDownloadFileName] = React.useState<string | null>(null);
  const [orgImageExt, setOrgImageExt] = React.useState<string>("");
  const [targetImageExt, setTargetImageExt] = React.useState<string>("");

  const getFileExtension = (fileName: string) => {
    const extension = fileName.split('.').pop();
    return extension || "";
  };

  const getImageInputFile = () => {
    const fileInput = (document.getElementById('image') as HTMLInputElement).files?.[0];
    return fileInput || null;
  };

  const upload = async (event: React.MouseEvent) => {
    event.preventDefault();
    setLoading(true);
    setError(null); // Reset any previous errors
    setResultImageUrl(null); // Reset the result image

    const imageFile = getImageInputFile();
    if (!imageFile) {
      setError("Please select an image file.");
      setLoading(false);
      return;
    }

    const body = new FormData();
    body.append("image", imageFile);
    body.append("format", targetImageExt);
    try {
      const response = await restful.POST('/upload-image', body);
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
    <main style={{ flexGrow: 1 }}>
      <div>
        <label> Select an image file </label>
        <input type="file" id="image" accept="image/*" required onInput={() => {
          const imageFile = getImageInputFile();
          if (imageFile) {
            const extension = getFileExtension(imageFile.name);
            setOrgImageExt(extension);
          }
        }}/>
      </div>
      <div className="grid">
        <div>
          <label htmlFor="input-formart"> Input file format </label>
          <input name="input-formart" value={orgImageExt.toUpperCase()} disabled/>
        </div>
        <div>
          <label> New file format </label>
          <select required defaultValue={"Select new format"} onChange={(event) => {
            setTargetImageExt(event.target.value);
          }}>
            <option disabled> Select new format </option>
            <option value={"PNG"}>PNG</option>
            <option value={"JPG"}>JPG</option>
            <option value={"JPEG"}>JPEG</option>
          </select>
        </div>
      </div>
      <button onClick={upload} disabled={loading} className="outline">
        {loading ? "Uploading..." : "Upload"}
      </button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      <div className="flex-v">
        <h4 style={{ textAlign: 'center' }}> Your Converted Image </h4>
        {resultImageUrl ? (
          <img 
            id="resultImage" alt="Processed" src={resultImageUrl} 
            width={"100%"} height={"auto"}
          />
        ) : (
          <img 
            id="resultImage" alt="Processed" src={"../../assets/imgs/placeholder.svg"} 
            width={"auto"} height={"auto"}
          />
        )}
        {resultImageUrl && (
          <button onClick={downloadFile}>Download</button>
        )}
      </div>
    </main>
  );
}

export default UIImageConverter;