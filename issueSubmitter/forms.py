from django import forms

class NameForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Short description of the problem'}))
    files = forms.CharField(label='Files involved', widget=forms.TextInput(attrs={'placeholder': '(e.g CSV files)'}), max_length=100)
    tags = forms.CharField(label='Tags', widget=forms.TextInput(attrs={'placeholder': '#Tags'}), max_length=100)
