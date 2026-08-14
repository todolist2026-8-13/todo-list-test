cat > app.js << 'EOF'
const input = document.querySelector('#todoInput');
const addBtn = document.querySelector('#addBtn');
const list = document.querySelector('#todoList');

addBtn.addEventListener('click', ()=>{
    let val = input.value.trim();
    if(!val) return;
    createItem(val);
    input.value = '';
})

function createItem(text){
    let li = document.createElement('li');
    li.innerHTML = `
        <span class="text">${text}</span>
        <div>
            <button class="ok">完成</button>
            <button class="del">删除</button>
        </div>
    `
    li.querySelector('.ok').onclick = ()=>{
        li.classList.toggle('done')
    }
    li.querySelector('.del').onclick = ()=>{
        li.remove()
    }
    list.appendChild(li)
}
EOF

