from rest_framework import serializers
from decisions.models import Case, Organization, Action


class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = ('id', 'iri', 'title', 'description', )


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'abstract', )


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ('id', 'title', 'case')
