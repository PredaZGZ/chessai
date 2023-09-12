import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

//Pages
import Chess from "./Pages/Chess.jsx";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Chess />} />
      </Routes>
    </Router>
  );
}
