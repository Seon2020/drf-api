from rest_framework import generics
from .serializer import HitsSerializer
from .models import Hits

class HitsList(generics.ListCreateAPIView):
    queryset = Hits.objects.all()
    serializer_class = HitsSerializer

class HitsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hits.objects.all()
    serializer_class = HitsSerializer

