//테이블 값 배열로 받기

//DOM 설정
const table     = document.getElementById('scoreTable')
const names     = document.getElementById('highScoreNames')

//테이블 행 수 확인
const tableRow  = table.rows.length

//테이블 배열화
//let cnt = 0 //while문에서 사용하려고 했으나 오류남.
let tableArr = []

let temp1
let temp2

//75점 초과자 배열
let highScoreArr = []

//
/* 
console.log(table.rows[cnt+1].cells[0].innerText)
똑같은 내용을 while 내부에서 실행하면 오류남. 
let temp = table.rows[cnt+1].cells[0].innerText
console.log(temp)
tableArr.push(table.rows[1].cells[0].innerText, table.rows[1].cells[1].innerText)

while(cnt <= tableRow){
    temp1 = table.rows[cnt+1].cells[0].innerText
    temp2 = table.rows[cnt+1].cells[1].innerText

    tableArr.push(temp1, temp2)
    cnt ++
}
*/
//
//배열에 넣기
for(let i = 1; i < tableRow; i ++){
    temp1 = table.rows[i].cells[0].innerText
    temp2 = table.rows[i].cells[1].innerText
    tableArr.push([temp1, temp2])
}
/*
//75점 이상만 추려내기
for(let i = 0; i < tableArr.length; i ++){
    if(tableArr[i][1] >= 75){
        highScoreArr.push([tableArr[i][0], [tableArr[i][1]]])
    }
}
*/

//추려서 배열에 넣기2 필터
highScoreArr = tableArr.filter(score => score[1] >= 75)

console.log('75점 이상: '+highScoreArr)


//화면에 뿌리기
names.textContent = highScoreArr









  