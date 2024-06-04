from django.db import models
from django.urls import reverse
from django.db.models.functions import Lower
from django.db.models import UniqueConstraint

# Create your models here.
class Project(models.Model):
    title = models.CharField(
        max_length=100,
        help_text='Please provide an unique project title.'
        )
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True)


    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('title'),
                name='project_title_case_insensitive_unique',
                violation_error_message='Project already exists (case insensitive match)'
            ),
        ]