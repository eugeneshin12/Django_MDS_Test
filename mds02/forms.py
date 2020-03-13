from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import PJT, MR, EQT, PDS, MDS

class PJTForm(ModelForm):
    class Meta:
        model = PJT
        fields = ('P_No', 'P_Name', 'P_Country', 'P_Client')

class MRForm(ModelForm):
    class Meta:
        model = MR
        fields = ('P_No', 'M_No', 'M_Name')

class EQTForm(ModelForm):
    class Meta:
        model = EQT
        fields = ('P_No', 'M_No', 'E_No', 'E_Name')


class MDSForm(ModelForm):
    class Meta:
        model = MDS
        fields = ('E_No','MD_Type','MD_Seal','MD_Matl')


class PDSForm(ModelForm):
    class Meta:
        model = PDS
        fields = ('E_No','PD_Fluid','PD_Head','PD_Dens','PD_NPSH')


#회원가입 클래스
class SignupForm(ModelForm):
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())

    field_order = ['username','password','password_check','last_name','first_name','email']

    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = {'username','password','last_name','first_name','email'}

#로그인 클래스
class SigninForm(ModelForm):
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = {'username', 'password'}

