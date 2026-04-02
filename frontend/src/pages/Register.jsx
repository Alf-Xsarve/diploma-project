import { useState } from "react";
import {
  TextField,
  Button,
  Box,
  Typography,
  Paper,
  Divider,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import { register } from "../api/auth";

function Register() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    birth_date: "",
    password: "",
    password_confirm: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    try {
      const res = await register(form);

      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      localStorage.setItem("user", JSON.stringify(res.data.user));

      navigate("/");
    } catch (err) {
      console.log(err.response?.data);
      alert("Ошибка регистрации");
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
        px: 2,
      }}
    >
      <Paper sx={{ p: 4, width: 450, borderRadius: 4 }}>
        
        {/* ⬅️ Назад */}
        <Button onClick={() => navigate("/")}>
          ← На главную
        </Button>

        <Typography variant="h5" mb={3} textAlign="center">
          Создание аккаунта
        </Typography>

        {/* 👤 ЛИЧНЫЕ ДАННЫЕ */}
        <Typography sx={{ fontWeight: 600, mb: 2 }}>
          Личная информация
        </Typography>

        <Box sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
          
          <TextField
            fullWidth
            label="Имя пользователя"
            name="username"
            onChange={handleChange}
            autoComplete="username"
          />

          <TextField
            fullWidth
            label="Имя"
            name="first_name"
            onChange={handleChange}
            autoComplete="given-name"
          />

          <TextField
            fullWidth
            label="Фамилия"
            name="last_name"
            onChange={handleChange}
            autoComplete="family-name"
          />

          <TextField
            fullWidth
            label="Email"
            name="email"
            onChange={handleChange}
            autoComplete="email"
          />

          <TextField
            fullWidth
            type="date"
            name="birth_date"
            onChange={handleChange}
            InputLabelProps={{ shrink: true }}
          />

        </Box>

        <Divider sx={{ my: 3 }} />

        {/* 🔐 ПАРОЛЬ */}
        <Typography sx={{ fontWeight: 600, mb: 2 }}>
          Безопасность
        </Typography>

        <Box sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
          
          <TextField
            fullWidth
            type="password"
            label="Пароль"
            name="password"
            onChange={handleChange}
            autoComplete="new-password"
          />

          <TextField
            fullWidth
            type="password"
            label="Повторите пароль"
            name="password_confirm"
            onChange={handleChange}
            autoComplete="new-password"
          />

        </Box>

        {/* 🔘 Кнопка */}
        <Button
          fullWidth
          variant="contained"
          sx={{ mt: 3, py: 1.2, borderRadius: 2 }}
          onClick={handleSubmit}
        >
          Зарегистрироваться
        </Button>

        {/* 🔗 Ссылка */}
        <Typography
          align="center"
          sx={{ mt: 2, cursor: "pointer", color: "#3f51b5" }}
          onClick={() => navigate("/login")}
        >
          Уже есть аккаунт? Войти
        </Typography>
      </Paper>
    </Box>
  );
}

export default Register;