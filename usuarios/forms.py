from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text= 'Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text= 'Optional')
    email = forms.EmailField(max_length=250, help_text= 'Requerido')
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
        
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image',)
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'