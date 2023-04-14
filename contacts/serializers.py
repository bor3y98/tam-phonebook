from rest_framework import serializers
from .models import Contact, ContactNumber


class ContactNumberSerializer(serializers.Serializer):
    number = serializers.CharField()
    type = serializers.CharField()


class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    company = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    contactnumbers = ContactNumberSerializer(many=True, required=True)

    def create(self, validated_data):
        numbers_data = validated_data.pop('contactnumbers')
        print(numbers_data)
        print(validated_data)
        contact = Contact.objects.create(**validated_data)
        for number_data in numbers_data:
            ContactNumber.objects.create(contact=contact, **number_data)
        return contact
