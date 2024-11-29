from django.shortcuts import render
from .models import Blog,Contact,Services,About
from django.views.generic.edit import FormView
from .forms import ContactForm
from .bot import send_message
from django.views.generic.list import ListView
from django.views import View

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


from django.shortcuts import render
from django.views import View
from .models import Contact
from .bot import send_message  # Assuming send_message is your bot function

class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        first_name = request.POST.get('first_name')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        # country = request.POST.get('country')
        # subject = request.POST.get('subject')
        # content = request.POST.get('content')  

        # Save contact info in the database
        contact = Contact(
            first_name=first_name,
            full_name=full_name,
            email=email
            # You can save other fields here as well
        )
        contact.save()

        # Prepare the message text for the bot
        message_text = f"New Contact Form Submission:\n\nFirst Name: {first_name}\nFull Name: {full_name}\nEmail: {email}"

        # Send the contact info to the bot
        send_message(message_text)

        # Print for debugging purposes
        print("Siz Post request yubordingiz")

        # After sending the message, render the contact page again or redirect
        return render(request, self.template_name)


class ServicesListView(ListView):
    model = Services
    template_name = 'services.html'
    context_object_name = 'services'















