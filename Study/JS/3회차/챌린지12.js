//1. 계산기

//계산기의 입력받기
const   keypad1         = document.getElementById("keypad1")
const   keypad2         = document.getElementById("keypad2")
const   keypad3         = document.getElementById("keypad3")
const   keypad4         = document.getElementById("keypad4")
const   keypad5         = document.getElementById("keypad5")
const   keypad6         = document.getElementById("keypad6")
const   keypad7         = document.getElementById("keypad7")
const   keypad8         = document.getElementById("keypad8")
const   keypad9         = document.getElementById("keypad9")
const   keypad0         = document.getElementById("keypad0")
const   keypadPlus      = document.getElementById("keypad+")
const   keypadMinus     = document.getElementById("keypad-")
const   keypadTimes     = document.getElementById("keypadX")
const   keypadDiv       = document.getElementById("keypad/")
const   keypadCancel    = document.getElementById("keypadC")
const   keypadCal       = document.getElementById("keypad=")
const   calField        = document.getElementById("calField")



//이벤트 리스너 설정
keypad1.onclick = function(){if(calField.value == 0){calField.value = 1}else{calField.value += 1}}
keypad2.onclick = function(){if(calField.value == 0){calField.value = 2}else{calField.value += 2}}
keypad3.onclick = function(){if(calField.value == 0){calField.value = 3}else{calField.value += 3}}
keypad4.onclick = function(){if(calField.value == 0){calField.value = 4}else{calField.value += 4}}
keypad5.onclick = function(){if(calField.value == 0){calField.value = 5}else{calField.value += 5}}
keypad6.onclick = function(){if(calField.value == 0){calField.value = 6}else{calField.value += 6}}
keypad7.onclick = function(){if(calField.value == 0){calField.value = 7}else{calField.value += 7}}
keypad8.onclick = function(){if(calField.value == 0){calField.value = 8}else{calField.value += 8}}
keypad9.onclick = function(){if(calField.value == 0){calField.value = 9}else{calField.value += 9}}
keypad0.onclick = function(){if(calField.value == 0){calField.value = 0}else{calField.value += 0}}
keypadTimes.onclick = function(){if(calField.value == 0){calField.value = 0}else{calField.value += "x"}}
keypadDiv.onclick = function(){if(calField.value == 0){calField.value = 0}else{calField.value += "/"}}
keypadMinus.onclick = function(){if(calField.value == 0){calField.value = 0}else{calField.value += "-"}}
keypadPlus.onclick = function(){if(calField.value == 0){calField.value = 0}else{calField.value += "+"}}
//다 지우고 0
keypadCancel.onclick = function(){calField.value = 0}//;tempCal = []; tempCal[0] = 0}
//계산 함수 호출
keypadCal.onclick = myCal

/* 아이폰 계산기 구현. 추후 재도전
//입력되어있던 숫자 받고 기호
keypadPlus.addEventListener('click', myCalInput)
//입력되어있던 숫자 받고 기호
keypadMinus.addEventListener('click', myCalInput)
//입력되어있던 숫자 받고 기호
keypadTimes.addEventListener('click', myCalInput)
//입력되어있던 숫자 받고 기호
keypaddiv.addEventListener('click', myCalInput)
//입력되어있던 값 연산 결과
keypadCal.addEventListener('click', myCal)

//입력 숫자 저장
function myCalInput(cal){
//    if(tempCal[0] == 0){
//        tempCal[0] = parseInt(calField.value)
//    }else 
    if(cal == "+"){
        tempCal.push(parseInt(calField.value))
    }else if(cal == "-"){
        tempCal.push(parseInt(calField.value))
    }else if(cal == "x"){
        tempCal.push(parseInt(calField.value))
    }else if(cal == "/"){
        tempCal.push(parseInt(calField.value))
    }
    console.log(tempCal)
}
*/


//입력 숫자 연산
function myCal(){
//tempCal 연산을 위한 임시값
    let tempCal = 0
    let array = calField.value.match(/(\d+|\+|\-|\*|\/)/g)
    let answer = 0

    for(let i = 0; i < array.length; i++){
        if(i % 2 == 0){
            tempCal += parseInt(array[i])
        }else{
            tempCal += array[i]
        }
    }
    answer = eval(tempCal)
    calField.value = answer 
}


//2. 구구단
//테이블 가지고 오기
const tableThs = document.getElementsByClassName("motherNum")
const tableTds = document.getElementsByClassName("childNum")
console.log(tableThs.length)
console.log(tableTds.length)


for(let i = 0; i < tableThs.length; i++){
    tableThs[i].textContent = (i+2)+"단"
}
for(let i = 0; i < tableThs.length; i++){
    let temp = ""
    for(let j = 0; j <= tableTds.length; j++){
        temp += `${i+2} X ${j+1} = ${(i+1)*j}<br>`    
    }
    tableTds[i].innerHTML = temp
}


//3. 카운트 다운
setInterval(function(){
    const nowTime = document.getElementById("nowTime")
    
    const now = new Date();
    
    let year    = now.getFullYear()
    let month   = now.getMonth() + 1
    let day     = now.getDate()
    let hour    = now.getHours()
    let min     = now.getMinutes()
    let sec     = now.getSeconds()
        
    nowTime.textContent = `현재날짜와 시간 : ${year}년${month}월${day}일 ${hour}:${min}:${sec}`
    
}, 1000)

    
//4. 스톱워치
let ms = 0, ss = 0, mm = 0, hh= 0
let stopwatchTimer
let startTime
let endTime

const runningTime = document.getElementById("watchTime")
const startBtn = document.getElementById("startTime")
const endBtn = document.getElementById("endTime")

//이벤트 리스너 설정
startBtn.onclick = start;
endBtn.onclick = end;


function start(){
    if(! startTime){
        startTime = new Date().getTime()
    }else{
        
    }
    
    stopwatchTimer = setInterval(function(){
        let nowTime = new Date().getTime()
        let newTime = new Date(nowTime - startTime)

        mm = newTime.getMinutes()
        ss = newTime.getSeconds()
        ms = Math.floor(newTime.getMilliseconds()/10)

        runningTime.textContent = `경과 시간: ${hh}:${mm}:${ss}:${ms}`
    }, 10)
    
    

}
function end(){
    clearInterval(stopwatchTimer)
}


function watch(){
/*
    ms ++
    if(ms >= 100){
        ms = 0;
        ss += 1;
    }
    if(ss >= 60){
        ss = 0;
        mm += 1;
    }
    if(mm >= 60){
        mm = 0;
        hh += 1;
    }
 */
    runningTime.textContent = `경과 시간: ${hh}:${mm}:${ss}:${ms}`

}