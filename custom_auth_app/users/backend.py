from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class EmailOrPhoneModelBackend(ModelBackend):
   
    def authenticate(self, request, email=None, password=None, **kwargs):

        user_model = get_user_model()

        if email is None:
            email = kwargs.get(user_model.USERNAME_FIELD)

        
        users = user_model._default_manager.filter(
            Q(**{user_model.USERNAME_FIELD: email}) | Q(phone__iexact=email)
        )

        for user in users:
            if user.check_password(password):
                return user
        if not users:
            user_model().set_password(password)
'''
class EmailOrPhoneModeBackend():

    def authenticate(self, request, email_or_phone=None, password=None):
        try:
             user = get_user_model().objects.get(
                 Q(email=email_or_phone) | Q(phone=email_or_phone)
             )
             pwd_valid = user.check_password(password)
             if pwd_valid:            
                 return user
             return None
        except get_user_model().DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
            '''
"""
Authentication backend which allows users to authenticate using either their
username or email address

Source: https://stackoverflow.com/a/35836674/59984
"""