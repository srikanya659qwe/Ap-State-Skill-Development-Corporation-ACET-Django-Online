from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Student
# Create your views here.
def hai(request):
	return HttpResponse("<h3>Hai guys welcome to django session</h3>")

def hello(request):
	return HttpResponse("<h2 style=background-color:red;color:blue;font-size:30px;font-style:italic>hai...guys</h2>")

def home(request,id):
	return HttpResponse("my rollnumber is :{}".format(id))

def sample(request):
	return render(request,'MyApp/sample.html')

def data(request,id,name):
	return render(request,'MyApp/data.html',{'i':id,'n':name})

def inline(request):
	return render(request,'MyApp/inline.html')

def internal(request):
	return render(request,'MyApp/internal.html')

def external(request):
	return render(request,'MyApp/external.html')

def boot(request):
	return render(request,'MyApp/boot.html')

def offline(request):
	return render(request,'MyApp/offline.html')

def register(request):
	if request.method=="POST":
		na=request.POST['name']
		roll=request.POST['rollnum']
		age=request.POST['age']
		mbl=request.POST['mbl']
		em=request.POST['email']
		add=request.POST['addr']

		Student.objects.create(name=na,rollnum=roll,age=age,mobile=mbl,
			email=em,address=add)
		return HttpResponse("your data record is inserted succssfully")
	return render(request,'MyApp/register.html')


def display(request):
	data=Student.objects.all()
	return render(request,'MyApp/display.html',{'data':data})