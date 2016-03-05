from django.shortcuts import render

from decisions.models import Case, Organization, Action
from api.serializers import CaseSerializer, OrganizationSerializer, ActionSerializer
from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework import exceptions, filters, mixins, serializers, viewsets
from rest_framework import viewsets

# from rest_framework.response import Response
# from rest_framework import status


# class CaseList(APIView):
class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all cases
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset
        else:
            return self.queryset.filter(public=True)


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all Organizations
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all Actions
    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
