// Load todos from localStorage or use default items
let todo_items = [];



function addTodo() {
    const todoInput = document.getElementById("todo-input");
    const user_input = todoInput.value.trim();

    if (user_input === "") {
        alert("Please enter a valid todo item.");
        return;
    }

    todo_items.push(user_input);
    todoInput.value = "";
    saveTodos();
    renderTodoList();
}

// Function to save todos to localStorage
function saveTodos() {
    localStorage.setItem('todos', JSON.stringify(todo_items));
}

function renderTodoList() {
    const todoList = document.getElementById("todo-list");
    todoList.innerHTML = "";

    todo_items.forEach((item, index) => {
        const card = document.createElement("div");
        card.className = "card p-4 rounded";
        card.innerHTML = `
          <div class="flex items-center justify-between shadow p-3 px-5 rounded-xl bg-gray-300">
            <p class="text-gray-700">${item}</p>
            <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded" onclick="deleteTodo(${index})">
              Delete
            </button>
          </div>
        `;
        todoList.appendChild(card);
    });
}

function deleteTodo(index) {
    todo_items.splice(index, 1);
    saveTodos();
    renderTodoList();
}

// Add event listeners
// document.getElementById("addItemButton").addEventListener("click", addTodo);
document.getElementById("todo-input").addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        addTodo();
    }
});

// Initial render
renderTodoList();