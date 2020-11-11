from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

import logging
logger = logging.getLogger(__name__)






class TestEndpoint(APIView):
    def post(self, request, format=None):

        # logger.info(request.data['filename'])

        logger.info(request.session.get())

        



        return Response("test")