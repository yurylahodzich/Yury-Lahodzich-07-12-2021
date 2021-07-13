from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from chat.models import Message
from chat.serializer import MessageSerializer


class MessageViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['get'])
    def search_messages(self, request, pk=None):
        received_queryset = Message.objects.filter(receiver_id=pk)
        received_data = MessageSerializer(received_queryset, many=True).data

        sent_queryset = Message.objects.filter(sender_id=pk)
        sent_data = MessageSerializer(sent_queryset, many=True).data

        return Response({
            "received": received_data,
            "sent": sent_data
        }, status=status.HTTP_200_OK)
