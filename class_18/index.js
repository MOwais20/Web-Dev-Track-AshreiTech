// Load todos from localStorage or use default items
let todo_items = [];

function addTodo() {
  const todoInput = document.getElementById("todo-input");
  const user_input = todoInput.value.trim();

  if (user_input === "") {
    alert("Please enter a valid todo item.");
    return;
  }

  // Core Functionality of adding a todo item
  // todo_items.push(user_input);

  // fetch('http://localhost:8000/add_todo', {
  //     method: 'POST',
  //     headers: {
  //         'Content-Type': 'application/json',
  //     },
  //     body: JSON.stringify({ item: user_input }),
  // })
  // .then(response => response.json())
  // .then(data => {
  //     todo_items = data.todos;
  //     renderTodoList();
  // })
  // .catch((error) => {
  //     console.error('Error:', error);
  // });

  const payload = {
    id: 1,
    task: user_input,
    done: false,
  };

  fetch("http://127.0.0.1:8000/todo/add-item", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer YOUR_ACCESS_TOKEN",
    },
    body: JSON.stringify(payload),
  })
  .then(async (response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok " + response.statusText);
    }
    let dataFromServer = await response.json();
    console.log("🚀 ~ addTodo ~ dataFromServer:", dataFromServer)

    if (dataFromServer.success) {
        alert("Item added successfully to the server!");
    }
    
  })
  .catch((error) => {
    console.error("Error From Server:", error);
  });

  todoInput.value = "";
  saveTodos();
  renderTodoList();
}

// Function to save todos to localStorage
function saveTodos() {
  localStorage.setItem("todos", JSON.stringify(todo_items));
}

async function renderTodoList() {

 let todoItems = await fetch('http://localhost:8000/todo/get-items')
 todoItems = await todoItems.json()

 console.log("🚀 ~ renderTodoList ~ todoItems:", todoItems)

    


  const todoList = document.getElementById("todo-list");
  todoList.innerHTML = "";

  todoItems.items.forEach((item, index) => {
    const card = document.createElement("div");
    card.className = "card p-4 rounded";
    card.innerHTML = `
          <div class="flex items-center justify-between shadow p-3 px-5 rounded-xl bg-gray-300">
            <p class="text-gray-700">${item.task}</p>
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
