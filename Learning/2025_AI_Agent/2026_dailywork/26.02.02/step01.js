const http = require('http');
const express = require('express');
const app = express();
const cors = require('cors');

// 크로스오리진 처리
app.use(cors());

// 사용자 정의 미들웨어 선언
app.use("/", function(req, res, next) {
    console.log("첫번째 사용자 정의 미들웨어 호출");
    res.writeHead(200, {"Content-Type":"text/html; charset=utf-8"})
    // 미들웨어 처리 후 다음 기능 호출 (중요)
    next();
});

// index.html페이지를 바로 접근 가능하게 한다.
// 정적(static) 폴더 - express
app.use("/public", express.static("./public"));

app.get("/", function(req, res) {
    res.end("GET - / 요청 완료")
});


const server = http.createServer(app);
server.listen(3000, function () {
    console.log(">>>>>>>>>>>>>> http://127.0.0.1:3000/car/list");
});
