from rest_framework import serializers
from appapi.models import users
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class usersSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(allow_blank=False)
    last_name = serializers.CharField(allow_blank=False)
    username=serializers.CharField(required=True,validators=[UniqueValidator(queryset=users.objects.all())] )
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=users.objects.all())] )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    phone=serializers.RegexField("[0-9]{10}",required=True,validators=[UniqueValidator(queryset=users.objects.all())])
    birth_date=serializers.DateField(required=True)
    class Meta:
        model = users
        fields = ("first_name","last_name","username","email","password","phone","birth_date")
    #     extra_kwargs = {
    #     'first_name': {'required': True},
    #     'last_name': {'required': True}
    # }