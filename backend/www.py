//模拟待办后端接口，模拟内存数据
let todoList = [];
let id = 1;

//新增待办
function addTodo(title){
    let todo = {id:id++, title:title, done:false}
    todoList.push(todo)
    return todo
}

//查询全部待办
function getTodoList(){
    return todoList
}

//修改待办完成状态
function updateTodo(todoId){
    let todo = todoList.find(item=>item.id === todoId)
    if(todo){
        todo.done = !todo.done
    }
    return todo
}

//删除待办
function deleteTodo(todoId){
    let index = todoList.findIndex(item=>item.id === todoId)
    if(index !== -1){
        todoList.splice(index,1)
        return true
    }
    return false
}

module.exports = {
    addTodo,
    getTodoList,
    updateTodo,
    deleteTodo
}

