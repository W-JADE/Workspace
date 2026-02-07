const http = require('http');
const express = require('express');
const app = express();
const cors = require('cors');
const path = require('path');

// 뷰엔진 설정
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// 크로스오리진 처리
app.use(cors());

app.use("/public", express.static("./public"));

app.get("/", function(req, res) {
    res.end("GET - / 요청 완료")
});

// 임시 데이터 리스트
// 데이터 베이스에서 가져온 데이터로 대체될 임시 목록
const carList = [
    {_id:1001, name:"GRANDEUR", price:3500, company:"HYUNDAI", year:2019},
    {_id:1002, name:"SONATA2", price:2500, company:"HYUNDAI", year:2022},
    {_id:1003, name:"BMW", price:5500, company:"BMW", year:2018},
    {_id:1004, name:"S80", price:4500, company:"VOLVO", year:2023}
];

// car list 처리
app.get('/car/list', (req, res)=>{
    // nodejs 콜백함수의 첫번째 인자는 error 객체
    // 또는 res.render()로 사용
    // req.app.render('car/list', {}, (err, html)=>{
	// 	if(err) throw err;
    //     res.end(html);
    // });

    // 또는 좀더 단순하게 사용
    res.render('car/list', {carList});
})

const server = http.createServer(app);
server.listen(3000, function () {
    console.log(">>>>>>>>>>>>>> http://127.0.0.1:3000/car/list");
});
