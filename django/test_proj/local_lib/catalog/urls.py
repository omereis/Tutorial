#
# c a t a l o g / u r l s . p y
#
from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
]


