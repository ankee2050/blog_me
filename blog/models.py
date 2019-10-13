from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Q
# Create your models here.

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		# self.get_queryset() is equvalent to this BlogPost.objects
		return self.filter(publish_date__lte=now)
		# return self.get_queryset().filter(publish_date__lte=now)

	def search(self, query):
		lookup = (	
					Q(title__icontains=query) |
				  	Q(content__icontains=query) |
				  	Q(slug__icontains=query) |
				  	Q(user__first_name__icontains=query) |
				  	Q(user__last_name__icontains=query) |
				  	Q(user__username__icontains=query)
				 )
		return self.filter(lookup)

class BlogPostManager(models.Manager):
	# def published(self):
		# now = timezone.now()
		# self.get_queryset() is equvalent to this BlogPost.objects
		# return self.get_queryset().filter(publish_date__lte=now)
	def get_queryset(self):
		return BlogPostQuerySet(self.model, using=self._db)

	def published(self):
		return self.get_queryset().published()

	def search(self, query = None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().published().search(query)


class BlogPost(models.Model):
	
	user = models.ForeignKey(User, default=1, null=True, on_delete = models.SET_NULL)
	# image = models.FileField(upload_to='images/', null=True, blank=True)
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	content = models.TextField(null=True, blank=True)
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = BlogPostManager()

	class Meta:
		ordering = ['-publish_date','-updated','-timestamp']

	def get_absolute_url(self):
		return f"/blog/{self.slug}"
	def get_update_url(self):
		return f"{self.get_absolute_url()}/update"
	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"

class another_blog_post(models.Model):
	title = models.TextField()
	content = models.TextField(null=True, blank= True)

class Student(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	address = models.CharField(max_length=200)
class Person(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.IntegerField()

	class Meta:
		db_table = 'person'


class Employee(models.Model):
	dep_id = models.IntegerField()
	employee_name = models.CharField(max_length=20)
	salary = models.IntegerField() 