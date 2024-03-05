from django.db import models

from users.models import User

from common.models import CommonModel


# Chat 모델
# ChatRoom: 오픈채팅방(비번o, 비번x), 개인채팅방
# ChatMessage: 메시지를 주고 받는 모델

class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)
    # type = models.CharField()
    # is_password =
    # room_password =


class ChatMessage(CommonModel):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()


# Room:Message (1:N)
# Room => Message, Message, Message (o)
# Message => Room1, Room2, Room3 (x)
