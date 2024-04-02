from django.shortcuts import render

# Create your views here.
def data_from_be(request):
    d={"name":"NAME",'course':"B.Tech", "age":21}
    return render(request,"data_from_be.html",context=d)

