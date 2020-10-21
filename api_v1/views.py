from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)

class TestEndpoint(APIView):
    def post(self, request, format=None):

        logger.warning("helloo thi is warning")

        logger.error("hthisi is info")

        return Response("test")