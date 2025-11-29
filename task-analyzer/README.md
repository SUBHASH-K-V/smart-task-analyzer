## Smart Task Analyzer

This mini-application helps you decide **what to work on first** by scoring and prioritizing tasks
based on their **urgency**, **importance**, **estimated effort**, and **dependencies**.

### How the Algorithm Works

Each task gets a numerical **score**; higher score means higher priority.

- **Urgency (due date)** – highest weight  
  - Overdue tasks get a large boost (+100).  
  - Tasks due today / tomorrow / within 3 or 7 days get progressively smaller boosts.  
  - Tasks far in the future get only a small baseline.  
  - Missing due dates are treated as medium-term with a neutral baseline.
- **Importance (1–10)** – strong weight  
  - The value is clamped between 1 and 10.  
  - Score contribution: `importance * 5`.  
  - This lets high-importance items outrank low-importance but still respects urgency.
- **Effort (estimated_hours)** – “quick wins” logic  
  - Tasks under 2 hours get a small bonus (+10) to encourage quick wins.  
  - Very large tasks (over 8 hours) get a small penalty (−5) so they don’t always dominate.
- **Dependencies**  
  - If a task has dependencies and some are still unmet (`dependencies` minus
    `completed_dependencies`), the score is slightly reduced (−10) because it may be blocked.

The final score is the sum of all these components. The `/analyze/` endpoint returns tasks sorted
by decreasing score; the `/suggest/` endpoint returns the **top 3 tasks** plus a human-readable
explanation of *why* each one is recommended.

### Project Structure

```text
task-analyzer/
├── backend/                  # Main Django Project Folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                    # App Folder
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Database structure
│   ├── scoring.py            # Custom scoring algorithm
│   ├── urls.py               # App-specific URLs
│   └── views.py              # API Logic
├── frontend/                 # Frontend Files
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── manage.py
├── db.sqlite3
└── requirements.txt
```

### Setup & Run Instructions

1. **Create and activate virtual environment (Windows example)**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

5. **Open the frontend**:
   - Open `frontend/index.html` directly in your browser  
   - Or serve it via a simple static server if preferred.

6. **Use the app**:
   - In the left panel, paste a JSON array of tasks, for example:
     ```json
     [
       {
         "title": "Finish assignment report",
         "due_date": "2025-11-30",
         "importance": 9,
         "estimated_hours": 3,
         "dependencies": []
       }
     ]
     ```
   - Choose a **sorting strategy**:
     - `Default (Smart score)` – uses the full scoring algorithm.
     - `Fastest wins` – prioritizes lower `estimated_hours`.
     - `Deadline driven` – sorts primarily by earliest due date.
   - Click **Analyze** to view all tasks sorted by priority.
   - Click **Suggest Top 3** to get the three best tasks for today, with explanations.

### Edge Cases

- **Past due dates** (e.g., due in 1990) are heavily prioritized as overdue.
- **Missing or invalid `importance`** defaults to 5 (medium importance).
- **Missing or invalid `estimated_hours`** defaults to 1 hour.
- **Missing `due_date`** is treated as a flexible, medium-term task.
- **Invalid JSON** input from the frontend shows a clear error message instead of crashing.



