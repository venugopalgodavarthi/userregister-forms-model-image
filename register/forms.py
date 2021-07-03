from django import forms
from django.forms.widgets import NumberInput

class USERFORM(forms.Form):
    firstname=forms.CharField(widget=forms.TextInput)
    lastname=forms.CharField(widget=forms.TextInput)
    email=forms.EmailField()
    phone=forms.IntegerField(widget=forms.TextInput)
    dob=forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    cho=(("Male","MALE"),("Female","FEMALE"))
    gender=forms.ChoiceField(choices=cho)
    address=forms.CharField(widget=forms.Textarea(attrs={'row':3}))
    img=forms.ImageField()