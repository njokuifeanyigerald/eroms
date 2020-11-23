from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    
    ent = Entry.objects.order_by('-date_posted')    #variable called entries which represents entries in the db

    context = {
                'ent' : ent
            }  # dictionary that makes whatever is here avaialable in the template

    return render(request, 'hello/app2.html', context)



def indexs(request):
    if request.method == 'POST':
        form = EntryForm(request.POST or None)    

        if form.is_valid():          #check that the form is valid      
            form.save()     #because I am using a model form the form is saved automatically
            return redirect('add')  #redirect to the records page after saving      
        

    else:
        form = EntryForm()

    context = {'form': form}

    return render(request, 'hello/app1.html', context)

@login_required
def delete_view(request, id):
    context = {}

    obj = get_object_or_404(Entry, id = id)

    if request.method =='POST':
        obj.delete()
        return redirect('add') 

        
    return render(request, 'hello/delete_view.html', context) 


@login_required
def edit_view(request, id):
    qs = get_object_or_404(Entry, id = id)
    form = EntryForm(request.POST or None,request.FILES or None , instance = qs)
    if request.method =='POST':
        # form = EntryForm(request.POST  , instance = obj)
        if form.is_valid():
            form.save()
            return redirect('add') 
    # else:
    #     form = EntryForm()        
 

    context = {'form': form}

    return render(request, 'hello/edit.html', context)

    



