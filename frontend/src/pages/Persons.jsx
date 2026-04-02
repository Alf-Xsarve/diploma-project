import { useEffect, useState } from "react";
import API from "../api/auth";
import {
  Grid,
  Container,
  Typography,
  TextField,
  Box,
  Button,
  Paper,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import HistoricalPersonCard from "../components/HistoricalPersonCard";

function Persons() {
  const [persons, setPersons] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  // 🔐 авторизация
  const isAuth = !!localStorage.getItem("access");

  // ✅ БЕЗОПАСНОЕ получение user
  let user = null;
  try {
    const userData = localStorage.getItem("user");
    if (userData && userData !== "undefined") {
      user = JSON.parse(userData);
    }
  } catch (e) {
    console.error("Ошибка парсинга user:", e);
  }

  useEffect(() => {
    API.get("persons/")
      .then((res) => {
        const data = res.data;

        if (Array.isArray(data)) {
          setPersons(data);
        } else if (data?.results) {
          setPersons(data.results);
        } else {
          setPersons([data]);
        }
      })
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  // 🔍 поиск
  const filteredPersons = persons.filter((person) =>
    person.full_name.toLowerCase().includes(search.toLowerCase())
  );

  // 🚪 logout
  const handleLogout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    localStorage.removeItem("user");
    window.location.reload();
  };

  return (
    <Container maxWidth={false} sx={{ mt: 2, px: 4 }}>
      
      {/* 🔝 ШАПКА */}
      <Paper
        sx={{
          p: 2,
          mb: 3,
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          borderRadius: 3,
        }}
      >
        <Typography sx={{ fontWeight: 600 }}>
          🇰🇬 История Кыргызстана
        </Typography>

        {isAuth ? (
          <Box sx={{ display: "flex", alignItems: "center", gap: 2 }}>
            <Typography sx={{ fontWeight: 500 }}>
              👋 {user?.first_name || user?.username || "Пользователь"}
            </Typography>

            <Button variant="outlined" onClick={handleLogout}>
              Выйти
            </Button>
          </Box>
        ) : (
          <Box>
            <Button sx={{ mr: 1 }} onClick={() => navigate("/login")}>
              Вход
            </Button>
            <Button
              variant="contained"
              onClick={() => navigate("/register")}
            >
              Регистрация
            </Button>
          </Box>
        )}
      </Paper>

      {/* 🔥 Заголовок */}
      <Typography
        align="center"
        sx={{
          fontWeight: 700,
          mb: 2,
          fontSize: { xs: "24px", md: "34px" },
          background: "linear-gradient(90deg, #3f51b5, #7c4dff)",
          WebkitBackgroundClip: "text",
          WebkitTextFillColor: "transparent",
        }}
      >
        История Кыргызстана в лицах
      </Typography>

      {/* 🔍 Поиск */}
      <Box sx={{ display: "flex", justifyContent: "center", mb: 4 }}>
        <TextField
          label="Поиск по имени"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          sx={{ width: "100%", maxWidth: 400 }}
        />
      </Box>

      {/* 📦 Карточки */}
      {loading ? (
        <Typography align="center">Загрузка...</Typography>
      ) : filteredPersons.length === 0 ? (
        <Typography align="center">Ничего не найдено</Typography>
      ) : (
        <Grid container spacing={3} justifyContent="center">
          {filteredPersons.map((person) => (
            <Grid item xs={12} sm={6} md={4} key={person.id}>
              <HistoricalPersonCard person={person} />
            </Grid>
          ))}
        </Grid>
      )}
    </Container>
  );
}

export default Persons;