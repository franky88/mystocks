from django.db import models
from django.db.models import Sum, FloatField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
import uuid
# Create your models here.
User = settings.AUTH_USER_MODEL


class Broker(models.Model):
    name = models.CharField(max_length=120, unique=True)
    website = models.URLField(blank=True, null=True)
    commission_fee = models.FloatField(default=0.0025)
    vat = models.FloatField(default=0.12)
    trans_fee = models.FloatField(default=0.00005)
    sccp_fee = models.FloatField(default=0.0001)
    sales_tax = models.FloatField(default=0.006)

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField(max_length=120)
    symbol = models.CharField(max_length=20, unique=True)
    boardlot = models.FloatField()
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, default=1)

    def total_share(self):
        total = Stock.objects.filter(symbol=self.symbol).aggregate(
            total=Sum('buystock__share'))
        if total == None:
            return 0
        else:
            return total['total']

    def total_investment(self):
        total = Stock.objects.filter(symbol=self.symbol).aggregate(
            total=Sum('buystock__total_investment'))
        if total == None:
            return 0
        else:
            return total['total']

    def total_price(self):
        if self.total_investment() and self.total_share():
            total = self.total_investment()/self.total_share()
            return total
        else:
            return 0

    def stock_name(self):
        name = "%s (%s)" % (self.name, self.symbol)
        return name

    def __str__(self):
        return self.stock_name()


class BuyStock(models.Model):
    ref_code = models.CharField(max_length=15, unique=True, blank=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.FloatField()
    share = models.FloatField()
    fees = models.FloatField(blank=True, null=True)
    average_price = models.FloatField(blank=True, null=True)
    total_average_price = models.FloatField(blank=True, null=True)
    total_investment = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.stock.stock_name()


@ receiver(post_save, sender=BuyStock)
def post_save_ref_code(sender, created, instance, *args, **kwargs):
    if created:
        instance.ref_code = str(uuid.uuid4()).replace("-", "").upper()[:15]
        instance.save()


@ receiver(pre_save, sender=BuyStock)
def pre_save_ref_code(sender, instance, *args, **kwargs):
    comm = instance.price * instance.share * instance.stock.broker.commission_fee

    def total_fees():
        if comm < 20:
            return 20.0
        else:
            return comm
    print(total_fees())
    instance.fees = total_fees() + (total_fees() * instance.stock.broker.vat) + (instance.price *
                                                                                 instance.share * instance.stock.broker.trans_fee) + (instance.price * instance.share * instance.stock.broker.sccp_fee)
    instance.average_price = ((
        instance.price*instance.share) + instance.fees)/instance.share
    if instance.stock.total_share() == None:
        instance.total_average_price = (
            instance.price*instance.share + instance.fees) / instance.share
    if instance.stock.total_share():
        instance.total_average_price = (
            instance.share/instance.stock.total_share()) * instance.average_price
    instance.total_investment = (
        instance.price*instance.share) + instance.fees
