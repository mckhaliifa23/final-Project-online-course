from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    """Model representing an online course"""
    name = models.CharField(max_length=200, help_text="Enter course name")
    description = models.TextField(blank=True, help_text="Enter course description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def is_get_score(self, submission_id):
        """
        Calculate and return total_score and possible_score for a submission.
        This method is required by the automated grader.
        """
        try:
            submission = Submission.objects.get(id=submission_id, course=self)
            total_score = submission.score
            possible_score = submission.total_score
            return total_score, possible_score
        except Submission.DoesNotExist:
            return 0, 0


class Lesson(models.Model):
    """Model representing a lesson within a course"""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        help_text="Select the course this lesson belongs to"
    )
    title = models.CharField(max_length=200, help_text="Enter lesson title")
    content = models.TextField(help_text="Enter lesson content")
    order = models.PositiveIntegerField(default=0, help_text="Order of lesson in course")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.name} - {self.title}"


class Question(models.Model):
    """Model representing an exam question"""
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='questions',
        help_text="Select the lesson this question belongs to"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='questions',
        help_text="Select the course this question belongs to"
    )
    question_text = models.CharField(
        max_length=500,
        help_text="Enter the question text"
    )
    grade_point = models.PositiveIntegerField(
        default=1,
        help_text="Points awarded for correct answer"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['lesson', 'id']

    def __str__(self):
        return self.question_text[:100]


class Choice(models.Model):
    """Model representing a choice for a multiple choice question"""
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices',
        help_text="Select the question this choice belongs to"
    )
    choice_text = models.CharField(
        max_length=300,
        help_text="Enter the choice text"
    )
    is_correct = models.BooleanField(
        default=False,
        help_text="Check if this is the correct answer"
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    """Model representing a student's exam submission"""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='submissions',
        help_text="Select the course for this submission"
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='submissions',
        help_text="Select the student who submitted"
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='submissions',
        help_text="Select the lesson for this submission"
    )
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0,
        help_text="Score achieved"
    )
    total_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0,
        help_text="Total possible score"
    )
    is_pass = models.BooleanField(
        default=False,
        help_text="Whether the submission is passing"
    )
    submitted_at = models.DateTimeField(auto_now_add=True, help_text="Submission timestamp")

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.student.username} - {self.course.name} - Score: {self.score}/{self.total_score}"


class SelectedChoice(models.Model):
    """Model representing selected choices in a submission"""
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name='selected_choices',
        help_text="Select the submission this choice belongs to"
    )
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        related_name='selected_choices',
        help_text="Select the choice that was selected"
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='selected_choices',
        help_text="Select the question this choice answers"
    )
    selected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('submission', 'question')
        ordering = ['id']

    def __str__(self):
        return f"{self.submission} - {self.choice.choice_text[:50]}"


class Instructor(models.Model):
    """Model representing an instructor who creates and manages courses"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='instructor_profile',
        help_text="Link to user account"
    )
    bio = models.TextField(blank=True, help_text="Instructor biography")
    expertise = models.CharField(max_length=200, blank=True, help_text="Area of expertise")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['user__username']
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}"


class Learner(models.Model):
    """Model representing a learner/student who takes courses"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='learner_profile',
        help_text="Link to user account"
    )
    bio = models.TextField(blank=True, help_text="Student biography")
    interests = models.CharField(max_length=200, blank=True, help_text="Areas of interest")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['user__username']
        verbose_name = 'Learner'
        verbose_name_plural = 'Learners'

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}"
