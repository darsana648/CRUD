from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


def create(request):
    if request.method == 'POST':
        cr = StudentForm(request.POST)
        if cr.is_valid():
            cr.save()
            return redirect('create')
    else:
        cr = StudentForm()

    data = Student.objects.all()
    return render(request, 'home.html', {'cr': cr, 'data': data})


def edit(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return redirect('create')  # Redirect if student doesn't exist

    if request.method == 'POST':
        fm = StudentForm(request.POST, instance=student)  # Bind the form with data for editing
        if fm.is_valid():
            fm.save()
            return redirect('create')
    else:
        fm = StudentForm(instance=student)  # Display the form with current data pre-filled

    return render(request, 'edit.html', {'fm': fm, 'student': student})


def delete(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
    except Student.DoesNotExist:
        pass  # If the student doesn't exist, do nothing (or handle differently)

    return redirect('create')
