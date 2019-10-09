from django.db import models

# Create your models here.
from django.db import models
from django.forms import ModelForm, Textarea

# Create your models here.

class ModelPost(models.Model):

    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True,upload_to='images/')
    audio = models.FileField(null=True, blank=True, upload_to='audios/')
    description = models.TextField(max_length=120)


    def __str__(self):
        return self.title

class PostModelForm(ModelForm):
    class Meta:
        model = ModelPost
        fields=['title', 'image', 'description', 'audio']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),

        }