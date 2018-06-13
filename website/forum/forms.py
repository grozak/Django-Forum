from django import forms

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)