from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from .forms import Listform
from .models import List
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
        form=Listform(request.POST or None)

        if form.is_valid():
            form.save()
            all_item=List.objects.all
            messages.success(request,('Item has been Added to List'))
            return render(request,'home.html',{'all_item':all_item})
    else:
        all_item=List.objects.all
        return render(request,"home.html",{'all_item':all_item})
def delete(request,list_id):
    item=List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,("Item Deleted Success"))
    return redirect('home')
def cross_off(request,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('home')
def uncross(request,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('home')
def edit(request,list_id):
    if request.method=="POST":
        item=List.objects.get(pk=list_id)
        form=Listform(request.POST or None,instance=item)

        if form.is_valid():
            form.save()
            messages.success(request,('Item has been Edited'))
            return redirect('home')
    else:
        item=List.objects.get(pk=list_id)
        return render(request,'edit.html',{'item':item})