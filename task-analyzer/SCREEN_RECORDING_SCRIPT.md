# Screen Recording Script - Smart Task Analyzer
## Complete Edge Case Testing Guide

### 🎬 Recording Setup (3-4 minutes total)

**Tools to use:**
- Windows: Press `Win + G` for Game Bar, then click record
- Or use: OBS Studio (free), Loom, or Screencastify

---

## 📋 Recording Script

### **Part 1: Introduction (30 seconds)**

**What to say/show:**
- "This is the Smart Task Analyzer - a Django application that helps prioritize tasks using a custom scoring algorithm."
- Show the main page loading
- Point out the interface: left side for input, right side for results

---

### **Part 2: Basic Functionality (1 minute)**

**Test 1: Fill Example**
- Click "Fill Example" button
- Show JSON being populated in textarea
- Explain: "This fills in sample tasks with different due dates and priorities"

**Test 2: Analyze Feature**
- Click "Analyze" button
- Show tasks appearing in results panel
- Point out:
  - Tasks sorted by score (highest first)
  - Priority badges (red = high, yellow = medium, green = low)
  - Score values displayed
- Say: "Tasks are automatically sorted by priority score"

**Test 3: Different Sorting Strategies**
- Change dropdown to "Fastest wins"
- Click "Analyze" again
- Show tasks re-sorted by estimated hours (shortest first)
- Change to "Deadline driven"
- Click "Analyze" again
- Show tasks sorted by due date (earliest first)

---

### **Part 3: Suggest Top 3 Feature (45 seconds)**

- Click "Suggest Top 3" button
- Show top 3 tasks appearing
- Point out the explanation text for each task
- Read one explanation out loud: "Notice how it explains why this task is prioritized - it mentions the due date, importance, and estimated hours"

---

### **Part 4: Edge Cases - CRITICAL (2 minutes)**

#### **Edge Case 1: Overdue Tasks**
- Clear the textarea
- Paste this JSON:
```json
[
  {
    "title": "Overdue urgent task",
    "due_date": "2020-01-01",
    "importance": 9,
    "estimated_hours": 2,
    "dependencies": []
  },
  {
    "title": "Future task",
    "due_date": "2026-12-31",
    "importance": 8,
    "estimated_hours": 1,
    "dependencies": []
  }
]
```
- Click "Analyze"
- **Point out:** "The overdue task from 2020 gets a much higher score (should be 100+ points) because it's overdue, even though the future task has higher importance"

#### **Edge Case 2: Missing Fields**
- Clear and paste:
```json
[
  {
    "title": "Task with missing importance",
    "due_date": "2025-12-01",
    "estimated_hours": 3
  },
  {
    "title": "Task with missing hours",
    "due_date": "2025-12-01",
    "importance": 7
  },
  {
    "title": "Task with no due date",
    "importance": 8,
    "estimated_hours": 2
  }
]
```
- Click "Analyze"
- **Point out:** "The app handles missing fields gracefully - it uses default values and still calculates scores"

#### **Edge Case 3: Invalid JSON**
- Clear the textarea
- Type invalid JSON: `{ "title": "test" }` (missing closing brace or array brackets)
- Click "Analyze"
- **Point out:** "See the error message? The app validates JSON and shows helpful error messages"

#### **Edge Case 4: Empty Array**
- Clear and paste: `[]`
- Click "Analyze"
- **Point out:** "Empty input is handled - shows 'No tasks to display'"

#### **Edge Case 5: Dependencies**
- Clear and paste:
```json
[
  {
    "title": "Task with dependencies",
    "due_date": "2025-12-01",
    "importance": 9,
    "estimated_hours": 2,
    "dependencies": [1, 2]
  },
  {
    "title": "Independent task",
    "due_date": "2025-12-01",
    "importance": 7,
    "estimated_hours": 1,
    "dependencies": []
  }
]
```
- Click "Analyze"
- **Point out:** "Tasks with unmet dependencies get a slight penalty in scoring"

#### **Edge Case 6: Very High/Low Values**
- Clear and paste:
```json
[
  {
    "title": "Extremely important task",
    "due_date": "2025-12-01",
    "importance": 10,
    "estimated_hours": 20,
    "dependencies": []
  },
  {
    "title": "Quick task",
    "due_date": "2025-12-01",
    "importance": 1,
    "estimated_hours": 0.5,
    "dependencies": []
  }
]
```
- Click "Analyze"
- **Point out:** "The algorithm handles extreme values correctly - very important tasks get high scores, quick tasks get bonus points"

#### **Edge Case 7: Due Today/Tomorrow**
- Clear and paste:
```json
[
  {
    "title": "Due today",
    "due_date": "2025-11-29",
    "importance": 5,
    "estimated_hours": 2,
    "dependencies": []
  },
  {
    "title": "Due tomorrow",
    "due_date": "2025-11-30",
    "importance": 5,
    "estimated_hours": 2,
    "dependencies": []
  }
]
```
- Click "Analyze"
- **Point out:** "Tasks due today or tomorrow get urgency bonuses - notice the higher scores"

---

### **Part 5: Suggest Top 3 Edge Cases (30 seconds)**

- Use the overdue task example from Edge Case 1
- Click "Suggest Top 3"
- **Point out:** "The explanation clearly states the task is overdue and needs immediate attention"

---

### **Part 6: Conclusion (15 seconds)**

- "The Smart Task Analyzer successfully handles all edge cases including overdue tasks, missing fields, invalid input, and various date scenarios. It provides intelligent prioritization with clear explanations."

---

## ✅ Edge Cases Checklist

Make sure you test ALL of these:

- [x] Overdue tasks (past due dates)
- [x] Missing importance field
- [x] Missing estimated_hours field
- [x] Missing due_date field
- [x] Invalid JSON format
- [x] Empty array
- [x] Tasks with dependencies
- [x] Extreme values (importance 10, hours 20+)
- [x] Tasks due today
- [x] Tasks due tomorrow
- [x] Different sorting strategies (Default, Fastest, Deadline)
- [x] Quick wins (low hours, high importance)
- [x] Suggest Top 3 with explanations

---

## 🎥 Recording Tips

1. **Speak clearly** - Explain what you're doing as you do it
2. **Show the screen** - Make sure all UI elements are visible
3. **Pause briefly** - Give viewers time to read error messages/results
4. **Highlight important parts** - Use mouse cursor to point at scores, badges, etc.
5. **Keep it under 5 minutes** - Edit out any long pauses or mistakes

---

## 📝 Quick Test Data

Save these JSON snippets to test quickly:

**Overdue:**
```json
[{"title": "Overdue", "due_date": "2020-01-01", "importance": 9, "estimated_hours": 2, "dependencies": []}]
```

**Missing Fields:**
```json
[{"title": "No importance", "due_date": "2025-12-01", "estimated_hours": 3}]
```

**Invalid JSON:**
```
{ "title": "broken"
```

**Empty:**
```
[]
```

---

Good luck with your recording! 🎬

