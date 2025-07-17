from rest_framework import serializers
from api.models import Company


#create serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model:Company
        fields= "__all__"