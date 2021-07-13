from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from chat.models import Message
from chat.serializer import MessageSerializer


class MessageViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (AllowAny,)
