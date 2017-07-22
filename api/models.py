from django.db import models

class Listing(models.Model):
    tx_id = models.CharField(max_length=255, primary_key=True)
    game_name = models.CharField(max_length=255, default="", blank=True, null=True)
    currency_name = models.CharField(max_length=255, default="", blank=True, null=True)
    currency_amount = models.IntegerField(default=0, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    cost = models.CharField(max_length=255, default="", blank=True, null=True)
    seller_address = models.CharField(max_length=255, default="", blank=True, null=True)
    block_number = models.IntegerField(default=0, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.tx_id)

    class Meta:
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
        app_label = "api"


