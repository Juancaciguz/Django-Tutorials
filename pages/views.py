from django.shortcuts import render
from django.views.generic import TemplateView 
# Create your views here.
class HomePageView(TemplateView): 
    template_name = 'pages/home.html'
class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 
 
     
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Juan Carlos", 
        }) 
 
        return context
class ContactPageView(TemplateView): 
    template_name = 'pages/contact.html'
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "email": "robert@gmail.com",
            "adress":"123 Street, New York, USA",
            "phone": "+1234567890",
        })
        return context