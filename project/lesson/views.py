from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson

def home(request):
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    return render(request, 'home.html', {'courses': courses, 'lessons': lessons})

def lesson_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    return render(request, 'lesson_list.html', {'course': course, 'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})
