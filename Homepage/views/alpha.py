
# from django.shortcuts import render
#
# from Homepage.models import Produkty
#
#
# def home(request):
#     zmiennaprodukty = Produkty.objects
#     return render(request, 'home.html', {'produkty':zmiennaprodukty})
#
#


from django.views.generic import TemplateView

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

from StronaMaracza.settings import EMAIL_HOST_USER


class SendFormEmail(View):


    def  get(self, request):

        # Get the form data
        name = request.GET.get('name', None)
        message = request.GET.get('message', None)
        emailik = request.GET.get('emailik', None)
        nazwisko = request.GET.get('nazwisko', None)
        # Send Email
        send_mail(
            'Bentley coraz bliżej',
            'Cześć, tu ' + name + ' ' + nazwisko + ',\n' + 'Mój adres email to: ' + emailik + ',\n' + '\n' + message,
            'sender@example.com', # Admin
            [ EMAIL_HOST_USER ],
        )

        # Redirect to same page after form submit
        messages.success(request, ('Wiadomość została wysłana.'))
        return redirect('home')

