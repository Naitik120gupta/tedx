from rest_framework import serializers
from .models import ContactMessage

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
