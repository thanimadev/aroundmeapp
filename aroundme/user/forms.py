from django import forms
from .models import *

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "gender":forms.Select(attrs={"class":"form-control",}),

            "phone":forms.NumberInput(attrs={"class":"form-control",}),
            "status":forms.TextInput(attrs={"class":"form-control",}),
        }

class PForm(forms.Form):
    old_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"placeholder":"enter old password","class":"form-control"}))
    new_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"placeholder":"enter new password","class":"form-control"}))
    confirm_new_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"placeholder":"confirm new password","class":"form-control"}))

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts 
        fields=["image","caption"]
        widgets={
            "image":forms.FileInput(),
            "caption":forms.TextInput(attrs={"class":"form-control",}),
            }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comment"]
        widgets={
            
            "comment":forms.TextInput(attrs={"class":"form-control","placeholder":"add your comment"}),
            }


