from django.shortcuts import redirect, render, get_object_or_404
from .models import Stock, BuyStock
from django.db.models import Sum, Count
from .forms import StockForm, BuyStockForm
# Create your views here.


def stock_list(request):
    stocks = Stock.objects.all().order_by('name')
    form = StockForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        return redirect('stocks:list')
    context = {
        'title': 'stock list',
        'stocks': stocks,
        'form': form
    }
    return render(request, 'stock_list.html', context)


def stock_details(request, symbol):
    stock = get_object_or_404(Stock, symbol=symbol)
    update_form = StockForm(request.POST or None, instance=stock)
    buy_stock_form = BuyStockForm(request.POST or None)
    if update_form.is_valid():
        instance = update_form.save(commit=False)
        instance.save()
        return redirect('stocks:details', symbol=stock.symbol)
    if request.method == "POST":
        if buy_stock_form.is_valid():
            instance = buy_stock_form.save(commit=False)
            instance.stock = stock
            instance.save()
        return redirect('stocks:details', symbol=stock.symbol)
    # if request.method == "POST":
    #     if update_form.is_valid():
    #         instance = update_form.save(commit=False)
    #         instance.save()
    #     return redirect('stocks:details', symbol=stock.symbol)
    context = {
        'title': 'stock details',
        'stock': stock,
        'updateform': update_form,
        'buystockform': buy_stock_form,
    }
    return render(request, 'stock_details.html', context)


def delete_stock(request, *args, **kwargs):
    stock_pk = kwargs.get('pk')
    delete_stock = get_object_or_404(Stock, pk=stock_pk)
    if request.method == "POST":
        delete_stock.delete()
        return redirect('stocks:list')
    context = {
        'instance': delete_stock,
    }
    return render(request, 'delete_stock.html', context)


def update_stock(request, *args, **kwargs):
    ref_code = kwargs.get('ref_code')
    update_stock = get_object_or_404(BuyStock, ref_code=ref_code)
    update_stock_form = BuyStockForm(
        request.POST or None, instance=update_stock)
    if request.method == "POST":
        if update_stock_form.is_valid():
            instance = update_stock_form.save(commit=False)
            instance.stock = update_stock.stock
            instance.save()
        return redirect('stocks:details', symbol=update_stock.stock.symbol)
    context = {
        'updatestockform': update_stock_form
    }
    return render(request, 'update_stock.html', context)


def delete_buy_stock(request, *args, **kwargs):
    stock_pk = kwargs.get('ref_code')
    delete_buy_stock = get_object_or_404(BuyStock, ref_code=stock_pk)
    if request.method == "POST":
        delete_buy_stock.delete()
        return redirect('stocks:details', symbol=delete_buy_stock.stock.symbol)
    context = {
        'instance': delete_buy_stock
    }
    return render(request, 'delete_stock.html', context)
