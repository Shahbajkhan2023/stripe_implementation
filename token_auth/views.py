from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import RegistrationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token



class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        context = {"message": "Hello, world!"}
        return Response(context)
    

class RegistrationView(APIView):
    """Registration View"""

    def post(self, request, *args, **kwargs):
        """Handles post request logic"""
        registration_serializer = RegistrationSerializer(data=request.data)

        # Check if the data is valid
        if registration_serializer.is_valid():
            # Save the user and create the token
            user = registration_serializer.save()
            token = Token.objects.create(user=user)

            return Response(
                {
                    "user": {
                        "id": registration_serializer.data["id"],
                        "first_name": registration_serializer.data["first_name"],
                        "last_name": registration_serializer.data["last_name"],
                        "username": registration_serializer.data["username"],
                        "email": registration_serializer.data["email"],
                        "is_active": registration_serializer.data["is_active"],
                        "is_staff": registration_serializer.data["is_staff"],
                    },
                    "status": {
                        "message": "User created",
                        "code": f"{status.HTTP_200_OK} OK",
                    },
                    "token": token.key,
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "error": registration_serializer.errors,
                "status": f"{status.HTTP_400_BAD_REQUEST} Bad Request",
            },
            status=status.HTTP_400_BAD_REQUEST
        )