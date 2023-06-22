from django.db import models
import uuid
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=500, null=True,blank=True)
    source_link = models.CharField(max_length=1000,null=True,blank=True)
    tag = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Projects'