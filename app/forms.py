from django import forms
from app.models import *

class Topicforms(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class Webpageforms(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #fields=['tname','url']
        #exclude=['email','name']
        #labels={'tname':'TN','name':'candidate'}
        #widgets={'email':forms.PasswordInput}
class Accessrecordforms(forms.ModelForm):
    class Meta():
        model=Accessrecord
        fields='__all__'

     