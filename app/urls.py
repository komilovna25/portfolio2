from django.conf.urls.static import static
from django.urls import path, include
from .views import home_view, BlogListView, ContactFormView, ServicesListView,AboutListView

urlpatterns = [
    path('', home_view, name='index-page'),
    path('blog/', BlogListView.as_view(), name='blog-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('services/', ServicesListView.as_view(), name='services-page'),
    path('about/', AboutListView.as_view(), name='about-page'),

]
