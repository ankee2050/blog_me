from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm 


def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = SignupForm()
	return render(request, 'signup.html', {'form':form})


def logout_app(request):
	logout(request)
	return redirect('/')

def login_app(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = AuthenticationForm(request=request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('/')
			else:
				return redirect('/login')
	else:
		form = AuthenticationForm()
		return render(request, 'login.html', {'form':form})


def home_page(request):
	my_title = "Blogs"
	qs = BlogPost.objects.all()[:4]
	# doc = "<h1>{title}</h1>".format(title=my_title)
	return render(request, "home.html", {"title":my_title, "blog_list":qs})

def about(request):
	return render(request,"hello_world.html",{"title":"About"})
	# return HttpResponse("<h1>I am a New Developer not introduced by the world yet!</h1>")

def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {
		'title': 'Contact',
		'form': form
	}
	return render(request, "form.html", context)
	# return HttpResponse("<h1>No Contact</h1>")

def example_page(request):
	context	 = {"title":"Example"}
	template_name = "hello_world.txt"
	template_obj = get_template(template_name)
	# return HttpResponse(template_obj.render(context))
	return render(request, "hello_world.html", {"title":template_obj.render(context)})

def example_page2(request):
	context	 = {"title":"Example"}
	template_name = "hello_world.html"
	template_obj = get_template(template_name)
	return HttpResponse(template_obj.render(context))