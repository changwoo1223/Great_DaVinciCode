import './App.css'
import Lobby from './pages/Lobby.jsx';
import Play from './pages/Play.jsx';
import { useState } from "react";

function App() {
  const [page, setPage] = useState("lobby"); // 현재 페이지 상태

  return (
    <div>
      {page === "lobby" && <Lobby content={"다빈치코드"} setPage={setPage} />}
      {page === "play" && <Play />}
    </div>
  );
}

export default App;

