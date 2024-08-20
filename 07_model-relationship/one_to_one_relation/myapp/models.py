from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff':True})
    page_name = models.CharField(max_length=70)
    page_category = models.CharField(max_length=70)
    page_publish_date = models.DateField()


class Like(Page):
    page = models.OneToOneField(Page, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    likes = models.IntegerField()