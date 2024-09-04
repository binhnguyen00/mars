import React from "react";

export function UIHome() {

  const getFileExtension = (fileName: string) => {
    const extension = fileName.split('.').pop();
    return extension ? `.${extension}` : '';
  }

  const upload = async (event: React.MouseEvent) => {
    event.preventDefault();
    const formData = new FormData();
    const imageFile = (document.getElementById('image') as HTMLInputElement).files[0];
    formData.append('image', imageFile);

    try {
      const response = await fetch('/upload-image', {
        method: 'POST',
        body: formData
      });
      if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);

        const resultImage = document.getElementById('resultImage') as HTMLImageElement;
        resultImage.src = url;
        resultImage.style.display = 'block';

        const downloadLink = document.getElementById('downloadLink') as HTMLAnchorElement;
        downloadLink.style.display = 'block';
        downloadLink.href = url;
        downloadLink.download = imageFile.name.replace(/\.[^/.]+$/, "") + "_processed" + getFileExtension(imageFile.name);
      } else {
        const error = await response.json();
        alert('Error: ' + error.error);
      }
    } catch (err) {
      console.error('Error:', err);
    }
  }

  return (
    <div>
      <h1> Upload Image </h1>

      <div>
        <input type="file" id="image" name="image" accept="image/*" required></input>
        <button onClick={upload}> Upload </button>
      </div>

      <br/>

      <div style={{ width: "300px", height: "300px" }}>
        <img id="resultImage" src="" style={{ display: "none" }}/>
        <a id="downloadLink" href="#" download style={{ display: "none" }}>Download</a>
      </div>
    </div>
  )
}