const form = document.getElementById("uploadForm");
const fileInput = document.getElementById("fileInput");
const dropArea = document.getElementById("drop-area");
const progress = document.getElementById("progress");
const bar = document.getElementById("bar");
const status = document.getElementById("status");

// Drag & drop
dropArea.addEventListener("click", () => fileInput.click());

dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.style.background = "#d3f8ec";
});

dropArea.addEventListener("dragleave", () => {
  dropArea.style.background = "#ecfdf5";
});

dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea.style.background = "#ecfdf5";
  fileInput.files = e.dataTransfer.files;
});

// Upload
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const file = fileInput.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);

  progress.style.display = "block";
  bar.style.width = "0%";
  status.textContent = "Uploading...";

  try {
    const res = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    const reader = res.body.getReader();
    let received = 0;
    const contentLength = +res.headers.get("Content-Length") || 1;

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      received += value.length;
      bar.style.width = `${(received / contentLength) * 100}%`;
    }

    const data = await res.json();
    status.textContent = data.message;
    bar.style.width = "100%";
  } catch (err) {
    status.textContent = "Upload failed.";
  }
});
