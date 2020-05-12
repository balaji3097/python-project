from django.shortcuts import render
from .models import shop
from difflib import get_close_matches
import difflib
# Create your views here.
def garments(request):
    obj1=[]
    obj2=[]
    obj=shop.objects.all()
    for o in obj:
        obj1.append(o)
    obj2.append(obj1)
    
    return render(request,'garments.html',{'obj':obj2})

def search(request):
    itm1=[]
    lst=[]
    final=[]
    
    obj1=[]
    obj2=[]
    f_obj=shop.objects.all()
    for o in f_obj:
        obj1.append(o)
    obj2.append(obj1)

    obj=shop.objects.all()
  
    
    for item in obj:
        lst.append(item.brand_name)
    for itm in lst:
        itm1.append(itm.replace(" ",""))   
    for i in itm1:
        final.append(i.lower())
    
    if request.method == 'POST':
        item = request.POST.get('item')
        if len(item) != 0:
            inp=item.replace(" ","")
            lwr_item =inp.lower()
            
            local_val=[] 

            close_match=difflib.get_close_matches(lwr_item, final,5,0.6)
            close_matches = list(dict.fromkeys(close_match))
            for i in close_matches:
                local_val.append(final.index(i))
            val=[]
         
            matched=[]
            for j in local_val:
                matched.append(lst[j])
            length_matched=len(matched)    
            if length_matched != 0:  
                for k in matched:    
                    val.append(shop.objects.filter(brand_name=k))
                return render(request,'garments.html',{'obj':val})  
            else:

                 return render(request,'garments.html',{'war':'*Item Not Found'})    
        
        else:
            return render(request,'garments.html',{'obj':obj2})    