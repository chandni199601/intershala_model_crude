from django.shortcuts import render
from  webApp.models import Emp

# Create your views here.
def Emp_View(request):
    EmpList=Emp.objects.all()
    my_Dict={'elist':EmpList}
    return render(request,'myApp/welcome.html',my_Dict)

