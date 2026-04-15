#!/usr/bin/env python3
"""
Script to create a test user for the Online Course Application
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinecourse_project.settings')
django.setup()

from django.contrib.auth.models import User


def create_test_user():
    """Create a test user for taking exams"""

    # Create test student
    if not User.objects.filter(username='student').exists():
        student = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='student123',
            first_name='Test',
            last_name='Student'
        )
        print("✅ Test student created successfully!")
    else:
        print("ℹ️ Test student already exists")

    print("\n📝 Login Credentials:")
    print("   Admin: username='admin', password='admin123'")
    print("   Student: username='student', password='student123'")
    print("\n🌐 Application URLs:")
    print("   Home: http://localhost:8000/")
    print("   Admin: http://localhost:8000/admin/")
    print("   Python Course: http://localhost:8000/course/1/")
    print("   Web Course: http://localhost:8000/course/2/")


if __name__ == "__main__":
    create_test_user()
