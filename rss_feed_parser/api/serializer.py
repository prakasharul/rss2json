from rest_framework import serializers

from . models import RSS


class rssSerializer(serializers.ModelSerializer):
    # url = serializers.URLField()
    # sort = serializers.IntegerField()

    class Meta:
        model = RSS
        fields = "__all__"

