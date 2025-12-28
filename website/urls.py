from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    path('para-quem/', views.for_who, name='for_who'),
    path('solucoes/', views.solutions, name='solutions'),
    path('como-trabalhamos/', views.process_view, name='process'),
    path('porque-sum-connect/', views.why, name='why'),
    path('contato/', views.contact, name='contact'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_post, name='blog_post'),
]
