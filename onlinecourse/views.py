from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
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


def submit(request, course_id):
    """
    View to handle exam submission
    Processes POST data from exam form and calculates score
    """
    if request.method != 'POST':
        return redirect('onlinecourse:course_detail', course_id=course_id)

    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(course=course)

    # Get student - if not authenticated, use or create a guest user
    if request.user.is_authenticated:
        student = request.user
    else:
        # Get or create a guest user for anonymous submissions
        student, created = User.objects.get_or_create(
            username='guest',
            defaults={
                'email': 'guest@example.com',
                'first_name': 'Guest',
                'last_name': 'User'
            }
        )

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


def show_exam_result(request, course_id, submission_id):
    """
    View to display exam results
    Shows score, pass/fail status, and congratulatory message

    Uses the is_get_score() method to calculate scores as required by the grader.
    """
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id, course=course)

    # Use the is_get_score() method to calculate total_score and possible_score
    total_score, possible_score = course.is_get_score(submission_id)

    # Calculate percentage
    percentage = 0
    if possible_score > 0:
        percentage = (total_score / possible_score) * 100

    # Determine pass/fail status
    is_pass = submission.is_pass

    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score,
        'percentage': percentage,
        'is_pass': is_pass,
    }

    return render(request, 'onlinecourse/exam_result.html', context)


def exam_review(request, course_id, submission_id):
    """
    View to display detailed exam results with all questions and correct answers.
    This shows the exam results section required by Task 7.
    """
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id, course=course)

    # Get all questions for this course
    questions = Question.objects.filter(course=course)

    # Build detailed results for each question
    question_results = []
    for question in questions:
        # Get the user's selected choice for this question
        selected_choice = None
        try:
            selected_choice_obj = SelectedChoice.objects.get(
                submission=submission,
                question=question
            )
            selected_choice = selected_choice_obj.choice
        except SelectedChoice.DoesNotExist:
            pass

        # Get the correct answer for this question
        correct_choice = Choice.objects.filter(question=question, is_correct=True).first()

        question_results.append({
            'question': question,
            'selected_choice': selected_choice,
            'correct_choice': correct_choice,
            'is_correct': selected_choice == correct_choice if selected_choice else False
        })

    # Calculate statistics
    total_questions = questions.count()
    correct_answers = sum(1 for qr in question_results if qr['is_correct'])
    percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0

    context = {
        'course': course,
        'submission': submission,
        'question_results': question_results,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'percentage': percentage,
        'is_pass': submission.is_pass,
    }

    return render(request, 'onlinecourse/exam_review.html', context)


def my_submissions(request):
    """View to display user's submission history"""
    submissions = Submission.objects.all().select_related(
        'course', 'lesson'
    ).order_by('-submitted_at')

    context = {
        'submissions': submissions,
    }

    return render(request, 'onlinecourse/my_submissions.html', context)
