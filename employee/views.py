from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee

# Create your views here.

# View for creating a new employee
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})

# View for displaying all employees
def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})

# View for editing an employee's details
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})

# View for updating an employee's details
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})

# View for deleting an employee
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
