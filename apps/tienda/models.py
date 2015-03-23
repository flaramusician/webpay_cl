from django.db import models
from django.core.urlresolvers import reverse
import getpaid


# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})

    @property
    def total(self):
        return 1000

getpaid.register_to_payment(Order, unique=False, related_name='payments')