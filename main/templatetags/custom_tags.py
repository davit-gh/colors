from main.models import PortfolioItemCategory, PortfolioItem
from mezzanine.pages.models import Page
from mezzanine.forms.models import Form
from mezzanine.galleries.models import Gallery
from django.template import RequestContext
from main.forms import ContactusForm

from mezzanine import template
register = template.Library()
import pdb


@register.as_tag
def get_project_portitems(*args):
	project_portitems = PortfolioItemCategory.objects.get(slug='projects').portfolioitems.all()
	return project_portitems

@register.as_tag
def get_services_portitem(*args):
	services_portitem = PortfolioItemCategory.objects.get(slug='services').portfolioitems.all()[0]
	return services_portitem

@register.as_tag
def get_about(*args):
	about_page = Page.objects.get(slug="about")
	staff = PortfolioItem.objects.get(parent=about_page)
	#pdb.set_trace()
	return [about_page, staff]

@register.as_tag
def get_gallery_images(*args):
	gallery = Gallery.objects.get(slug="gallery")
	images = gallery.images.all()
	categories = gallery.categories
	#pdb.set_trace()
	return [images, categories]


@register.as_tag
def get_contact_form(*args):
	return ContactusForm()
