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

    try {
      const response = await restful.POST('/upload-image', formData);
      if (!response.ok) {
        throw new Error(response.statusText);
      }

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      setResultImageUrl(url);

      const processedFileName = imageFile.name.replace(/\.[^/.]+$/, "") + "_processed" + getFileExtension(imageFile.name);
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
    <div>
      <h1> Upload Image </h1>

      <div>
        <input type="file" id="image" name="image" accept="image/*" required />
        <button onClick={upload} disabled={loading}>
          {loading ? "Uploading..." : "Upload"}
        </button>
      </div>

      <br />

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {resultImageUrl && (
        <div className="flex-v" style={{ width: "300px", height: "300px" }}>
          <img id="resultImage" src={resultImageUrl} alt="Processed" />
          <button onClick={downloadFile}>Download</button>
        </div>
      )}
    </div>
  );
}
