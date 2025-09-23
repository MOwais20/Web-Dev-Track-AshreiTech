// Load todos from localStorage or use default items
let todo_items = [];

function addTodo() {
  const todoInput = document.getElementById("todo-input");
  const user_input = todoInput.value.trim();

  if (user_input === "") {
    alert("Please enter a valid todo item.");
    return;
  }

  const payload = {
    id: crypto.randomUUID(),
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

async function updateTodoListOnFrontend() {
  const todoList = document.getElementById("todo-list");
  todoList.innerHTML = "";

  todo_items.forEach((item, index) => {
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

async function renderTodoList() {

 let todoItems = await fetch('http://localhost:8000/todo/get-items')
 todoItems = await todoItems.json()

 console.log("🚀 ~ renderTodoList ~ todoItems:", todoItems)


  todo_items = [...todoItems.items, ...todo_items];

  const todoList = document.getElementById("todo-list");
  todoList.innerHTML = "";

  todo_items.forEach((item, index) => {
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
  const todo_item_in_list = todo_items[index];
  todo_items.splice(index, 1);

  // Update the list on the frontend 
  // updateTodoListOnFrontend();

  fetch(`http://localhost:8000/todo/delete-item?item_id=${todo_item_in_list.id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    },
    // body: JSON.stringify({ item_id: parseInt(todo_item_in_list.id) })
  })
  .then(async (response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok " + response.statusText);
    }
    let dataFromServer = await response.json();
    console.log("🚀 ~ deleteTodo ~ dataFromServer:", dataFromServer)

    if (dataFromServer.success) {
      renderTodoList();
      alert("Item deleted successfully from the server!");
    }
  })
  .catch((error) => {
    console.error("Error From Server:", error);
  });

  
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
