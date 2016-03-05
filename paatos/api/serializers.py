from rest_framework import serializers
from decisions.models import Case


class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = ('id', 'iri', 'title', 'description', )
