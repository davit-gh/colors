from django.db import models
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged

from mezzanine.utils.models import upload_to
from mezzanine.core.models import RichText, Orderable
from mezzanine.pages.models import Page
from django.utils.translation import ugettext_lazy as _

COLUMN_CHOICES = (
    ('6', 'Two columns'), # 2 columns use span6
    ('4', 'Three columns'), # 3 columns use span4
    ('3', 'Four columns'), # 4 columns use span3
)

class Portfolio(Page):
    '''
    A collection of individual portfolio items
    ''' 
    content = RichTextField(blank = True)
    columns = models.CharField(max_length=1,choices=COLUMN_CHOICES,default='3')
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

class PortfolioItem(Page, RichText):
    
    featured_image = FileField(verbose_name=_("Featured Image"), upload_to=
            upload_to("main.PortfolioItem.featured_image", "portfolio"),\
            format="Image", max_length=255, null=True, blank=True)

    short_description = RichTextField(blank=True)
    categories = models.ManyToManyField("PortfolioItemCategory", 
            verbose_name=_("Categories"),\
            blank=True, related_name="portfolioitems")
    href = models.CharField(max_length=2000, blank=True,\
            help_text = "A link to the finished project (optional)")
    class Meta:
        verbose_name = _("Portfolio item")
        verbose_name_plural = _("Portfolio items")


class PortfolioItemImage(Orderable):
    portfolioitem = models.ForeignKey(PortfolioItem, related_name="images")
    file = FileField(_("File"), max_length=200, format="Image",\
        upload_to=upload_to("main.PortfolioItemImage.file", "portfolio items"))
    title = models.CharField(max_length=100, help_text="title of the portfolio item image", blank=True)
    subtitle = models.CharField(max_length=100, help_text="subtitle of the portfolio item image", blank=True)
    desc = RichTextField(help_text="desription of the portfolio item image", blank=True)
    class Meta:
        verbose_name="Portfolio Item Image"
        verbose_name_plural="Portfolio Item Images"

class PortfolioItemCategory(Slugged):
    """
    A category for grouping portfolio items into a series.
    """
    
    class Meta:
        verbose_name=_("Portfolio Item Category")
        verbose_name_plural=_("Portfolio Item Categories")
        ordering=("title",)


class Contactus(models.Model):
    name = models.CharField(_("Name"), max_length=100, blank=False)
    email = models.EmailField(blank=False)
    title = models.CharField(_("Title"), max_length=100, blank=False)
    description = models.TextField(_("Description"), blank=False)
    message_date = models.DateTimeField(auto_now_add=True, blank=True)
