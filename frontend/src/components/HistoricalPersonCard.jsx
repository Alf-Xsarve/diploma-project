import { useState } from "react";
import { useNavigate } from "react-router-dom"; // 🔥 добавили
import {
  Card,
  CardMedia,
  CardContent,
  Typography,
  CardActions,
  IconButton,
  Button,
  Box,
} from "@mui/material";
import FavoriteIcon from "@mui/icons-material/Favorite";


function HistoricalPersonCard({ person }) {
  const [liked, setLiked] = useState(false);
  const navigate = useNavigate(); // 🔥 навигация

  return (
    <Card
      sx={{
        width: 240,
        height: 420,
        display: "flex",
        flexDirection: "column",
        borderRadius: 4,
        overflow: "hidden",
        boxShadow: 3,
        transition: "0.3s",
        "&:hover": {
          transform: "translateY(-6px)",
          boxShadow: 8,
        },
      }}
    >
      {/* 📸 Картинка */}
      <Box sx={{ position: "relative" }}>
        <CardMedia
          component="img"
          height="200"
          image={person?.photo || "https://via.placeholder.com/300"}
          alt={person.full_name}
          sx={{ objectFit: "cover" }}
        />

        {/* 🟣 overlay */}
        <Box
          sx={{
            position: "absolute",
            bottom: 0,
            width: "100%",
            background:
              "linear-gradient(to top, rgba(0,0,0,0.7), transparent)",
            color: "white",
            fontSize: "12px",
            p: 1,
          }}
        >
          {person.profession}
        </Box>
      </Box>

      {/* 📄 Контент */}
      <CardContent sx={{ flexGrow: 1 }}>
        <Typography variant="subtitle1" sx={{ fontWeight: 600 }} noWrap>
          {person.full_name}
        </Typography>

        <Typography variant="body2" color="text.secondary">
          {person.birth_year} – {person.death_year || "..."}
        </Typography>

        <Typography
          variant="body2"
          sx={{
            mt: 1,
            color: "text.secondary",
            display: "-webkit-box",
            WebkitLineClamp: 2,
            WebkitBoxOrient: "vertical",
            overflow: "hidden",
            fontSize: "13px",
          }}
        >
          {person.description}
        </Typography>
      </CardContent>

      {/* 🔘 Кнопки */}
      <CardActions
        sx={{
          display: "flex",
          justifyContent: "space-between",
          px: 2,
          pb: 2,
        }}
      >
        {/* 🔥 ЧИТАТЬ */}
        <Button
          variant="contained"
          size="small"
          fullWidth
          onClick={() => navigate(`/person/${person.id}`)} // 🚀 переход
          sx={{
            mr: 1,
            borderRadius: "10px",
            textTransform: "none",
            fontWeight: 600,
            fontSize: "13px",
            py: 0.7,
            background: "linear-gradient(90deg, #3f51b5, #7c4dff)",
            boxShadow: "0 3px 10px rgba(124,77,255,0.3)",
            "&:hover": {
              background: "linear-gradient(90deg, #303f9f, #651fff)",
            },
          }}
        >
          Читать
        </Button>

        {/* ❤️ Лайк */}
        <IconButton
          onClick={() => setLiked(!liked)}
          sx={{
            border: "1px solid #eee",
            borderRadius: "10px",
            p: 0.8,
          }}
        >
          <FavoriteIcon
            sx={{
              fontSize: 18,
              color: liked ? "#e53935" : "#bbb",
            }}
          />
        </IconButton>
      </CardActions>
    </Card>
  );
}

export default HistoricalPersonCard;