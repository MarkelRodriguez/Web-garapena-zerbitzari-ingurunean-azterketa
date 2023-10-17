from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('index/', views.index, name='index2'),
    path('pertsona/', views.pertsona, name='pertsona'),
    path('etxea/', views.etxea, name='etxea'),
    path('gehitualokairua/',views.gehitualokairua,name='gehitualokairua'),
    path('gehitualokairua/gehituerregistroalokairua/',views.gehituerregistroalokairua,name='gehituerregistroalokairua'),
    path('pertsona/gehitupertsona/', views.gehitupertsona,name='gehitupertsona'),
    path('pertsona/gehitupertsona/gehituerregistropertsona/', views.gehituerregistropertsona,name='gehituerregistropertsona'),
    path('etxea/gehituetxea/', views.gehituetxea,name='gehituetxea'),
    path('etxea/gehituetxea/gehituerregistroetxea/', views.gehituerregistroetxea,name='gehituerregistroetxea'),
    path('pertsona/ezabatupertsona/<dni>', views.ezabatupertsona,name='ezabatupertsona'),
    path('pertsona/eguneratupertsona/<dni>/', views.eguneratupertsona,name='eguneratupertsona'),
    path('eguneratuerregistropertsona/<dni>', views.eguneratuerregistropertsona,name='eguneratuerregistropertsona'),
    path('etxea/ezabatuetxea/<int:id>', views.ezabatuetxea,name='ezabatuetxea'),
    path('etxea/eguneratuetxea/<int:id>/', views.eguneratuetxea,name='eguneratuetxea'),
    path('eguneratuerregistroetxea/<int:id>', views.eguneratuerregistroetxea,name='eguneratuerregistroetxea'),
]