from django.db import models
from cms.models.pluginmodel import CMSPlugin



class Profile(models.Model):
    bio = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="uploads/uploads/images/")

    def __unicode__(self):
        return self.bio


class ProfilePlugIn(CMSPlugin):
    profiles = Profile.objects.all()














