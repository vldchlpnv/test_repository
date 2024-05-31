from . import views # точка потому что импортируем из текущего модуля если вписать имя текущего модуля будет красным подсвечено
from django.urls import path


urlpatterns = [
    path('', views.main_page),
    path('supernova_remnant/', views.function_1),
    path('globular_cluster/', views.function_2),
    path('open_cluster/', views.function_3),
    path('nebula_with_cluster/', views.function_4),
    path('H_II_region_nebula_with_cluster/', views.function_5),
    path('planetary nebula/', views.function_6),
    path('galaxy/', views.function_7),
    path('H_II_region_nebula/', views.function_8),
    path('asterism/', views.function_9),
    path('diffuse_nebula/', views.function_10),
    ]
