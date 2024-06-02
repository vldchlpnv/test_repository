from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.
def main_page(request):
    return HttpResponse("Заголовок главной страницы")
def types_of_objects(request, types_slug): # обьекты по их категориям в виде динамических url(попробуем так)
    return HttpResponse(f"<h1>Типы объектов из каталога Месье</h1><p>{types_slug}")
def discovery_date(request, discovery_date_convert): # год открытия объекта(потом добавлю вместе с датой открытия)
    return HttpResponse(f"<h1>Год открытия</h1><p>{discovery_date_convert}")
def each_object(request, object_name): # каждый обьект из каталога по отдельности
    print(request.GET)
    if int(object_name[1:]) > 110 or int(object_name[1:]) <= 0:
        raise Http404()
    return HttpResponse(f"<h1>Объект</h1><p> {object_name}")
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



#def function_1(request):
#    return HttpResponse("Остаток сверхновой")
#def function_2(request):
#    return HttpResponse("Шаровое скопление")
#def function_3(request):
#    return HttpResponse("Рассеянное скопление")
#def function_4(request):
#    return HttpResponse("Рассеянное скопление с туманностью")
#def function_5(request):
#    return HttpResponse("Рассеянное скопление и эмиссионная туманность")
#def function_6(request):
#    return HttpResponse("Планетарная туманность")
#def function_7(request):
#    return HttpResponse("Галактика")
#def function_8(request):
#    return HttpResponse("Эмиссионная туманность")
#def function_9(request):
#    return HttpResponse("Группа звезд")
#def function_10(request):
#    return HttpResponse("Диффузная туманность")
