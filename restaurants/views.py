from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def default(request):
	context = {"msg": "Hello World!",}
	#return HttpResponse("<h1>{{msg}}</h1>")
	return render(request,'default.html',context)