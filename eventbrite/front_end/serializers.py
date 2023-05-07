from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models

#A serializer file and class to complex data into native python datatypes
class CreateUserForm(serializers.ModelSerializer):

    class Meta:
        fields = ('username','email','password')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Display Name'
        self.fields['email'].label='Email Address'

