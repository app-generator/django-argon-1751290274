# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    first_name = models.TextField(max_length=255, null=True, blank=True)
    last_name = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Invoice(models.Model):

    #__Invoice_FIELDS__
    invoice_number = models.TextField(max_length=255, null=True, blank=True)
    invoice_issuance_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    invoice_payment_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    invoice_amount = models.IntegerField(null=True, blank=True)

    #__Invoice_FIELDS__END

    class Meta:
        verbose_name        = _("Invoice")
        verbose_name_plural = _("Invoice")



#__MODELS__END
