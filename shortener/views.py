from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import URL
from .serializer import URLSerializer
from django.shortcuts import redirect
from django.core.cache import cache
class URLView(APIView):
    def post(self,request):
        serializer = URLSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        resp = serializer.data
        return Response({"originalURL": resp["originalURL"], "shortenedURL":resp["shortenedURL"]}, status=status.HTTP_201_CREATED)
    def get(self,request, shortcode):
        long_url = cache.get(f"{shortcode}")
        if not long_url:
            try:
                url = URL.objects.get(shortenedURL = shortcode)
            except URL.DoesNotExist:
                return Response({"error" : "URl does not exist"}, status=status.HTTP_404_NOT_FOUND)
            url.visits += 1
            url.save()
            cache.set(f"code:{url.shortenedURL}",long_url, timeout=3600)
        return redirect(url.originalURL)

class TopURLView(APIView):
    def get(self, request):
        url = URL.objects.all().order_by('-visits')[:10]
        serializer = URLSerializer(url, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
