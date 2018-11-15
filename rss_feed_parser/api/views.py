from django.shortcuts import render
from rest_framework.views import  APIView, status
from rest_framework import  viewsets
from rest_framework.response import Response

from . serializer import rssSerializer
from . models import RSS

import feedparser


def feedparse(url):
    parsed_data = feedparser.parse(url)
    return parsed_data


class rssApi(APIView):

    def get(self, request):
        data = [{"url":"http:","sort":10},{"url":"http:","sort":10},{"url":"http:","sort":10},{"url":"http:","sort":10}]
        results = rssSerializer(data, many=True).data
        return Response(results)

    def post(self, request):
        serializer = rssSerializer(data=self.request.data)
        if serializer.is_valid():
            url = serializer.validated_data["url"]
            sort = serializer.validated_data["sort"]

            feeds = feedparse(url)
            return Response({'feeds':feeds}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)


class RssApi(viewsets.ModelViewSet):
    queryset = RSS.objects.all()
    serializer_class = rssSerializer
