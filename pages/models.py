from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, PageChooserPanel)

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class HomePage(Page):
    banner_image = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=True)
    company_name = models.TextField(max_length=255, default='Charismatic Labs')
    banner_heading = models.TextField(max_length=255, default='Charismatic Labs')
    banner_text = models.TextField(max_length=255, default='')
    copyright_text = models.TextField(max_length=255, default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('banner_image'),
            FieldPanel('company_name'),
            FieldPanel('banner_heading'),
            FieldPanel('banner_text'),
            FieldPanel('copyright_text'),
        ], 'Banner'),
    ]

class AboutUs(Page):
    aboutus_heading = models.TextField(max_length=255, default='ABOUT US')
    aboutus_subheading = models.TextField(max_length=255, default='')
    aboutus_text = models.TextField(default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('aboutus_heading'),
            FieldPanel('aboutus_subheading'),
            FieldPanel('aboutus_text'),
        ], 'AboutUs'),
    ]

class AboutUsContent(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=True)
    name = models.TextField(max_length=255, default='')
    development_percent = models.TextField(max_length=255, default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('name'),
            FieldPanel('development_percent'),
        ], 'AboutUsContent'),
    ]

class ServiceHeading(Page):
    heading = models.TextField(max_length=255, default='OUR SERVICES')
    description = models.TextField(max_length=255, default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('heading'),
            FieldPanel('description'),
        ], 'ServiceHeading'),
    ]

class ServicePage(Page):
    heading = models.TextField(max_length=255, default='')
    description = models.TextField(max_length=255, default='')
    icon = models.TextField(max_length=255, default='fa-code')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('heading'),
            FieldPanel('description'),
            FieldPanel('icon'),
        ], 'Service'),
    ]

class TeamHeading(Page):
    heading = models.TextField(max_length=255, default='OUR TEAM')
    description = models.TextField(max_length=255, default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('heading'),
            FieldPanel('description'),
        ], 'TeamHeading'),
    ]

class TeamPage(Page):
    avatar = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=True)
    name = models.TextField(max_length=255, default='')
    designation = models.TextField(max_length=255, default='')
    description = models.TextField(max_length=255, default='')
    facebook_link = models.TextField(max_length=255, default='')
    twitter_link = models.TextField(max_length=255, default='')
    google_link = models.TextField(max_length=255, default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('avatar'),
            FieldPanel('name'),
            FieldPanel('designation'),
            FieldPanel('description'),
            FieldPanel('facebook_link'),
            FieldPanel('twitter_link'),
            FieldPanel('google_link'),
        ], 'Team'),
    ]

class PortfolioHeading(Page):
    heading = models.TextField(max_length=255, default='OUR WORKS')
    description = models.TextField(max_length=255, default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('heading'),
            FieldPanel('description'),
        ], 'PortfolioHeading'),
    ]

class PortfolioCategory(Page):
    name = models.TextField(max_length=255, default='OUR TEAM')
    internal_name = models.TextField(max_length=255, default='', help_text='This is used for categorisation(enter internal name without any space)')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('internal_name'),
        ], 'PortfolioCategory'),
    ]

class Portfolio(Page):
    name = models.TextField(max_length=255, default='')
    portfolio_category = models.ForeignKey(
        PortfolioCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    image = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            ImageChooserPanel('image'),
        ], 'Portfolio'),
        PageChooserPanel('portfolio_category'),
    ]

class ContactUs(Page):
    heading = models.TextField(max_length=255, default='STAY CONNECTED')
    description = models.TextField(max_length=255, default='')
    facebook_link = models.TextField(max_length=255, blank=True, null=True, help_text='If any of link is set empty then we will not show the icon.')
    twitter_link = models.TextField(max_length=255, blank=True, null=True)
    google_link = models.TextField(max_length=255, blank=True, null=True)
    instagram_link = models.TextField(max_length=255, blank=True, null=True)
    pinterest_link = models.TextField(max_length=255, blank=True, null=True)
    skype_link = models.TextField(max_length=255, blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('heading'),
            FieldPanel('description'),
            FieldPanel('facebook_link'),
            FieldPanel('twitter_link'),
            FieldPanel('google_link'),
            FieldPanel('instagram_link'),
            FieldPanel('pinterest_link'),
            FieldPanel('skype_link'),
        ], 'ContactUs'),
    ]