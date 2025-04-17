from rest_framework import serializers
from . models import Contact

#normal serializer
# class ContactSerializer(serializers.Serializer):
#     name=serializers.CharField()
#     email=serializers.EmailField()
#     message=serializers.CharField()


#model serialzer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'