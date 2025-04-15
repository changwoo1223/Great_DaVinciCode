const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const app = express();
const server = http.createServer(app);
const io = new Server(server, {
    cors: {
    origin: "*", // Vite 주소
    methods: ["GET", "POST"]
    }
});
/*
let players = [];
io.on("connection", (socket) => {
    console.log("A player connected:", socket.id);

if (players.length < 4) {
    players.push(socket.id);
    io.emit("updatePlayers", players);
} else {
    socket.emit("roomFull");
    socket.disconnect();
}

socket.on("disconnect", () => {
    players = players.filter(id => id !== socket.id);
    io.emit("updatePlayers", players);
    });

  // 게임 내 커스텀 이벤트들 처리
socket.on("move", (data) => {
    socket.broadcast.emit("move", data); // 다른 플레이어에게 전달
    });
});
*/
server.listen(3000, () => {
    console.log("서버 실행 중: http://localhost:3000");
});