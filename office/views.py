from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse ("خوش امدید") 

def sazman(request,esm):
  if (esm=="kar" or esm=="tamin" or esm=="uni"):   
    if (esm=="kar"): d={"sazman": "اداره کار", "address":"شهرکرد - خیابان جهاد ", "phone":"038-32266200", "address electroniki":"kar@ir"}
    if (esm=="tamin"):  d={"sazman": "تامین اجتماعی", "address":"خیابان کاشانی ","phone":"038-32267500", "address electroniki":"tamin@ir"}
    if (esm=="uni"): d={"sazman": "اداره فنی و حرفه ای", "address":"خیابان انقلاب", "phone":"038-32268500", "آدرس سایت":"etvto@ir"}
    return render(request,"offfice/m.html",context=d)
  else:
      return HttpResponse("موردی یافت نشد")  

  
        