const express = require('express');
const app = express();

const cors = require('cors');
app.use(cors());

const path = require('path');
const distPath = path.join(__dirname, '../../client/dist');

// 서버 실행
const PORT = 3000; 
app.listen(PORT, () => {
    console.log(`서버가 실행 중 👉 http://localhost:${PORT}`);
});
// 정적 파일 경로 설정 (React 빌드된 결과 제공)
app.use(express.static(distPath));
// 루트 경로로 접속 시 index.html 보내기
app.get('*', (req, res) => {
    res.sendFile(path.join(distPath, 'index.html'));
    });

