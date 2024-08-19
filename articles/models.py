from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Article(models.Model):
   title = models.CharField(max_length=255)
   body = models.TextField()
   created_on = models.DateTimeField(auto_now_add=True)
   author = models.ForeignKey(
     get_user_model(),
     on_delete=models.CASCADE,
     )
   updated_on = models.DateTimeField(auto_now= True)
   status = models.IntegerField(choices=STATUS, default=0)

   class Meta:
        ordering = ['-created_on']

   def __str__(self):
     return self.title
   
   def get_absolute_url(self):
     return reverse('article_detail', args=[str(self.id)])