from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
# Create your views here.
from .forms import BlogPostModelForm,StudentForm
from .models import BlogPost,Student
	# student = StudentForm()
	# return render(request,'blog/form.html',{'form':student})
@login_required()
def blog_post_list_view(request): 
	# list out object
	# could be search
	qs = BlogPost.objects.all().published()
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs = (qs | my_qs).distinct()
	template_name = 'blog/list.html'
	context = {"object_list":qs}
	return render(request, template_name, context)

# @login_required()
@staff_member_required()
def blog_post_create_view(request):
	# create object
	# ? use a form
	form = BlogPostModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		# obj = form.save(commit=False)
		# obj.title = form.cleaned_data.get('title') + " --APPENDING--"
		# obj.save()
		# obj =BlogPost.objects.create(**form.cleaned_data)
		form = BlogPostModelForm()

	template_name = 'blog/form.html'
	context = {
		"title": "Create Blog",
		"form":form
	}
	return render(request, template_name, context)


def blog_post_detail_view(request, slug):
	# 1 object -> detail view
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/detail.html'
	context = {"object":obj}

	return render(request, template_name, context)

@staff_member_required()
def blog_post_update_view(request, slug):
	# 1 object -> detail view
	# could be search
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=obj)
	if form.is_valid():
		form.save()
		# form = BlogPostModelForm()
	template_name = 'blog/form.html'
	context = {
		"form":form,
		"title": f"update {obj.title}",
	}
	return render(request, template_name, context)

@staff_member_required()
def blog_post_delete_view(request, slug):
	# 1 object -> detail view
	# could be search
	obj = get_object_or_404(BlogPost, slug=slug)
	if request.method == "POST":
		obj.delete()
		return redirect("/blog")
	template_name = 'blog/delete.html'
	context = {"object":obj}
	return render(request, template_name, context)

def get_student(request):

	student = StudentForm(request.POST or None)
	if student.is_valid():
		student.save()
		return redirect("/blog/show")


	return render(request,'blog/form.html',{'form':student})

def show(request):
	student = Student.objects.all()

	return render(request,'blog/show.html',{'data':student})

def delete_student(request,sid):
	s = Student.objects.filter(id=sid).delete()
	# s.delete()
	return redirect("/blog/show")

def edit_student(request,sid):
	obj = Student.objects.get(id=sid)
	s = StudentForm(request.POST or None, instance=obj)
	if s.is_valid():
	   s.save()
	   return redirect("/blog/show")

	return render(request, 'blog/form.html', {'form':s})

