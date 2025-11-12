from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Incident
from .serializers import IncidentSerializer


class IncidentView(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_description="Получить список инцидентов с фильтрацией по статусу",
        manual_parameters=[
            openapi.Parameter(
                'status',
                openapi.IN_QUERY,
                description="Фильтр по статусу",
                type=openapi.TYPE_STRING,
                enum=['new', 'in_progress', 'resolved', 'closed']
            )
        ]
    )
    def list(self, request):
        # Получить список инцидентов (с фильтром по статусу)
        status_filter = request.query_params.get('status')

        if status_filter:
            incidents = Incident.objects.filter(status=status_filter)
        else:
            incidents = Incident.objects.all()

        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать инцидент",
        request_body=IncidentSerializer
    )
    def create(self, request):
        # Создать инцидент
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            incident = serializer.save()
            return Response(
                {
                    "message": "Incident CREATED",
                    "incident_id": incident.incident_id
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "message": "Can't ADD",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    @swagger_auto_schema(
        operation_description="Обновить статус инцидента",
        methods=['patch'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'status': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=['new', 'in_progress', 'resolved', 'closed']
                )
            }
        )
    )
    @action(detail=True, methods=['patch'], url_path='update-status')
    def update_status(self, request, pk=None):
        # Обновить статус инцидента по id
        incident = get_object_or_404(Incident, pk=pk)

        # Обновляем только статус
        new_status = request.data.get('status')
        if not new_status:
            return Response(
                {"message": "Status field is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        incident.status = new_status
        incident.save()

        serializer = IncidentSerializer(incident)
        return Response(
            {
                "message": "Incident STATUS UPDATED",
                "data": serializer.data
            }
        )

