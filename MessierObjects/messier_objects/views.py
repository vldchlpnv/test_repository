from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_page(request):
    return HttpResponse("Заголовок главной страницы")
def function_1(request):
    return HttpResponse("Остаток сверхновой")
def function_2(request):
    return HttpResponse("Шаровое скопление")
def function_3(request):
    return HttpResponse("Рассеянное скопление")
def function_4(request):
    return HttpResponse("Рассеянное скопление с туманностью")
def function_5(request):
    return HttpResponse("Рассеянное скопление и эмиссионная туманность")
def function_6(request):
    return HttpResponse("Планетарная туманность")
def function_7(request):
    return HttpResponse("Галактика")
def function_8(request):
    return HttpResponse("Эмиссионная туманность")
def function_9(request):
    return HttpResponse("Группа звезд")
def function_10(request):
    return HttpResponse("Диффузная туманность")
