from django import forms


class HelpForm(forms.Form):
	name = forms.CharField(max_length=30)
	title = forms.CharField(max_length=50)
	story = forms.CharField(widget=forms.Textarea)