from django import forms
from .models import Stock, BuyStock


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
            'name',
            'symbol',
            'boardlot',
            'broker'
        ]


class BuyStockForm(forms.ModelForm):
    class Meta:
        model = BuyStock
        fields = [
            # 'stock',
            'price',
            'share'
        ]
