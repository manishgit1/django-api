from rest_framework import serializers 
from django.contrib.auth import  authenticate
from .models import AppUser, Transaction, BankAccount



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    account_number = serializers.CharField(write_only=True)
    class Meta:
        model =  AppUser
        fields = ['email', 'name', 'password', 'phone_number', 'account_number']
    
    def validate_account_number(self, value):
        try:
            bank_account = BankAccount.objects.get(account_number=value)

        except BankAccount.DoesNotExist:
            raise serializers.ValidationError('Invalid account number')    


    def create(self, validated_data):

        user = AppUser.objects.create_user(email=validated_data['email'],
                                         password=validated_data['password'],
                                         name=validated_data['name'],
                                         phone_number=validated_data['phone_number'],
                                         account_number = validated_data['account_number'],)   


        return user 
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, validated_data):
        user = authenticate(username=validated_data['email'], password=validated_data['password'])
        if not user:
            raise serializers.ValidationError('User not found')
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('email', 'name', 'phone_number', 'account_number')


class TransactionSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(source='sender.name')
    receiver = serializers.StringRelatedField(source='receiver.name')
    sender_account_number  = serializers.StringRelatedField(source='sender.account_number')
    receiver_account_number = serializers.StringRelatedField(source='receiver.account_number')

    class Meta:
        model = Transaction
        fields= ['sender','sender_account_number', 'receiver', 'receiver_account_number','amount', 'timestamp']