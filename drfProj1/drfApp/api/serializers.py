from rest_framework import serializers
from drfApp.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"
        #exclude=["rating"]


    def validate_rating(self,value):
        if value>10:
            raise serializers.ValidationError("Max rating can be 10")
        return value
    
    def validate(self, data):
        if data['name']==data['description']:
            raise serializers.ValidationError("Description cannot be same as name")
        return data



# #using validators=[] core argument
# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError("Name too short")

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     rating=serializers.FloatField()
#     description=serializers.CharField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get("name",instance.name)
#         instance.rating=validated_data.get("rating",instance.rating)
#         instance.description=validated_data.get("description",instance.description)
#         instance.save()
#         return instance
    
#     #field level validation
#     def validate_rating(self,value):
#         if value>10:
#             raise serializers.ValidationError("Max rating can be 10")
#         return value
    
#     #object level validation
#     def validate(self, data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError("Description cannot be same as name")
#         return data
