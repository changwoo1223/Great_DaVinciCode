const express = require("express");
const http = require("http");
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server);
// 루트 경로
const path = require('path');
const distPath = path.join(__dirname, '../../client/dist');
app.use(express.static(distPath));

app.use(express.json()); // JSON 파싱 미들웨어

// 루트 경로로 접속 시 index.html 보내기
app.get('*', (req, res) => {
    res.sendFile(path.join(distPath, 'index.html'));
    });

let socketOn = false; // Socket.IO 상태
let player = 0;
// 서킷 서버 활성화
app.get('/join',(req,res) => { // join 경로
    if(!socketOn){
        socketOn = true;
        console.log('socket 서버가 열렸어요.');
    }else {}
});
// 플레이어 관리
io.on('connection',(socket) => {
    if (!socketOn){
        socket.disconnect();
    }
    if (player >= 4){
        socket.emit('정원초과에요.');
        socket.disconnect();
    }
    player++;
    console.log(`플레이어 ${player}명 참가.`);
    
    socket.on('disconnect',() => {
        player--;
        console.log(`플레이어 연결이 끊켯어요 현재:${player}명`);
    });
});


const PORT = 3000; 
server.listen(PORT, () => {
    console.log(`서버 실행 중 => http://localhost:${PORT}`);
});