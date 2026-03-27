async function fetchTasks() {
    const res = await fetch('/tasks');
    const data = await res.json();

    const list = document.getElementById('taskList');
    list.innerHTML = "";

    data.forEach(task => {
        const li = document.createElement('li');
        li.innerHTML = `${task[1]} 
            <button onclick="deleteTask(${task[0]})">Delete</button>`;
        list.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById('taskInput');

    await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: input.value })
    });

    input.value = "";
    fetchTasks();
}

async function deleteTask(id) {
    await fetch(`/tasks/${id}`, { method: 'DELETE' });
    fetchTasks();
}

fetchTasks();