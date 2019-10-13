from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea)

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		if email.endswith(".edu"):
			raise forms.ValidationError("Please do not use .edu")
		return email

class SignupForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	email = forms.EmailField(max_length=120, help_text='Required. Inform a valid email.')
	class Meta:
		model = User
		# exclude = ()
		fields = ('username','first_name','last_name','email','password1','password2', )