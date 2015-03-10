from django.shortcuts import render
from main.forms import ContactusForm
from django.contrib import messages
from django.utils.translation import ugettext as _

# Create your views here.
def contactus(request):
	if request.method == 'POST':
        	form = ContactusForm(request.POST)
        # check whether it's valid:
        	if form.is_valid():
            	# process the data in form.cleaned_data as required
            		form.save()
            	# redirect to a new URL:
			messages.info(request, _("We received your message, we will respond shortly. Thank you!"))
		else:
			messages.error(request, _("Your message has not been sent. Please fill in all the fields."))
    	# if a GET (or any other method) we'll create a blank form
    	else:
        	form = ContactusForm()

	return render(request,'base.html',{'form':form})
