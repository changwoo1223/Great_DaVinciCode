const express = require('express');
const app = express();
const PORT = 3000; 
const cors = require('cors');
app.use(cors());





// 서버 실행
app.listen(PORT, () => {
    console.log(`서버가 실행 중 👉 http://localhost:${PORT}`);
});