from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PredictionSerializer
from .models import Prediction


class PredictionListAPI(APIView):

    def get(self, request):

        predictions = Prediction.objects.order_by("-created_at")

        serializer = PredictionSerializer(predictions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)