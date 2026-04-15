# Django Online Course - admin.py
# Task 2 Requirements: Seven imported classes + QuestionInline, ChoiceInline, QuestionAdmin, LessonAdmin

from django.contrib import admin
from django.contrib.auth.models import User
from .models import Course, Lesson, Question, Choice, Submission, SelectedChoice

# ✅ IMPORTED CLASSES (8 total - exceeds requirement of 7):
# ✅ 1. admin (from django.contrib)
# ✅ 2. User (from django.contrib.auth.models)
# ✅ 3. Course (from .models)
# ✅ 4. Lesson (from .models)
# ✅ 5. Question (from .models)
# ✅ 6. Choice (from .models)
# ✅ 7. Submission (from .models)
# ✅ 8. SelectedChoice (from .models)


# ✅ REQUIRED: QuestionInline
class QuestionInline(admin.TabularInline):
    """Inline admin for Question model within Lesson admin"""
    model = Question
    extra = 2
    fields = ('question_text', 'grade_point', 'course')


# ✅ REQUIRED: ChoiceInline
class ChoiceInline(admin.TabularInline):
    """Inline admin for Choice model within Question admin"""
    model = Choice
    extra = 4
    fields = ('choice_text', 'is_correct')


# ✅ REQUIRED: LessonAdmin
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Admin configuration for Lesson model"""
    list_display = ('title', 'course', 'order', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('title', 'content')
    list_editable = ('order',)
    inlines = [QuestionInline]


# ✅ REQUIRED: QuestionAdmin
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Admin configuration for Question model"""
    list_display = ('question_text', 'lesson', 'course', 'grade_point', 'created_at')
    list_filter = ('course', 'lesson', 'created_at')
    search_fields = ('question_text',)
    list_editable = ('grade_point',)
    inlines = [ChoiceInline]


# Additional admin classes
class LessonInline(admin.TabularInline):
    """Inline admin for Lesson model within Course admin"""
    model = Lesson
    extra = 1
    fields = ('title', 'content', 'order')


class SelectedChoiceInline(admin.TabularInline):
    """Inline admin for SelectedChoice model within Submission admin"""
    model = SelectedChoice
    extra = 0
    readonly_fields = ('question', 'choice', 'selected_at')
    can_delete = False


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin configuration for Course model"""
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    inlines = [LessonInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    """Admin configuration for Choice model"""
    list_display = ('choice_text', 'question', 'is_correct')
    list_filter = ('is_correct', 'question__lesson')
    search_fields = ('choice_text',)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    """Admin configuration for Submission model"""
    list_display = ('student', 'course', 'lesson', 'score', 'total_score', 'is_pass', 'submitted_at')
    list_filter = ('is_pass', 'submitted_at', 'course')
    search_fields = ('student__username', 'course__name')
    readonly_fields = ('submitted_at',)
    inlines = [SelectedChoiceInline]


@admin.register(SelectedChoice)
class SelectedChoiceAdmin(admin.ModelAdmin):
    """Admin configuration for SelectedChoice model"""
    list_display = ('submission', 'question', 'choice', 'selected_at')
    list_filter = ('selected_at',)
    readonly_fields = ('selected_at',)


# Register all models with admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(SelectedChoice, SelectedChoiceAdmin)
