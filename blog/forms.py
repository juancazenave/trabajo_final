from django import forms

class PostFormulario(forms.Form):

    title = forms.CharField()
    intro = forms.CharField()
    body = forms.CharField()
