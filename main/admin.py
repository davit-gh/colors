from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from main.models import Portfolio, PortfolioItem, PortfolioItemImage, PortfolioItemCategory
#from main.models import Order
#from cartridge.shop.forms import ProductAdminForm


class PortfolioItemImageInline(TabularDynamicInlineAdmin):
	model=PortfolioItemImage

class PortfolioItemAdmin(PageAdmin):
	inlines=(PortfolioItemImageInline, )

#admin.site.register(Order,PageAdmin)
admin.site.register(Portfolio,PageAdmin)
admin.site.register(PortfolioItem,PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)


from copy import deepcopy
from django.contrib import admin
from mezzanine.forms.admin import FormAdmin
from mezzanine.forms.models import Form

form_fieldsets = deepcopy(FormAdmin.fieldsets)
form_fieldsets[0][1]["fields"].insert(-2, "bgimagee")

class MyFormAdmin(FormAdmin):
    fieldsets = form_fieldsets

admin.site.unregister(Form)
admin.site.register(Form, MyFormAdmin)

from main.models import Contactus
class ContactusAdmin(admin.ModelAdmin):
	list_display=('name','email','title','description', 'message_date')

admin.site.register(Contactus,ContactusAdmin)
