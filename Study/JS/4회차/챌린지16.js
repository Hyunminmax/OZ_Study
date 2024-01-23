//1. 가위바위보
// 변수 선언
const   scissorsBtn = document.getElementById("scissors")
const   rockBtn     = document.getElementById("rock")
const   bojagiBtn   = document.getElementById("bojagi")
const   whoisWin    = document.getElementById("srbResult")

//버튼 선택시 함수 호출
scissorsBtn.addEventListener("click", whoisWinner)
rockBtn.addEventListener("click", whoisWinner)
bojagiBtn.addEventListener("click", whoisWinner)

//컴퓨터의 값 생성
function comsAnswer(){
    let comAnswer   
    comAnswer = Math.floor(Math.random() * 3) + 1
    if(comAnswer == 1){
        comAnswer = "가위"
    }else if(comAnswer == 2){
        comAnswer = "바위"
    }else if(comAnswer == 3){
        comAnswer = "보"
    }
    return comAnswer
}

//결과 표시
function displayWinner(c, u, winNum){
    if(winNum == 0){
        whoisWin.innerHTML = `당신의 선택 : ${u} VS 컴퓨터의 선택 : ${c} <br>결과는 무승부 입니다.`
    }else if(winNum == 1){
        whoisWin.innerHTML = `당신의 선택 : ${u} VS 컴퓨터의 선택 : ${c} <br>결과는 당신의 승리! 입니다.`
    }else{
        whoisWin.innerHTML = `당신의 선택 : ${u} VS 컴퓨터의 선택 : ${c} <br>결과는 당신의 패배 입니다. `
    }
}

//승리자 찾기 함수
function whoisWinner(){
    let com = comsAnswer()
    if(com == this.value){
        displayWinner(com, this.value, 0)
    }else if(com == "가위"){
        if(this.value == "바위"){
            displayWinner(com, this.value, 1)
        }else{
            displayWinner(com, this.value, 2)
        }
    }else if(com == "바위"){
        if(this.value == "보"){
            displayWinner(com, this.value, 1)
        }else{
            displayWinner(com, this.value, 2)
        }
    }else if(com == "보"){
        if(this.value == "가위"){
            displayWinner(com, this.value, 1)
        }else{
            displayWinner(com, this.value, 2)
        }
    }
}



//2. 이미지 멈춰
//변수 선언
const   imageArea   = document.getElementById("imageArea")
const   stopBtn     = document.getElementById("stop")
let     imageChg    
let     imageNum    = 1

//정기적으로 백그라운드 이미지 변경하기
imagechg = setInterval(function() {

    imageArea.style.backgroundSize = "cover"
    if(imageNum == 1){
        imageArea.style.backgroundImage = "url(../../HTML/Images/meadow-4485609_1280.jpg)"
        imageNum += 1
    }else if(imageNum == 2){
        imageArea.style.backgroundImage = "url(../../HTML/Images/plant-4214358_1280.jpg)"
        imageNum += 1
    }else if(imageNum == 3){
        imageArea.style.backgroundImage = "url(../../HTML/Images/woman-1509956_1280.jpg)"
        imageNum = 1
    }
    
    
}, 500);
//이미지 정지
stopBtn.onclick = function(){
    clearInterval(imagechg)
}



//3. 아이스크림
//변수 선언
const   inputBtn    = document.getElementById("iceInput")
const   checkBtn    = document.getElementById("iceCheck")
const   listBtn     = document.getElementById("iceList")
const   titlesP     = document.getElementById("iceTitles")
const   containerDiv= document.getElementById("container3")
let     iceArr      = []

//버튼 클릭시 이벤트
//아이스크림추가
inputBtn.onclick    = function(){
    let temp = prompt("추가하고 싶은 아이스크림 이름을 하나만 적으세요.")
    if(iceArr.indexOf(temp) != -1){
        alert("이미 있는 아이스크림입니다.")
    }else{
        iceArr.push(temp)
    }
}
//아이스크림 확인
checkBtn.onclick    = function(){
    let count = 0
    while(count < iceArr.length){
        alert(iceArr[count])
        count += 1
    }
}
//아이스크림 목록출력
listBtn.onclick     = function(){
    const eachNumDiv = document.createElement("div")
    eachNumDiv.classList.add("eachnum")
    eachNumDiv.textContent = iceArr
    eachNumDiv.style.fontSize = "20px"
    eachNumDiv.style.fontWeight = "900"
    titlesP.textContent = "선택하신 아이스크림은 : "
    containerDiv.append(eachNumDiv)
}

