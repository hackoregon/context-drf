from rest_framework import viewsets
from rest_framework.response import Response
from django.apps import apps

class ContextViewSet(viewsets.ViewSet):
  """
  List all Context sources
  """
  def list(self, request):
    return Response(apps.get_app_config('context').all())

  def retrieve(self, request, pk=None):
    return Response(apps.get_app_config('context').source(pk))
