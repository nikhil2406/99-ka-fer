from django import forms
from rango.models import UserPersonal, UserFinancial

class UserPersonalForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='enter your name')
    age = forms.IntegerField(initial=0, help_text='enter your age')
    phone = forms.CharField(max_length=10, help_text='enter your contact number')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = UserPersonal
        fields = ('name', 'age', 'phone', 'views')

class UserFinancialForm(forms.ModelForm):
    salary = forms.IntegerField(initial=0, help_text='enter your salary')
    otherIncome = forms.IntegerField(initial=0, help_text='enter your other income')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = UserFinancial
        fields = ('salary', 'otherIncome', 'views')



