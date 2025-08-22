import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000", // FastAPI backend
});

export const analyzeData = async (text, imageFile) => {
  let imageBase64 = null;

  if (imageFile) {
    const reader = new FileReader();
    imageBase64 = await new Promise((resolve) => {
      reader.onloadend = () => resolve(reader.result.split(",")[1]);
      reader.readAsDataURL(imageFile);
    });
  }

  const payload = { text, image_base64: imageBase64 };
  const response = await API.post("/analyze", payload);
  return response.data;
};

export const getHistory = async () => {
  const response = await API.get("/history?limit=10");
  return response.data;
};
