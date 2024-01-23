//회원가입 페이지의 데이터 받기

//오브젝트와 연결할 const값
const doc_email             = document.getElementById("email")
const doc_name              = document.getElementById("name")
const doc_password          = document.getElementById("PW")
const doc_password_check    = document.getElementById("pw_check")
const doc_tel1_1            = document.getElementById("tel_1")
const doc_tel1_2            = document.getElementById("tel_2")
const doc_tel1_3            = document.getElementById("tel_3")
const doc_tel_check         = document.getElementById("tel_check")
const doc_location          = document.getElementById("location")
const doc_sex               = document.getElementsByName("radio_sex")


//값 받을 변수 
let email           = ""
let name            = "" 
let password        = ""
let password_check  = ""
let tel1_1          = ""
let tel1_2          = ""
let tel1_3          = ""
let tel_check       = ""
let local_location  = "" //location은 예약어인듯 오류가 발생해서 앞에 local_을 붙임
let sex             = ""

//submit 버튼 type을 submit으로 하면 JS파일에서 콘솔에 찍자마자 바로 리플래쉬되어 임시로 button으로 변경
const submitBtn = document.getElementById("submit")
submitBtn.onclick = function(){
//변수에 값 할당
    email = doc_email.value
    name = doc_name.value   
    password= doc_password.value    
    password_check = doc_password_check.value
    tel1_1 = doc_tel1_1.value
    tel1_2 = doc_tel1_2.value  
    tel1_3 = doc_tel1_3.value  
    tel_check = doc_tel_check.value  
    local_location = doc_location.value
    
    if(doc_sex[0].checked){
        sex = "male"
    }else{
        sex = "female"
    }

    
    
    console.log(email)
    console.log(name)
    console.log(password)
    console.log(password_check)
    console.log(tel1_1)
    console.log(tel1_2)
    console.log(tel1_3)
    console.log(tel_check)
    console.log(local_location)
    console.log(sex)
}
