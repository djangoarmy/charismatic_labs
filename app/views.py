from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from .models import ContactDetails
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
from pages.models import HomePage, AboutUs, AboutUsContent, ServiceHeading, ServicePage, TeamHeading, TeamPage, PortfolioHeading, Portfolio, ContactUs, PortfolioCategory

class IndexPageView(TemplateView):

    def get(self, request, **kwargs):
        context = {}
        banner = HomePage.objects.all().order_by('-id')
        if banner:
            context['banner'] = banner[0]
        about_us = AboutUs.objects.all().order_by('-id')
        if about_us:
            context['about_us'] = about_us[0]
        context['about_us_content'] = AboutUsContent.objects.all()
        service_heading = ServiceHeading.objects.all().order_by('-id')
        if service_heading:
            context['service_heading'] = service_heading[0]
        context['services'] = ServicePage.objects.all()
        team_heading = TeamHeading.objects.all().order_by('-id')
        if team_heading:
            context['team_heading'] = team_heading[0]
        context['team'] = TeamPage.objects.all()
        portfolio_heading = PortfolioHeading.objects.all().order_by('-id')
        if portfolio_heading:
            context['portfolio_heading'] = portfolio_heading[0]
        context['portfolios'] = Portfolio.objects.all()
        context['portfolio_categories'] = PortfolioCategory.objects.all()
        contact_us = ContactUs.objects.all().order_by('-id')
        if contact_us:
            context['contact_us'] = contact_us[0]
        return render(request, 'index.html', context=context)

    def post(self, request, *args, **kwargs):
        contact_name = request.POST.get('name', False)
        contact_email = request.POST.get('email', False)
        contact_subject = request.POST.get('subject', False)
        contact_message = request.POST.get('message', False)
        if contact_name and contact_email and contact_subject and contact_message:
            ContactDetails.objects.create(contact_name=contact_name, contact_email=contact_email, contact_subject=contact_subject, contact_message=contact_message)
            subject = 'New contact form submitted.'
            template = get_template('contactform_email_template.html')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_message': contact_message,
            })
            content = template.render(context)
            try:
                send_mail(subject, content, contact_email, ['admin@example.com'])
            except BadHeaderError:
                pass
            return render(request, 'index.html', {'success': True})
        return render(request, 'index.html', {'error': True})