from django import forms

from app.models import *

class UserForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['questions']
class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['answers']