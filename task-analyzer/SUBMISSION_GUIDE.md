# Submission Guide - Smart Task Analyzer

## 📋 Submission Checklist

### Submission 1: Publish Your Project

**Option A: Deploy to Railway (Recommended - Free & Easy)**
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variables if needed
6. Railway will auto-detect Django and deploy
7. Get your live URL (e.g., `https://your-app.railway.app`)

**Option B: Deploy to Render (Free Tier Available)**
1. Go to https://render.com
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Settings:
   - Build Command: `pip install -r requirements.txt && python manage.py migrate`
   - Start Command: `python manage.py runserver 0.0.0.0:$PORT`
6. Deploy and get your URL

**Option C: Deploy to PythonAnywhere (Free Tier)**
1. Go to https://www.pythonanywhere.com
2. Sign up for free account
3. Upload your code via Files tab
4. Set up Web app in Web tab
5. Configure WSGI file to point to your Django app

**For all deployments, you'll need to:**
- Set `ALLOWED_HOSTS` in `backend/settings.py` to include your domain
- Set `DEBUG = False` for production
- Configure static files serving
- Set up a production database (PostgreSQL recommended)

---

### Submission 2: GitHub Repository & ZIP File

#### Step 1: Initialize Git Repository

```bash
cd C:\Users\subha\OneDrive\Desktop\project\task-analyzer
git init
git add .
git commit -m "Initial commit: Smart Task Analyzer"
```

#### Step 2: Create GitHub Repository

1. Go to https://github.com
2. Click "New repository"
3. Name it: `smart-task-analyzer` (or your preferred name)
4. **DO NOT** initialize with README, .gitignore, or license
5. Click "Create repository"

#### Step 3: Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/smart-task-analyzer.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

#### Step 4: Download ZIP from GitHub

1. Go to your repository on GitHub
2. Click the green "Code" button
3. Click "Download ZIP"
4. Save the ZIP file

#### Step 5: Upload to Google Drive

1. Go to https://drive.google.com
2. Click "New" → "File upload"
3. Upload the ZIP file
4. Right-click the file → "Share" → "Get link"
5. Set permission to "Anyone with the link can view"
6. Copy the shareable link

**Submit:**
- GitHub repository link: `https://github.com/YOUR_USERNAME/smart-task-analyzer`
- Google Drive ZIP link: `https://drive.google.com/file/d/...`

---

### Submission 3: Screen Recording

#### What to Record:

1. **Project Overview (30 seconds)**
   - Show the main page loading
   - Explain what the app does

2. **Fill Example Feature (30 seconds)**
   - Click "Fill Example" button
   - Show the JSON being populated

3. **Analyze Feature (1 minute)**
   - Click "Analyze" button
   - Show tasks being sorted by score
   - Explain the priority colors (red=high, yellow=medium, green=low)
   - Try different sorting strategies (Default, Fastest, Deadline)

4. **Suggest Top 3 Feature (1 minute)**
   - Click "Suggest Top 3" button
   - Show the top 3 tasks with explanations
   - Read one explanation out loud

5. **Edge Cases (30 seconds)**
   - Show what happens with overdue tasks (they get high priority)
   - Show error handling (try invalid JSON)

**Total video length: ~3-4 minutes**

#### Recording Tools:

**Windows:**
- Built-in: Press `Win + G` to open Game Bar, click record
- OBS Studio (free): https://obsproject.com
- ShareX (free): https://getsharex.com

**Online:**
- Loom (free): https://www.loom.com
- Screencastify (Chrome extension)

#### Upload to Google Drive:

1. Record your video
2. Save the video file (MP4 format recommended)
3. Upload to Google Drive
4. Right-click → "Share" → "Get link"
5. Set permission to "Anyone with the link can view"
6. Copy the shareable link

**Submit:** Google Drive video link

---

## 📝 Quick Commands Reference

```bash
# Activate virtual environment
venv\Scripts\activate

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver

# Create superuser (optional, for admin access)
python manage.py createsuperuser
```

---

## ✅ Final Submission Checklist

- [ ] Project deployed and live URL working
- [ ] GitHub repository created and code pushed
- [ ] ZIP file downloaded from GitHub and uploaded to Google Drive
- [ ] Screen recording created and uploaded to Google Drive
- [ ] All three links ready to submit:
  - [ ] Published project URL
  - [ ] GitHub repository link
  - [ ] Google Drive ZIP link
  - [ ] Google Drive video link

---

## 🆘 Troubleshooting

**If GitHub push fails:**
- Make sure you've committed all files first
- Check your GitHub username is correct
- You may need to authenticate (GitHub will prompt you)

**If deployment fails:**
- Check that `requirements.txt` includes all dependencies
- Make sure `ALLOWED_HOSTS` includes your domain
- Check deployment logs for specific errors

**If video is too large:**
- Compress the video using HandBrake (free): https://handbrake.fr
- Or upload to YouTube as unlisted and share that link

Good luck with your submission! 🚀

