from apps.core.models import SiteConfiguration


def core(request):

    site_config = SiteConfiguration.objects.filter(is_active=True).last()

    return {
        'site_config': site_config,
        'navigation_links': site_config.navigation_link.all(),
        'social_links': site_config.social_link.all(),
        'contact_detail': site_config.contact_detail,
        'about_detail': site_config.about_detail,
        'disqus': site_config.disqus,
    }