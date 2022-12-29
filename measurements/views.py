from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from measurements.models import Project, Measurement
from measurements.serializers import ProjectSerializer, MeasurementSerializer
from rest_framework.views import APIView

# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         projects = Project.objects.all()
#         ser = ProjectSerializer(projects, many=True)
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response({'status' : 'ok'})


# class ProjectViewSet(APIView):
#     def get(self, request):
#         projects = Project.objects.all()
#         ser = ProjectSerializer(projects, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response({'status' : 'ok'})

class ProjectViewSet(ListAPIView):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def post(self, requst):
        return Response({'status': 'ok'})

class OneProjectViewSet(RetrieveAPIView):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(ListAPIView):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

