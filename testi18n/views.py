from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext as _


class IndexPage(TemplateView):
    template_name = 'index.html'


class TestView(APIView):
    def get(self, request):
        data = []
        data.append({
            'title': _("hello")})
        return Response({'data': data}, status=status.HTTP_200_OK)
