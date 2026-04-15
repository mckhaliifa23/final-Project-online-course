# 🎓 Django Online Course Application

A comprehensive Django-based online learning platform with integrated assessment features. This application allows instructors to create courses with lessons and exams, while students can enroll, learn, and take assessments to demonstrate their knowledge.

## ✨ Features

### For Students
- 📚 **Browse Courses** - View available online courses
- 📖 **Learn Lessons** - Access structured course content
- ✍️ **Take Exams** - Multiple choice assessments for each course
- 📊 **View Results** - Instant feedback with scores and pass/fail status
- 🏆 **Achievement System** - Congratulations messages upon passing (70%+ threshold)

### For Instructors
- 🎯 **Course Management** - Create and manage courses via Django Admin
- 📝 **Lesson Creation** - Add structured lessons to courses
- ❓ **Question Bank** - Create multiple choice questions with point values
- ✔️ **Choice Management** - Define correct/incorrect answers
- 📈 **Submission Tracking** - View all student submissions and scores

## 🛠️ Technologies Used

- **Backend**: Django 4.2
- **Database**: SQLite (default Django database)
- **Frontend**: Bootstrap 5
- **Language**: Python 3.9+
- **Authentication**: Django's built-in authentication system

## 📋 Requirements

- Python 3.9 or higher
- pip (Python package installer)
- Basic knowledge of Django administration

## 🚀 Installation & Setup

### Prerequisites
Ensure you have Python 3.9+ installed:
```bash
python3 --version
```

### Step 1: Clone or Download the Repository
```bash
git clone https://github.com/YOUR_USERNAME/django-online-course.git
cd django-online-course
```

### Step 2: Install Django
```bash
pip3 install django
```

### Step 3: Run Migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Step 4: Create a Superuser
```bash
python3 manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 5: Run the Development Server
```bash
python3 manage.py runserver
```

The application will be available at **http://localhost:8000/**

## 🎮 Usage

### Accessing the Application

1. **Home Page**: http://localhost:8000/
   - View all available courses

2. **Admin Panel**: http://localhost:8000/admin/
   - Login with superuser credentials
   - Manage courses, lessons, questions, and choices

3. **Course Detail**: http://localhost:8000/course/1/
   - View course content and lessons
   - Take exams

### Creating Content (via Admin Panel)

1. **Create a Course**:
   - Go to Admin → OnlineCourse → Courses
   - Add course name and description

2. **Add Lessons**:
   - Go to the Course
   - Add lessons with title, content, and order

3. **Create Questions**:
   - Go to Lessons
   - Add questions with grade points
   - Assign to course

4. **Add Choices**:
   - Go to Questions
   - Add 2+ choices per question
   - Mark the correct answer

### Taking an Exam

1. Navigate to a course page
2. Answer all multiple choice questions
3. Click "Submit Exam"
4. View instant results with score and feedback

## 📸 Screenshots

### Course List Page
![Course List](screenshots/course_list.png)
*Browse all available courses*

### Course Detail with Exam
![Course Detail](screenshots/course_detail.png)
*View lessons and take assessments*

### Exam Results
![Exam Results](screenshots/exam_results.png)
*Instant feedback with congratulations message*

### Admin Panel
![Admin Panel](screenshots/admin_panel.png)
*Manage all course content*

## 📁 Project Structure

```
django-online-course/
├── onlinecourse_project/         # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── onlinecourse/                 # Main application
│   ├── models.py                 # Database models
│   ├── views.py                  # View functions
│   ├── urls.py                   # URL routing
│   ├── admin.py                  # Admin configuration
│   └── templates/onlinecourse/   # HTML templates
│       ├── course_list.html
│       ├── course_details_bootstrap.html
│       ├── exam_result.html
│       └── my_submissions.html
├── manage.py                     # Django management script
└── README.md                     # This file
```

## 🗄️ Database Models

### Core Models

1. **Course**
   - Name and description
   - Timestamps for created/updated

2. **Lesson**
   - Belongs to a Course
   - Title, content, and order

3. **Question**
   - Belongs to Lesson and Course
   - Question text and grade points

4. **Choice**
   - Belongs to a Question
   - Choice text and correct/incorrect flag

5. **Submission**
   - Student's exam submission
   - Score, total score, pass/fail status
   - Timestamps

6. **SelectedChoice**
   - Links submissions to chosen answers
   - Tracks student responses

## 🎯 Key Features Explained

### Passing Threshold
Students must score **70% or higher** to pass an exam. The system automatically:
- Calculates the percentage score
- Determines pass/fail status
- Displays appropriate feedback

### Scoring System
- Each question has configurable grade points
- Correct answers earn full points
- Incorrect answers earn 0 points
- Total score calculated and displayed immediately

### Bootstrap Integration
The application uses Bootstrap 5 for:
- Responsive design
- Clean, modern UI
- Mobile-friendly interface
- Professional styling

## 🔐 Default Credentials

After running the test user script:
- **Admin**: username=`admin`, password=`admin123`
- **Student**: username=`student`, password=`student123`

## 📝 License

This project is created for educational purposes as part of a Django course assignment.

## 👤 Author

Created as a final project submission for Django Online Course Development.

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Framework
- Online Course Platform requirements

---

## 📞 Support

For issues or questions, please refer to the assignment guidelines or contact your instructor.

**Happy Learning! 🎓**
