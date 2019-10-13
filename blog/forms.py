from django import forms
from .models import BlogPost,Student

# class BlogPostForm(forms.Form):
# 	title = forms.CharField()
# 	slug = forms.SlugField()
# 	content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ['title','image','slug','content','publish_date']

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		qs = BlogPost.objects.filter(title__exact=title)
		if self.instance is not None:
			qs = qs.exclude(pk=self.instance.pk) # id = instance.id
		if qs.exists():
			raise forms.ValidationError("This title is already been used before.")
		return title

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ['name','age','address']
