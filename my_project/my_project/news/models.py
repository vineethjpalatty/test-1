from django.db import models
from django.forms import ModelForm, Textarea
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Editorial(models.Model):
    Heading = models.CharField(max_length=200)
    Description = models.TextField(max_length=200)

    def __str__(self):
        return self.Heading

class EditorialForm(ModelForm):
    class Meta:
        model = Editorial
        fields=['Heading','Description']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),

        }