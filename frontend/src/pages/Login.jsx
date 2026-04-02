import { useState } from "react";
import {
  TextField,
  Button,
  Box,
  Typography,
  Paper,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import { login } from "../api/auth";

function Login() {
  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async () => {
    try {
      const res = await login(form);

      // 🔐 сохраняем токены
      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);

      // 👤 сохраняем пользователя
      localStorage.setItem("user", JSON.stringify(res.data.user));

      navigate("/");
    } catch (err) {
      console.log(err.response?.data);

      if (err.response?.data?.detail) {
        alert("Неверный логин или пароль");
      } else {
        alert("Ошибка входа");
      }
    }
  };

  return (
    <Box
      sx={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#f5f7fb",
      }}
    >
      <Paper sx={{ p: 4, width: 400, borderRadius: 3 }}>
        
        {/* ⬅️ Назад */}
        <Button onClick={() => navigate("/")}>
          ← На главную
        </Button>

        <Typography variant="h5" mb={3} textAlign="center">
          Вход
        </Typography>

        <TextField
          fullWidth
          label="Username"
          name="username"
          margin="normal"
          onChange={handleChange}
          autoComplete="username"
        />

        <TextField
          fullWidth
          type="password"
          label="Password"
          name="password"
          margin="normal"
          onChange={handleChange}
          autoComplete="current-password"
        />

        {/* 🔘 Кнопка */}
        <Button
          fullWidth
          variant="contained"
          sx={{ mt: 2, py: 1.2 }}
          onClick={handleSubmit}
        >
          Войти
        </Button>

        {/* 🔗 Ссылка */}
        <Typography
          align="center"
          sx={{ mt: 2, cursor: "pointer", color: "#3f51b5" }}
          onClick={() => navigate("/register")}
        >
          Нет аккаунта? Зарегистрироваться
        </Typography>
      </Paper>
    </Box>
  );
}

export default Login;