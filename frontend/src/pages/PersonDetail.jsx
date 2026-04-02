import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import API from "../api/auth";
import {
  Box,
  Typography,
  Grid,
  Paper,
  Button,
} from "@mui/material";

function PersonDetail() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [person, setPerson] = useState(null);

  useEffect(() => {
    API.get(`persons/${id}/`)
      .then((res) => setPerson(res.data))
      .catch((err) => console.error(err));
  }, [id]);

  if (!person) return <Typography align="center">Загрузка...</Typography>;

  return (
    <Box sx={{ maxWidth: 1200, mx: "auto", p: 3 }}>

      {/* 🔙 Назад */}
      <Button onClick={() => navigate("/")} sx={{ mb: 2 }}>
        ← Назад
      </Button>

      <Paper sx={{ p: 3, borderRadius: 3 }}>

        {/* 🔥 Заголовок */}
        <Typography variant="h4" sx={{ mb: 2 }}>
          {person.full_name}
        </Typography>

        <Typography variant="subtitle1" sx={{ mb: 3, color: "gray" }}>
          {person.birth_year} — {person.death_year || "..."} | {person.profession}
        </Typography>

        <Grid container spacing={3}>

          {/* 📝 ТЕКСТ */}
          <Grid size={{ xs: 12, md: 8 }}>
            <Typography
              sx={{
                lineHeight: 1.7,
                whiteSpace: "pre-line",
                fontSize: "16px",
              }}
            >
              {person.description_full || person.description}
            </Typography>
          </Grid>

          {/* 🖼 ФОТО */}
          <Grid size={{ xs: 12, md: 4 }}>
            {person.photo && (
              <Box
                component="img"
                src={person.photo}
                alt={person.full_name}
                sx={{
                  width: "100%",
                  borderRadius: 3,
                  boxShadow: 3,
                }}
              />
            )}
          </Grid>

        </Grid>

        {/* 📄 ДОКУМЕНТЫ */}
        {(person.pdf_file || person.doc_file) && (
          <Box sx={{ mt: 4 }}>
            <Typography variant="h6" mb={1}>
              Дополнительные материалы
            </Typography>

            {person.pdf_file && (
              <Button
                variant="outlined"
                href={person.pdf_file}
                target="_blank"
                sx={{ mr: 2 }}
              >
                Открыть PDF
              </Button>
            )}

            {person.doc_file && (
              <Button
                variant="outlined"
                href={person.doc_file}
                target="_blank"
              >
                Скачать Word
              </Button>
            )}
          </Box>
        )}

      </Paper>
    </Box>
  );
}

export default PersonDetail;