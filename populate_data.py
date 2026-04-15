#!/usr/bin/env python3
"""
Script to populate sample data for testing the Online Course Application
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinecourse_project.settings')
django.setup()

from onlinecourse.models import Course, Lesson, Question, Choice


def create_sample_data():
    """Create sample courses, lessons, questions, and choices"""

    # Create Course 1: Python Programming
    python_course = Course.objects.create(
        name="Python Programming Fundamentals",
        description="Learn the basics of Python programming from scratch."
    )

    # Create lessons for Python course
    lesson1 = Lesson.objects.create(
        course=python_course,
        title="Introduction to Python",
        content="Python is a high-level, interpreted programming language known for its simplicity and readability.",
        order=1
    )

    lesson2 = Lesson.objects.create(
        course=python_course,
        title="Variables and Data Types",
        content="Learn about variables, integers, floats, strings, and more in Python.",
        order=2
    )

    # Create questions for Python course
    q1 = Question.objects.create(
        course=python_course,
        lesson=lesson1,
        question_text="What is the correct way to create a variable in Python?",
        grade_point=10
    )
    Choice.objects.bulk_create([
        Choice(question=q1, choice_text="var x = 5", is_correct=False),
        Choice(question=q1, choice_text="x = 5", is_correct=True),
        Choice(question=q1, choice_text="let x = 5", is_correct=False),
        Choice(question=q1, choice_text="int x = 5", is_correct=False),
    ])

    q2 = Question.objects.create(
        course=python_course,
        lesson=lesson1,
        question_text="Which of the following is NOT a Python data type?",
        grade_point=10
    )
    Choice.objects.bulk_create([
        Choice(question=q2, choice_text="int", is_correct=False),
        Choice(question=q2, choice_text="str", is_correct=False),
        Choice(question=q2, choice_text="char", is_correct=True),
        Choice(question=q2, choice_text="float", is_correct=False),
    ])

    q3 = Question.objects.create(
        course=python_course,
        lesson=lesson2,
        question_text="How do you print output in Python?",
        grade_point=10
    )
    Choice.objects.bulk_create([
        Choice(question=q3, choice_text="print('Hello')", is_correct=True),
        Choice(question=q3, choice_text="echo('Hello')", is_correct=False),
        Choice(question=q3, choice_text="console.log('Hello')", is_correct=False),
        Choice(question=q3, choice_text="write('Hello')", is_correct=False),
    ])

    q4 = Question.objects.create(
        course=python_course,
        lesson=lesson2,
        question_text="What is the result of 2 ** 3 in Python?",
        grade_point=10
    )
    Choice.objects.bulk_create([
        Choice(question=q4, choice_text="5", is_correct=False),
        Choice(question=q4, choice_text="6", is_correct=False),
        Choice(question=q4, choice_text="8", is_correct=True),
        Choice(question=q4, choice_text="9", is_correct=False),
    ])

    q5 = Question.objects.create(
        course=python_course,
        lesson=lesson2,
        question_text="Which function is used to get the length of a string?",
        grade_point=10
    )
    Choice.objects.bulk_create([
        Choice(question=q5, choice_text="length()", is_correct=False),
        Choice(question=q5, choice_text="len()", is_correct=True),
        Choice(question=q5, choice_text="size()", is_correct=False),
        Choice(question=q5, choice_text="count()", is_correct=False),
    ])

    # Create Course 2: Web Development
    web_course = Course.objects.create(
        name="Web Development Basics",
        description="Introduction to HTML, CSS, and JavaScript."
    )

    lesson3 = Lesson.objects.create(
        course=web_course,
        title="HTML Fundamentals",
        content="Learn the structure of HTML documents and common tags.",
        order=1
    )

    lesson4 = Lesson.objects.create(
        course=web_course,
        title="CSS Styling",
        content="Learn how to style web pages with CSS.",
        order=2
    )

    # Create questions for Web Development course
    q6 = Question.objects.create(
        course=web_course,
        lesson=lesson3,
        question_text="What does HTML stand for?",
        grade_point=10
    )
    Choice.objects.bulk_create([
        Choice(question=q6, choice_text="Hyper Text Markup Language", is_correct=True),
        Choice(question=q6, choice_text="High Tech Modern Language", is_correct=False),
        Choice(question=q6, choice_text="Hyper Transfer Markup Language", is_correct=False),
        Choice(question=q6, choice_text="Home Tool Markup Language", is_correct=False),
    ])

    q7 = Question.objects.create(
        course=web_course,
        lesson=lesson3,
        question_text="Which tag is used for the largest heading?",
        grade_point=10
    )
    Choice.objects.bulk_create([
        Choice(question=q7, choice_text="<heading>", is_correct=False),
        Choice(question=q7, choice_text="<h1>", is_correct=True),
        Choice(question=q7, choice_text="<h6>", is_correct=False),
        Choice(question=q7, choice_text="<head>", is_correct=False),
    ])

    q8 = Question.objects.create(
        course=web_course,
        lesson=lesson4,
        question_text="Which CSS property changes text color?",
        grade_point=10
    )
    Choice.objects.bulk_create([
        Choice(question=q8, choice_text="text-color", is_correct=False),
        Choice(question=q8, choice_text="color", is_correct=True),
        Choice(question=q8, choice_text="font-color", is_correct=False),
        Choice(question=q8, choice_text="foreground", is_correct=False),
    ])

    print("✅ Sample data created successfully!")
    print(f"📚 Created 2 courses with lessons and questions")
    print(f"   - {python_course.name}: 5 questions, 50 total points")
    print(f"   - {web_course.name}: 3 questions, 30 total points")


if __name__ == "__main__":
    create_sample_data()
