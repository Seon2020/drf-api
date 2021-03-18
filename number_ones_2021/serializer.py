from rest_framework import serializers
from .models import Hits

class HitsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'album', 'description', 'artists', 'added_by', 'added_on')
        model = Hits

    
