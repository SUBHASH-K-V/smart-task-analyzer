const API_BASE = "/api/tasks";
const taskJsonEl = document.getElementById("task-json");
const strategyEl = document.getElementById("strategy");
const errorEl = document.getElementById("error");
const resultsEl = document.getElementById("results");

const btnFillExample = document.getElementById("btn-fill-example");
const btnAnalyze = document.getElementById("btn-analyze");
const btnSuggest = document.getElementById("btn-suggest");

function setError(message) {
  errorEl.textContent = message || "";
}

function fillExample() {
  const today = new Date();
  const tomorrow = new Date(today);
  tomorrow.setDate(today.getDate() + 1);
  const inThree = new Date(today);
  inThree.setDate(today.getDate() + 3);
  const lastWeek = new Date(today);
  lastWeek.setDate(today.getDate() - 7);

  const fmt = (d) => d.toISOString().slice(0, 10);

  const example = [
    {
      title: "Finish assignment report",
      due_date: fmt(tomorrow),
      importance: 9,
      estimated_hours: 3,
      dependencies: [],
    },
    {
      title: "Pay electricity bill",
      due_date: fmt(lastWeek),
      importance: 8,
      estimated_hours: 0.5,
      dependencies: [],
    },
    {
      title: "Refactor old codebase",
      due_date: fmt(inThree),
      importance: 6,
      estimated_hours: 10,
      dependencies: [],
    },
    {
      title: "Plan weekend trip",
      due_date: fmt(inThree),
      importance: 4,
      estimated_hours: 2,
      dependencies: [],
    },
  ];

  taskJsonEl.value = JSON.stringify(example, null, 2);
  setError("");
}

function parseTasksFromTextarea() {
  const raw = taskJsonEl.value.trim();
  if (!raw) {
    throw new Error("Please paste an array of tasks in JSON format.");
  }
  let parsed;
  try {
    parsed = JSON.parse(raw);
  } catch (e) {
    throw new Error("Invalid JSON. Make sure your input is valid JSON.");
  }
  if (!Array.isArray(parsed)) {
    throw new Error("Top-level JSON should be an array of task objects.");
  }
  return parsed;
}

function getPriorityClass(score) {
  if (score >= 120) return "priority-high";
  if (score >= 80) return "priority-medium";
  return "priority-low";
}

function renderTasks(tasks, withExplanations = false) {
  resultsEl.innerHTML = "";
  if (!tasks || tasks.length === 0) {
    resultsEl.innerHTML = "<p>No tasks to display.</p>";
    return;
  }

  tasks.forEach((item, idx) => {
    const t = withExplanations ? item.task || item : item;
    const reason = withExplanations ? item.reason : null;

    const title = t.title || `Task #${idx + 1}`;
    const score = typeof t.score === "number" ? t.score : 0;
    const importance = t.importance ?? "?";
    const est = t.estimated_hours ?? "?";
    const due = t.due_date || "N/A";

    const priorityClass = getPriorityClass(score);
    const priorityLabel =
      priorityClass === "priority-high"
        ? "High priority"
        : priorityClass === "priority-medium"
          ? "Medium priority"
          : "Low priority";

    const card = document.createElement("article");
    card.className = "task-card";

    card.innerHTML = `
      <div class="task-main">
        <div class="task-title">${title}</div>
        <div class="task-meta">
          Due: <strong>${due}</strong> · Importance: <strong>${importance}</strong>/10 · Est: <strong>${est}</strong>h
        </div>
        <span class="task-badge ${priorityClass}">${priorityLabel}</span>
      </div>
      <div class="score-pill">
        Score: <strong>${score.toFixed(1)}</strong>
      </div>
      ${reason
        ? `<div class="explanation">${reason}</div>`
        : ""
      }
    `;

    resultsEl.appendChild(card);
  });
}

async function analyze() {
  setError("");
  try {
    const tasks = parseTasksFromTextarea();
    const strategy = strategyEl.value;

    const res = await fetch(`${API_BASE}/analyze/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ tasks, strategy }),
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Server error (${res.status}): ${text}`);
    }

    const data = await res.json();
    renderTasks(data.tasks || []);
  } catch (e) {
    console.error(e);
    setError(e.message || "Something went wrong while analyzing tasks.");
  }
}

async function suggest() {
  setError("");
  try {
    const tasks = parseTasksFromTextarea();
    const res = await fetch(`${API_BASE}/suggest/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ tasks }),
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Server error (${res.status}): ${text}`);
    }

    const data = await res.json();
    renderTasks(data.suggestions || [], true);
  } catch (e) {
    console.error(e);
    setError(e.message || "Something went wrong while fetching suggestions.");
  }
}

btnFillExample.addEventListener("click", fillExample);
btnAnalyze.addEventListener("click", analyze);
btnSuggest.addEventListener("click", suggest);

// Pre-fill an example on load for convenience
fillExample();



