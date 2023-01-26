from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Booking(models.Model):
    """The booking model definition"""

    name = models.CharField(
        max_length=200,
        verbose_name=_("Name of Booking"),
    )
    number_of_guests = models.IntegerField(
        default=0,
        verbose_name=_("Number of Guests"),
    )

    class Meta:
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("booking_detail", kwargs={"pk": self.pk})


class Menu(models.Model):
    """Menu model definition"""

    title = models.CharField(
        verbose_name=_("Title of Menu"),
        max_length=200,
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=10,
        decimal_places=2,
    )
    inventory = models.IntegerField(verbose_name=_("Inventory"))

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menus")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("menu_detail", kwargs={"pk": self.pk})
