from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import User

class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user=kwargs.pop('user')
        super(ProfileForm,self).__init__(*args,**kwargs)
        if not user.is_superuser:
            self.fields['username'].help_text = None
            self.fields['username'].disabled=True
            self.fields['email'].disabled=True
            self.fields['special_user'].disabled=True
            self.fields['is_author'].disabled=True
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','special_user','is_author']

class SighUpForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']