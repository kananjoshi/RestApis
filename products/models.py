from django.db import models
from django.utils.translation import ugettext as _


class Category(models.Model):
    name = models.CharField(_("Product"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_("Product"), max_length=50, blank=True, null=True)
    price = models.IntegerField(_("Price"))
    category = models.ForeignKey(Category, related_name=_("category"), on_delete=models.DO_NOTHING)
    image = models.ImageField(_("Product Image"), upload_to='media/proucts/')

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
