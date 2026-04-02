import { BrowserRouter, Routes, Route } from "react-router-dom";
import Persons from "./pages/Persons";
import Login from "./pages/Login";
import Register from "./pages/Register";
import PersonDetail from "./pages/PersonDetail"; // 🔥 добавили

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Persons />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* 🔥 новая страница */}
        <Route path="/person/:id" element={<PersonDetail />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;