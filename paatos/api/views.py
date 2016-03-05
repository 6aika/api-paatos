from django.shortcuts import render

from decisions.models import Case
from api.serializers import CaseSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CaseList(APIView):
    """
    List all cases
    """

    def get(self, request, format=None):
        case = Case.objects.all()
        serializer = CaseSerializer(case, many=True)
        return Response(serializer.data)
