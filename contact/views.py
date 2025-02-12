from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import ContactMessage
from .serializers import ContactFormSerializer

@api_view(['POST'])
def submit_contact_form(request):
    serializer = ContactFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Form submitted successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
