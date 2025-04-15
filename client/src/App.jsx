import './App.css'
import Button from './components/Button/Button.jsx'
import WaitingRoom from './pages/waitingRoom.jsx';
import { useState } from "react";

function App() {
  const [page, setPage] = useState("waitingRoom"); // 현재 페이지 상태
  const play = () => {
    setPage("play");
  };
  
  return (
    <div className="">
      {page === "waitingRoom" && <WaitingRoom content={"다빈치코드"} />}
      {page === "play" && <></>}
    </div>
  );
}

export default App
