from django.db import models
from cms.models.pluginmodel import CMSPlugin

class Profile(CMSPlugin):
    bio = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="myproject/media/cms_page_media")

    def __unicode__(self):
        return self.bio











