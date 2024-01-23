//카운트다운 타이머
/*  필요사항
    1. 현시간
    2. 목표시간
    3. #알람타이머? 1시간으로 세팅하면 목표시간 1시간 전부터 타이머 자동으로 시작


    */



//목표시간 24년6월23일13시?12시? 아... 몇 시더라. ㅠㅜ 일단 13시.
let targetTime = new Date(2024, 5, 23, 13)

function countDown(){
    //현시간
    let nowTime = new Date()

    //두 시간의 차이
    let cntTime   = targetTime - nowTime

    //시간 할당에 필요한 DOM 연결
    const days  = document.getElementById('days')
    const hours = document.getElementById('hours')
    const min   = document.getElementById('min')
    const sec   = document.getElementById('sec')

    //시간 한번에 계산
    let [cal_days, cal_hours, cal_min, cal_sec, cal_msec] = [
        Math.floor(cntTime / (1000 * 60 * 60 * 24)),                        //전체에서 날로 나눈 몫
        Math.floor((cntTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),   //전체에서 날로 나눈 나머지(시간)
        Math.floor((cntTime % (1000 * 60 * 60)) / (1000 * 60)),             //전체에서 시간으로 나눈 나머지(분)
        Math.floor((cntTime % (1000 * 60)) / 1000),                         //전체에서 분으로 나눈 나머지
        Math.floor((cntTime % (1000)))                                      //전체에서 초로 나눈 나머지
    ]
    //화면에 표시
    days.textContent    = cal_days  + "일 "
    hours.textContent   = cal_hours + "시 "
    min.textContent     = cal_min   + "분 "
    sec.textContent     = cal_sec   + "초 "
}

//시간 표시 반복 실행 필요
setInterval(countDown, 1000);

//알람 설정 시간 받기
const   alarm       = document.getElementById("getTime")
const   alarmBtn    = document.getElementById("checkBtn") 
const   checkAlarm  = document.getElementById("checkAlarmTime")
let     alarmTime   = []

//Btn클릭시 인풋값 받기 
alarmBtn.addEventListener("click", function(){
alarmTime = alarm.value.split(',')
checkAlarm.textContent = "당신이 입력한 시간은 " + alarmTime[0] + "년" +  alarmTime[1] + "월" + alarmTime[2]+ "일" + alarmTime[3] + "시" + alarmTime[4] + "분" + alarmTime[5] + "초 입니다."
setInterval(function(){alarmCount(alarmTime)}, 1000);
})

// 2024,01,23,10,00,00



//입력받은 시간으로 알림하기
function alarmCount(targetTime){
    const target = new Date(targetTime[0],targetTime[1]-1,targetTime[2],targetTime[3],targetTime[4],targetTime[5])
    
    //현시간
    let nowTime = new Date()

    //5초 전 찾기
    let cntTime   = target - nowTime

    //시간 할당에 필요한 DOM 연결
    const days  = document.getElementById('targetDays')
    const hours = document.getElementById('targetHours')
    const min   = document.getElementById('targetMin')
    const sec   = document.getElementById('targetSec')

    //시간 한번에 계산
    let [cal_days, cal_hours, cal_min, cal_sec, cal_msec] = [
        Math.floor(cntTime / (1000 * 60 * 60 * 24)),                        //전체에서 날로 나눈 몫
        Math.floor((cntTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),   //전체에서 날로 나눈 나머지(시간)
        Math.floor((cntTime % (1000 * 60 * 60)) / (1000 * 60)),             //전체에서 시간으로 나눈 나머지(분)
        Math.floor((cntTime % (1000 * 60)) / 1000),                         //전체에서 분으로 나눈 나머지
        Math.floor((cntTime % (1000)))                                      //전체에서 초로 나눈 나머지
    ]

    if (cal_days == 0 && cal_hours == 0 && cal_min == 0 && cal_sec <= 5){
        //화면에 표시
        days.textContent    = cal_days  + "일 "
        hours.textContent   = cal_hours + "시 "
        min.textContent     = cal_min   + "분 "
        sec.textContent     = cal_sec   + "초 "
    }
}