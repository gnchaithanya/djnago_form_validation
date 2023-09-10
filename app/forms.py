from django import forms

def check_for_s(value):
    if value[0].lower()=='s':
        raise forms.ValidationError('Start with s')
    
def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length should be greater than 5')
    
def check_for_age(value):
    if(value)<=20:
        raise forms.ValidationError('Invalid age entered')

class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_s,check_for_len])
    Sage=forms.IntegerField(validators=[check_for_age])
    Sid=forms.IntegerField()
    Semail=forms.EmailField(validators=[check_for_s])
