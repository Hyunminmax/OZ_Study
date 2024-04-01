const todoList  = document.getElementById('todo-list')
const todoForm  = document.getElementById('todo-form')
let todoArr = [];

//로컬 저장소에 저장
function saveTodos(){
    const todoString = JSON.stringify(todoArr)
    localStorage.setItem("myTodos", todoString)
}


//로컬 저장소 열람
function loadTodos(){
    const myTodos = localStorage.getItem("myTodos")
    if(myTodos !== null){
        todoArr = JSON.parse(myTodos)
        displayTodos()
    }
}



//할일 등록, 열람, 수정, 삭제

//삭제
function handTodoDelBtnClick(clickedId){
    todoArr = todoArr.filter(function(aTodo){
        return aTodo.todoId !== clickedId
    })
    displayTodos()
    saveTodos()
}

//등록
todoForm.addEventListener("submit", function(e){
    e.preventDefault()
    const toBeAdded = {
        todoText    : todoForm.todo.value,
        todoId      : new Date().getTime(),
        todoDone    : false
    }
    todoForm.todo.value = ""
    todoArr.push(toBeAdded)
    displayTodos()
    saveTodos()
})

//수정
function handleTodoItemClick(clickedId){
    todoArr = todoArr.map(function(aTodo){
        if(aTodo.todoId === clickedId){
            return{
                ...aTodo, todoDone: !aTodo.todoDone
            }
        }else{
            return aTodo
        }
    })
    displayTodos()
    saveTodos()
}

//열람
function displayTodos(){
    todoList.innerHTML = ""
    todoArr.forEach(function(aTodo){
        const todoItem = document.createElement('li')
        const todoDelBtn = document.createElement('span')
        todoDelBtn.textContent = 'xxxxx'
        todoItem.textContent = aTodo.todoText
        todoItem.title = "클릭하면 완료됨"
        if(aTodo.todoDone){
            todoItem.classList.add("Done")
        }else{
            todoItem.classList.add("yet")
        }
        todoDelBtn.title = "클릭하면 삭제됨"

        todoItem.addEventListener("click", function(){
            handleTodoItemClick(aTodo.todoId)
        })

        todoDelBtn.addEventListener("click", function(){
            handTodoDelBtnClick(aTodo.todoId)
        })
        todoList.appendChild(todoDelBtn)
        todoList.appendChild(todoItem)
    })
}