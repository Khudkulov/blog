from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    user = request.user
    Token.objects.get(user=user).delete()
    response = {
        "success": True,
        "message": "Successfully logged out"
    }
    return Response(response, status=status.HTTP_200_OK)
