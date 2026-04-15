# 📸 Screenshot Guide for Django Online Course Project

## Application Status: ✅ RUNNING

The Django server is running at **http://localhost:8000/**

---

## 📝 Screenshot 1: Admin Site (03-admin-site.png)

### Steps:
1. Open your browser and go to: **http://localhost:8000/admin/**
2. Login with:
   - Username: `admin`
   - Password: `admin123`
3. **IMPORTANT**: The screenshot MUST show:
   - ✅ "Authentication and Authorization" section (User, Group models)
   - ✅ "OnlineCourse" section with all models:
     - Courses
     - Choices
     - Lessons
     - Questions
     - Selected choices
     - Submissions
4. Take a screenshot and save it as `03-admin-site.png`

### What it should look like:
```
Django administration
-------------------
Authentication and Authorization
- Groups
- Users

OnlineCourse
- Courses
- Choices
- Lessons
- Questions
- Selected choices
- Submissions
```

---

## 📝 Screenshot 2: Final Result Page (07-final.png)

### Steps:
1. First, make sure you're logged in as a student (or create one):
   - Go to **http://localhost:8000/admin/**
   - Login as admin: `admin` / `admin123`
   - Under "Authentication and Authorization", click "Users"
   - Create a new user (or use existing: `student` / `student123`)

2. Take the exam:
   - Go to: **http://localhost:8000/course/1/** (Python Programming Fundamentals)
   - Answer all 5 questions (correct answers: x=5, char, print('Hello'), 8, len())
   - Click "Submit Exam"

3. **IMPORTANT**: The screenshot MUST show:
   - ✅ "Congratulations!" message
   - ✅ Score display (e.g., "50/50" or percentage)
   - ✅ Pass/Fail indicator
   - ✅ Exam feedback

4. Take a screenshot and save it as `07-final.png`

### What it should look like (if you pass):
```
🎉 Congratulations!
You have passed the exam!

Python Programming Fundamentals

50.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your Score: 50 out of 50

✓ Passed!
Excellent work! You have successfully completed this assessment.
```

---

## 🎯 Quick Test Answers (to pass with 100%):

**Python Course (5 questions, 50 points total):**
1. What is the correct way to create a variable in Python?
   → `x = 5`

2. Which of the following is NOT a Python data type?
   → `char`

3. How do you print output in Python?
   → `print('Hello')`

4. What is the result of 2 ** 3 in Python?
   → `8`

5. Which function is used to get the length of a string?
   → `len()`

**Web Development Course (3 questions, 30 points total):**
1. What does HTML stand for?
   → `Hyper Text Markup Language`

2. Which tag is used for the largest heading?
   → `<h1>`

3. Which CSS property changes text color?
   → `color`

---

## 🌐 Important URLs:

- Home: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- Python Course: http://localhost:8000/course/1/
- Web Course: http://localhost:8000/course/2/

---

## 📋 After Taking Screenshots:

Once you have both screenshots:
1. Save them in the project directory (or a screenshots folder)
2. Ensure filenames are exactly:
   - `03-admin-site.png`
   - `07-final.png`
3. Proceed to Phase 3: GitHub Submission
