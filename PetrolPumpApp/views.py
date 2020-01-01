# Create your views here.
from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from django.views import View
from PetrolPumpApp.models import PetrolList
from django.db.models import Q
from datetime import date



# Create your views here.
def PetrolData(request):
    pdata = PetrolList.objects.raw("select  Id,ROW_NUMBER() OVER (ORDER BY Id) row_num,City,Price,Changes from PetrolPumpApp_petrollist")
    resultquery = (Q(City='Delhi') | Q(City='Mumbai') | Q(City='Kolkatta') | Q(City='Chennai'))
    MetroCity_data = PetrolList.objects.filter(resultquery)
    PageData = {
        'AllCityData': pdata,
        'MetroCityData': MetroCity_data,
        'Today': date.today()
    }
    return render(request, 'PetrolPumpApp/index.html', context=PageData)


def DieselData(request):
    pdata = PetrolList.objects.raw("select  Id,ROW_NUMBER() OVER (ORDER BY Id) row_num,City,Price,Changes from PetrolPumpApp_petrollist")
    resultquery = (Q(City='Delhi') | Q(City='Mumbai') | Q(City='Kolkatta') | Q(City='Chennai'))
    MetroCity_data = PetrolList.objects.filter(resultquery)
    PageData = {
        'AllCityData': pdata,
        'MetroCityData': MetroCity_data,
        'Today': date.today()
    }
    return render(request, 'PetrolPumpApp/deisel.html', context=PageData)


# class HomePage(View):
#     def get(self,request,page_type='petrol'):
#         pdata=PetrolList.objects.raw("select  Id,ROW_NUMBER() OVER (ORDER BY Id) row_num,City,Price,Changes from PetrolPumpApp_petrollist")
#         resultquery = (Q(City='Delhi') | Q(City='Mumbai') | Q(City='Kolkatta') | Q(City='Chennai'))
#         MetroCity_data=PetrolList.objects.filter(resultquery)
#         PageData={
#             'AllCityData':pdata,
#             'MetroCityData':MetroCity_data,
#             'Today':date.today()
#         }
#         return render(request, 'PetrolPumpApp/index.html',context=PageData)
#     def post(self,request):
#         getRadio= request.POST.get("options")
#         if(getRadio=='P'):
#             pdata = PetrolList.objects.raw("select  Id,ROW_NUMBER() OVER (ORDER BY Id) row_num,City,Price,Changes from PetrolPumpApp_petrollist")
#             resultquery = (Q(City='Delhi') | Q(City='Mumbai') | Q(City='Kolkatta') | Q(City='Chennai'))
#             MetroCity_data = PetrolList.objects.filter(resultquery)
#             PageData = {
#                 'AllCityData': pdata,
#                 'MetroCityData': MetroCity_data,
#                 'Today': date.today()
#             }
#             return render(request, 'PetrolPumpApp/index.html',context=PageData)
#         return render(request, 'PetrolPumpApp/index.html', {"Account": "Ashutosh Rai"})