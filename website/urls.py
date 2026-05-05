from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    path('para-quem/', views.for_who, name='for_who'),
    path('solucoes/', views.solutions, name='solutions'),
    path('como-trabalhamos/', views.process_view, name='process'),
    path('porque-sum-connect/', views.why, name='why'),
    path('contato/', views.contact, name='contact'),
    path('automacao-whatsapp/', views.service_whatsapp, name='service_whatsapp'),
    path('integracao-sistemas/', views.service_integration, name='service_integration'),
    path('automacao-ia/', views.service_ia, name='service_ia'),
    path('power-bi-automatizado/', views.service_power_bi, name='service_power_bi'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('google0e0c0ed2b26b4964.html', TemplateView.as_view(template_name="website/google0e0c0ed2b26b4964.html", content_type='text/html')),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_post, name='blog_post'),
]
