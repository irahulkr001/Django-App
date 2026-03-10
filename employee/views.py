from django.shortcuts import render, redirect
from django.views import View
from employee.models import Employee
from employee.forms import EmployeeForm
# from Library.books.models import Book


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,'index.html')

class Addemployee(View):
    def get(self, request):
        form_instance = EmployeeForm()
        context = {'forms':form_instance}
        return render(request,'addemployee.html',context)
    def post(self,request):
        print(request.POST) #normal data
        print(request.FILES) #file data
        form_instance = EmployeeForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return render(request,'addemployee.html')

class ViewEmployee(View):
    def get(self, request):
        e = Employee.objects.all()
        context = {'employee': e}
        return render(request,'viewemployee.html',context)

