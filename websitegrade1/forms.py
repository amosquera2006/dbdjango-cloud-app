from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fullname', 'test']



class FormId(forms.ModelForm):  # class created for manage info
    class Meta:
        model = Member
        fields = ['id']

class FormId(forms.Form):
    field = forms.IntegerField()






