from django.urls import path
from . import views
app_name = "stocks"
urlpatterns = [
    path('', views.stock_list, name="list"),
    path('details/<symbol>', views.stock_details, name='details'),
    path('update/<ref_code>', views.update_stock, name='update'),
    path('delete/<pk>', views.delete_stock, name='delete'),
    path('delete/stock/<ref_code>', views.delete_buy_stock, name='delete_buy'),
]
