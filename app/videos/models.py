from django.db import models
from common.models import CommonModel
from users.models import User

# from reactions.models import Reaction


# homework
# class ReactionManager(models.Manager):
#     def get_queryset(self):
#         # likes_count = self.get_queryset().filter().count()
#         likes_count = Reaction.objects.filter(reaction=1).count()
#         # dislikes_count = Reaction.objects.filter(reaction=-1).count()
#         return likes_count


class Video(CommonModel):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField()
    video_uploaded_url = models.URLField()
    video_file = models.FileField(upload_to='storage/')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes_count = ReactionManager()
