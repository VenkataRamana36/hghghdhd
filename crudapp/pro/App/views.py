from django.shortcuts import render, redirect

from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print("save")
            form.save()
            return redirect('/show')
        else:
            form = EmployeeForm()
        return render(request, '/show.html', {'form': form})
    else:
        form = EmployeeForm(request.GET)
        return render(request, 'index.html', {'form': form})


def show(request):
    employee = Employee.objects.all()
    return render(request, 'show.html', {'employee': employee})


def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')


def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    if form.is_valid():
        form.save()
        return redirect("templates/show.html")
    return redirect("templates/show.html")
