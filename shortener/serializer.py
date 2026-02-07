from rest_framework import serializers
from .models import URL
from .utils import generate_short
from django.core.cache import cache

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'
        read_only_fields = ["shortenedURL", "visits", "created_at"]
    def create(self, validated_data):
        url = validated_data['originalURL']
        cached_code = cache.get(f"url:{url}")
        if cached_code:
            return URL.objects.get(originalURL = cached_code)
        if URL.objects.filter(originalURL = url).exists():
            return URL.objects.get(originalURL = url)
        validated_data['shortenedURL'] = generate_short(url)
        obj = URL.objects.create(**validated_data)

        cache.set(f"url:{url}",obj.shortenedURL, timeout=3600)
        cache.set(f"code:{obj.shortenedURL}", obj.originalURL, timeout=3600)
        return obj
    #0U0UeG