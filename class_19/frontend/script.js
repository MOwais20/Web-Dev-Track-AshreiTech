const API_BASE = "http://127.0.0.1:8000";

// --- Todo Handlers ---
document.getElementById("todo-form").onsubmit = async (e) => {
    e.preventDefault();
    const task = document.getElementById("todo-task").value;
    const user_id = document.getElementById("todo-user-id").value;
    if (!user_id || !task) return;
    await fetch(`${API_BASE}/todo/add-item`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id, task, done: false })
    });
    document.getElementById("todo-task").value = "";
    loadTodos(user_id);
};


document.getElementById("fetch-todos-btn").onclick = function() {
    const user_id = document.getElementById("todo-user-id").value;
    if (user_id) loadTodos(user_id);
};

async function loadTodos(user_id) {
    if (!user_id) return;
    const res = await fetch(`${API_BASE}/todo/get-items?user_id=${user_id}`);
    const data = await res.json();
    const list = document.getElementById("todo-list");
    list.innerHTML = "";
    data.items.forEach(item => {
        const li = document.createElement("li");
        li.className = item.done ? "done" : "";
        li.textContent = item.task;
        // Complete button
        if (!item.done) {
            const doneBtn = document.createElement("button");
            doneBtn.textContent = "Done";
            doneBtn.onclick = async () => {
                await fetch(`${API_BASE}/todo/update-item?item_id=${item._id}`, { method: "PUT" });
                loadTodos(user_id);
            };
            li.appendChild(doneBtn);
        }
        // Edit button
        const editBtn = document.createElement("button");
        editBtn.textContent = "Edit";
        editBtn.onclick = () => {
            const newTask = prompt("Edit task:", item.task);
            if (newTask) {
                fetch(`${API_BASE}/todo/update-item-task?item_id=${item._id}&task=${encodeURIComponent(newTask)}`, { method: "PUT" })
                    .then(() => loadTodos(user_id));
            }
        };
        li.appendChild(editBtn);
        // Delete button
        const delBtn = document.createElement("button");
        delBtn.textContent = "Delete";
        delBtn.onclick = async () => {
            await fetch(`${API_BASE}/todo/delete-item?item_id=${item._id}`, { method: "DELETE" });
            loadTodos(user_id);
        };
        li.appendChild(delBtn);
        list.appendChild(li);
    });
}
