# Imports the forms module from the Django library
from django import forms

# Creates a form class for the user comments
class CommentForm(forms.Form):
	comment = forms.CharField()