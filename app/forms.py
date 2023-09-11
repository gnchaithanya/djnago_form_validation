from django import forms
from django.core import validators
def check_for_s(value):
    if value[0].lower()=='s':
        raise forms.ValidationError('Start with s')
    
def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length should be greater than 5')
    
# def check_for_age(value):
#     if(value)<=20:
#         raise forms.ValidationError('Invalid age entered')

class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_s,check_for_len])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField(validators=[check_for_s])
    ReenterEmail=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    password=forms.CharField(max_length=100,widget=forms.PasswordInput,validators=[validators.RegexValidator('[a-zA-Z]+(\d+\W|\W+\d)')])


    def clean(self):
        s=self.cleaned_data['Semail']
        r=self.cleaned_data['ReenterEmail']
        age=self.cleaned_data['Sage']
        if (s!=r) or age<18:
            raise forms.ValidationError('Entered data are not matching')
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>5:
            raise forms.ValidationError('Invalid bot value')
    
        
    