from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import ProfilePlugIn


class CMSProfilePlugIn(CMSPluginBase):
    model = ProfilePlugIn
    name = _("ProfilePlugIn")
    render_template = "ProfilePlugIn.html"

    def render(self, context, instance, placeholder):
        context.update({'profiles':instance.profiles, 'instance':instance, 'placeholder': placeholder})
        return context


plugin_pool.register_plugin(CMSProfilePlugIn)


