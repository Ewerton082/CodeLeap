from django.db import models
from Users.models import User


class Posts(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE,blank=False, null=False, verbose_name="Owner Post")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created Data")
    title = models.CharField(max_length=60, null=False, blank=False, verbose_name="Post Title")
    content = models.TextField(blank=False, null=False, verbose_name="Post Content")

    def __str__(self):
        return f"{self.title} | {self.created_datetime}"


class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner Like")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name="Post Liked")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created Data")

    class Meta:
        unique_together = ("user", "post")
