from rest_framework import serializers
from drfApp.models import Movie

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    rating=serializers.FloatField()
    description=serializers.CharField()

    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.rating=validated_data.get("rating",instance.rating)
        instance.description=validated_data.get("description",instance.description)
        instance.save()
        return instance