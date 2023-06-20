from django import forms
from .models import Profile, Question, Answer
from django.contrib.auth.models import User
import os


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=1 ,widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_check = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'password_check', 'avatar']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check')
        if password and password_check and password != password_check:
            raise forms.ValidationError("Passwords don't match")    
        return cleaned_data



    def save(self, commit=True):
        self.cleaned_data.pop('password_check')
        user = User.objects.create_user(
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password'],
            email = self.cleaned_data['email'],
        )
        profile = super(RegistrationForm, self).save(commit=False)
        profile.user = user

        if commit:
            user.save()
            profile.save()
        return profile
    

class SettingsForm(forms.ModelForm):
   #avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email']


class AskForm(forms.ModelForm):
    tag_list = forms.CharField(required=False)
    title = forms.CharField(widget=forms.TextInput(), required=True)
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": "3"}))

    class Meta:
        model = Question
        fields = ['title', 'text', 'tag_list']


class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": "3"}), label="Question answer", required=True)

    class Meta:
        model = Answer
        fields = ['text']

