//HTML 요서 선택

const todaySpan   = document.querySelector("#today")
const numbersDiv  = document.querySelector(".numbers")
const drawBtn     = document.querySelector("#draw")
const resetBtn    = document.querySelector("#reset")

let lottoNumbers = []

//날짜 추가
const today = new Date()
let year  = today.getFullYear()
let month = today.getMonth() + 1
let date  = today.getDate()
todaySpan.textContent = `${year}년 ${month}월 ${date}일 `


//화면에 추가
function paintNumber(number){
  const eachNumDiv = document.createElement("div")
  eachNumDiv.classList.add("eachnum")
  eachNumDiv.textContent = number
  numbersDiv.append(eachNumDiv)
}

//랜덤 숫자 6개 배열에 넣기
drawBtn.addEventListener("click", function(){
  if(lottoNumbers.length == 6){
    reset()
  }
  while(lottoNumbers.length < 6){
    let rn = Math.floor(Math.random() * 45) + 1
    if(lottoNumbers.indexOf(rn) === -1){
      lottoNumbers.push(rn)
      paintNumber(rn)
    }
  }
})

//리셋 버튼
resetBtn.addEventListener("click", reset)

//리셋
function reset(){
  lottoNumbers.splice(0,6)
  numbersDiv.innerHTML = ""
}