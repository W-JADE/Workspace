// html 파일 외부의 자바스크립트
// External 방식의 Javascript
// onload 이벤트 핸들러에 호출되며 순서가 달라진다
document.body.bgColor = "green";

//DOM 선택
var externBtn = document.getElementById("externBtn");
// console.log(externBtn);

externBtn.onclick = function() {
    document.body.bgColor = "orange";
    alert("익스터널 OK!");
}