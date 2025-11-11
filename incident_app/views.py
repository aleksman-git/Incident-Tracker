from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import viewsets
from models import Incident
from serializers import IncidentSerializer

class IncidentView(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    http_method_names = ['get', 'post', 'put']

    @swagger_auto_schema(operation_description="incident_list")
    def list(self, request, *args, **kwargs):
        incident_list = list(Incident.objects.all().values())
        return Response(incident_list)

    @swagger_auto_schema(operation_description="incident_create")
    def create(self, request, *args, **kwargs):
        incident_add = IncidentSerializer(data=request.data)
        if incident_add.is_valid():
            incident_add.save()
            return Response({"message": "Incident CREATED"})
        else:
            return Response({"message": "Can't ADD"})

    @swagger_auto_schema(operation_description="incident_read")
    def retrieve(self, request, *args, **kwargs):
        incident_list_id = list(Incident.objects.filter(id=kwargs['pk']).values())
        return Response(incident_list_id)

    @swagger_auto_schema(operation_description="incident_update")
    def update(self, request, *args, **kwargs):
        incident_id = Incident.objects.get(id=kwargs['pk'])
        update_incident = IncidentSerializer(
            incident_id, data=request.data, partial=True)
        if update_incident.is_valid():
            update_incident.save()
            return Response({"message": "Incident UPDATED"})
        else:
            return Response({"message": "Can't UPDATE"})

