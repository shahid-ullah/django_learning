from django.urls import path

from .views import AboutPage, HomePage

urlpatterns = [
    # path('about/', about, name='about'),
    path('about/', AboutPage.as_view(), name='about'),
    path('home/', HomePage.as_view(), name='home'),
]
