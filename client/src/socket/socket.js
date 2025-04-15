const socket = io('http://localhost:3000');

socket.on('connect', () => {
    console.log('서버에 연결됨!');
    socket.emit('message', '안녕 서버냥!');
});

socket.on('message', (msg) => {
    console.log('서버 응답:', msg);
});