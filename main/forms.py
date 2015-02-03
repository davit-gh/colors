from main.models import Contactus
from django.forms import ModelForm

class ContactusForm(ModelForm):
	class Meta:
		model = Contactus
		fields = ['name', 'email', 'title', 'description']
