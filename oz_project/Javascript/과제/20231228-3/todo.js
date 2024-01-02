const todoList = document.getElementById('todo-list');
const todoForm = document.getElementById('todo-form');
let todoArr = [];


//로컬 저장소에 저장하기
function saveTodos(){
    const todoString = JSON.stringify(todoArr);
    localStorage.setItem("myTods", todoString);
}

//로컬 저장소에서 가져오기
function loadTodos(){
    const myTodos = localStorage.getItem("myTodos");
    if(myTodos !== null){
        todoArr =JSON.parse(mytodos);
        displayTodos();
    }
    
}
loadTodos();

//할일 삭제하기
function handleTodoDelBtnClick(clickedId){
    todoArr = todoArr.filter(function(aTodo){
        return aTodo.todoId !== clickedId;
    })
    displayTodos();
    saveTodos();
}


//할일 수정하기
function handleTodoItemClick(clickedId){
    todoArr = todoArr.map(function(aTodo){
        if(aTodo.todoId === clickedId){
            return{
                ...aTodo, 
                todoDone: !aTodo.todoDone
            }
        } else {
            return aTodo
        }
    })
    displayTodos();
    saveTodos();
    
}

//할일 보여주기
function displayTodos(){
    todoList.innerHTML = "";
    todoArr.forEach(function(aTodo){
        const todoItem = document.createElement('li');
        const todoDelBtn = document.createElement('span');
        todoDelBtn.textContent = 'x';
        todoItem.textContent = aTodo.todoText;
        todoItem.title = "클릭하면 완료됨";
        if(aTodo.todoDone){
            todoItem.classList.add("done")
        } else {
            todoItem.classList.add("yet")
        }
        todoDelBtn.title = "클릭하면 삭제됨";

        todoItem.addEventListener("click", function(){
            handleTodoItemClick(aTodo.todoId);
        })
        todoDelBtn.addEventListener("click",function(){
            handleTodoDelBtnClick(aTodo.todoId);
        })
        todoItem.appendChild(todoDelBtn);
        todoList.appendChild(todoItem);
    })
}

//할일 추가하기
todoForm.addEventListener("submit", function(e){
    e.preventDefault();
    const toBeAdded = {
        todoText : todoForm.todo.value, 
        todoId : new Date().getTime(),
        todoDone : false
    }
    todoForm.todo.value ="";
    todoArr.push(toBeAdded);
    displayTodos();
    saveTodos();
    // console.log(todoArr);
})

//
