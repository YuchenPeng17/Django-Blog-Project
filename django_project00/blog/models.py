from django.db import models

# Create your models here.
class Article(models.Model):
    # ID
    article_id = models.AutoField(primary_key=True)
    # Title
    title = models.TextField()
    # Abstract
    abstract = models.TextField()
    # Content
    content = models.TextField()
    # Published Date
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title