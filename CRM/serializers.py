from rest_framework import serializers

from .models import Client, User, Contract, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'role',)
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def validate_name(self, value):
        if Client.objects.filter(name=value).exists():
            raise serializers.ValidationError('Le nom du projet existe déjà')
        return value


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        return Event.objects.create(**validated_data)
