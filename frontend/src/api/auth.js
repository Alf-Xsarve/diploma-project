import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  headers: {
    "Content-Type": "application/json", // 👈 ВАЖНО
  },
});

// 🔐 автоматически подставляем токен
API.interceptors.request.use((req) => {
  const token = localStorage.getItem("access");

  if (token) {
    req.headers.Authorization = `Bearer ${token}`;
  }

  return req;
});

// 🔑 ЛОГИН
export const login = (data) =>
  API.post("token/", data);

// 📝 РЕГИСТРАЦИЯ
export const register = (data) =>
  API.post("register/", data);

export default API;