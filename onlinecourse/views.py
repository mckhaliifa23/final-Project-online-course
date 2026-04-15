from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import (
    Course,
    Lesson,
    Question,
    Choice,
    Submission,
    SelectedChoice
)


def course_list(request):
    """View to display all available courses"""
    courses = Course.objects.all()
    return render(request, 'onlinecourse/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    """View to display course details including lessons and exam form"""
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    questions = Question.objects.filter(course=course)

    context = {
        'course': course,
        'lessons': lessons,
        'questions': questions,
    }
    return render(request, 'onlinecourse/course_details_bootstrap.html', context)


@login_required
def submit(request, course_id):
    """
    View to handle exam submission
    Processes POST data from exam form and calculates score
    """
    if request.method != 'POST':
        return redirect('onlinecourse:course_detail', course_id=course_id)

    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(course=course)
    student = request.user

    # Get the first lesson (or create logic to get specific lesson)
    lesson = course.lessons.first()
    if not lesson:
        messages.error(request, 'No lessons found for this course.')
        return redirect('onlinecourse:course_detail', course_id=course_id)

    # Calculate total score
    total_score = questions.aggregate(total=Sum('grade_point'))['total'] or 0

    # Calculate earned score
    earned_score = 0
    selected_choices_data = []

    for question in questions:
        choice_id = request.POST.get(f'question_{question.id}')
        if choice_id:
            try:
                choice = Choice.objects.get(pk=choice_id, question=question)
                if choice.is_correct:
                    earned_score += question.grade_point
                selected_choices_data.append((question, choice))
            except Choice.DoesNotExist:
                # Invalid choice, skip
                pass

    # Determine passing (70% threshold)
    passing_threshold = 0.7
    is_pass = (earned_score / total_score >= passing_threshold) if total_score > 0 else False

    # Create submission
    submission = Submission.objects.create(
        course=course,
        student=student,
        lesson=lesson,
        score=earned_score,
        total_score=total_score,
        is_pass=is_pass
    )

    # Create selected choice records
    for question, choice in selected_choices_data:
        SelectedChoice.objects.create(
            submission=submission,
            question=question,
            choice=choice
        )

    return redirect('onlinecourse:show_exam_result', course_id=course_id, submission_id=submission.id)


@login_required
def show_exam_result(request, course_id, submission_id):
    """
    View to display exam results
    Shows score, pass/fail status, and congratulatory message
    """
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id, course=course)

    # Calculate percentage
    percentage = 0
    if submission.total_score > 0:
        percentage = (submission.score / submission.total_score) * 100

    context = {
        'course': course,
        'submission': submission,
        'percentage': percentage,
        'is_pass': submission.is_pass,
    }

    return render(request, 'onlinecourse/exam_result.html', context)


@login_required
def my_submissions(request):
    """View to display user's submission history"""
    submissions = Submission.objects.filter(student=request.user).select_related(
        'course', 'lesson'
    ).order_by('-submitted_at')

    context = {
        'submissions': submissions,
    }

    return render(request, 'onlinecourse/my_submissions.html', context)
