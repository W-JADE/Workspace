const http = require('http');
const express = require('express');
const app = express();
const cors = require('cors');
const path = require('path');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(cors());

app.use("/public", express.static("./public"));

app.get("/", function(req, res) {
    res.end("GET - / 요청 완료")
});

const carList = [
    {_id:1001, name:"GRANDEUR", price:3500, company:"HYUNDAI", year:2019},
    {_id:1002, name:"SONATA2", price:2500, company:"HYUNDAI", year:2022},
    {_id:1003, name:"BMW", price:5500, company:"BMW", year:2018},
    {_id:1004, name:"S80", price:4500, company:"VOLVO", year:2023}
];

var cnt = 1005;

// car list 처리
app.get('/car/list', function (req, res) {
    res.render('car/list', {carList});
});

// 상세 보기 
app.get('/car/detail', function(req, res) {
    var _id = Number(req.query._id);
    var idx = carList.findIndex(function(item, i) {
        console.log(item, i);
        return item._id == _id;
    });
    var car = null;
    console.log(idx);
    if(idx != -1) {
        car = carList[idx];
    }
    res.render('car/detail', {car});
});

// 삭제 기능
app.get('/car/delete', function(req, res) {
    var _id = Number(req.query._id);
    var idx = carList.findIndex(function(item, i) {
        console.log(item, i);
        return item._id == _id;
    });
    console.log(idx);
    if(idx != -1) {
        // idx의 내용 삭제 (splice() 함수로 삭제)
        carList.splice(idx, 1);
    }
    // 목록으로 새로고침
    res.redirect('/car/list');
});

// 정보 입력 뷰 페이지 보이기
app.get("/car/input", function(req, res) {
    res.render('car/input');
});

// 새 자동차 정보 입력
app.get("/car/input_ok", function(req, res) {
    //console.dir(req.query);
    var newCar = {
        _id:cnt++,
        name: req.query.name,
        company: req.query.company,
        price: req.query.price,
        year: req.query.year
    }
    carList.push(newCar);
    res.redirect('/car/list');
});


// 수정 기능
app.get('/car/modify', function(req, res) {
    var _id = Number(req.query._id);
    var idx = carList.findIndex(function(item, i) {
        console.log(item, i);
        return item._id == _id;
    });
    var car = null;
    console.log(idx);
    if(idx != -1) {
        car = carList[idx];
    }
    res.render('car/modify', {car});
});

app.get("/car/modify_ok", function(req, res) {
    var car = {
        _id:req.query._id,
        name: req.query.name,
        company: req.query.company,
        price: req.query.price,
        year: req.query.year
    }

    var _id = Number(req.query._id);
    var idx = carList.findIndex(function(item, i) {
        return item._id == _id;
    });
    if(idx != -1) {
        carList[idx] = car;
    }
    
    res.redirect('/car/list');
})

const server = http.createServer(app);
server.listen(3000, function () {
    console.log(">>>>>>>>>>>>>> http://127.0.0.1:3000/car/list");
});



