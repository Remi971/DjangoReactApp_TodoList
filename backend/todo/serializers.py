from rest_framework import serializers
from .models import Todo

# Serializers convert model instances to JSON so the frontend can work with the received data.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

# The code specifies the model to work with and the field to be converted to JSON