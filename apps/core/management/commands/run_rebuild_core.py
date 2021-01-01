from tqdm import tqdm
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from apps.core.models import SiteConfiguration, NavigationLink, SocialLink, ContactDetail, AboutDetail, Disqus


class Command(BaseCommand):

    def handle(self, *args, **options):

        #######################################################################
        # user model entries

        print('\n adding user model entries')

        user_model = get_user_model()

        try:
            user_model.objects.get(username='admin')

        except user_model.DoesNotExist:
            user_model.objects.create_superuser(username='admin',
                                                email='admin@djangomango.com',
                                                password='pass1234')


        #######################################################################
        # site config

        print('\n adding site config')

        site_config = SiteConfiguration.objects.filter(is_active=True).last()

        if not site_config:
            site_config = SiteConfiguration()

        site_config.site_name = "Site Name"
        site_config.site_url = "http://www.djangomango.com/"
        site_config.site_description = """
Site description
        """

        site_config.is_active = True

        site_config.save()


        #######################################################################
        # navigation menu links

        print('\n adding navigation menu links')

        nav_items = [
            {'order': 0, 'title': 'Home', 'target': '/', 'featured': False},
        ]

        for item in tqdm(nav_items):
            order = item.pop('order', 0)

            NavigationLink.objects.update_or_create(
                site_config=site_config,
                order=order,
                defaults={**item}
            )


        #######################################################################
        # social media links

        print('\n adding social media links')

        social_items = [
            {'order': 0, 'title': 'Twitter', 'icon_class': 'fa-twitter', 'social_url': ''},
            {'order': 1, 'title': 'Facebook', 'icon_class': 'fa-facebook-f', 'social_url': ''},
            {'order': 2, 'title': 'LinkedIn', 'icon_class': 'fa-linkedin-in', 'social_url': ''},
            {'order': 3, 'title': 'YouTube', 'icon_class': 'fa-youtube', 'social_url': ''}
        ]

        for item in tqdm(social_items):
            order = item.pop('order', 1)

            SocialLink.objects.update_or_create(
                site_config=site_config,
                order=order,
                defaults={**item}
            )


        #######################################################################
        # contact details

        print('\n adding contact details')

        dic = {
            'email': 'contact@djangomango.com',
            'address': 'Address'
        }

        ContactDetail.objects.update_or_create(
            site_config=site_config,
            defaults={**dic}
        )


        #######################################################################
        # about details

        print('\n adding about details')

        summary = """
About details
        """

        dic = {
            'summary': summary
        }

        AboutDetail.objects.update_or_create(
            site_config=site_config,
            defaults={**dic}
        )


        #######################################################################
        # disqus

        print('\n adding disqus url')

        dic = {
            'is_active': False,
            'disqus_url': '',
        }

        Disqus.objects.update_or_create(
            site_config=site_config,
            defaults={**dic}
        )
