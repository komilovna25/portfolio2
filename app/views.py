from django.shortcuts import render
from .models import Blog,Contact,Services,About
from django.views.generic.edit import FormView
from .forms import ContactForm
from .bot import send_message
from django.views.generic.list import ListView


def home_view(request):
    return render(request=request, template_name='index.html')


class AboutListView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'

    
class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/" 
    
    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        full_name = form.cleaned_data.get('full_name')
        email = form.cleaned_data.get('email')
        content = form.cleaned_data.get('content')

        text = f"Name: {first_name}\nEmail: {email}\nMessage: {content}"
        send_message(text)  

        Contact.objects.create(
            first_name=first_name,
            email=email,
            content=content
        )

        return super().form_valid(form)

class ServicesListView(ListView):
    model = Services
    template_name = 'services.html'
    context_object_name = 'services'















