from django .urls import path
from rest_framework import routers
from .views import MenuItemsView, menuview, bookingview
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.index, name = 'index' ),
    #path('menu/', menuview.as_view()),
    path('booking/', bookingview.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
