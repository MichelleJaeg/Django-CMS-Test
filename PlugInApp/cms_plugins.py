from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import Profile


class PicturePlugIn(CMSPluginBase):
    model = Profile
    name = _("PicturePlugIn")
    render_template = "PicturePlugIn.html"

    def render(self, context, instance, placeholder):
        context.update({'profile':instance.profile, 'object':instance, 'placeholder': placeholder})
        return context


plugin_pool.register_plugin(PicturePlugIn)


