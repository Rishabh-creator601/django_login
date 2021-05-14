


from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
# cd web && python manage.py runserver 
def home(request):
	if request.user.is_anonymous:
		return redirect("/login")
	return render(request,'content.html')
	
def loginUser(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		password = request.POST.get('password')
		user = authenticate(username=name, password=password)
		if user is not None:	
		 	login(request,user)
		 	return redirect("/")
		  		
    		# A backend authenticated the credentials
		else:
			return render(request,'login.html')
  		  # No backend authenticated the credentials
	
	return render(request,'login.html')
	
	
def logoutUser(request):
	logout(request)
	return redirect("/login")
