from django.shortcuts import redirect, render
from .forms import MyRegisterForm
from .models import RegisterForm

# Create your views here.
def home(request):
    if request.method=="POST":
        minage=request.POST.get('minage')
        maxage=request.POST.get('maxage')
        resultobj=RegisterForm.objects.raw('select id,name,age,address,contact,email from datas where age between "'+minage+'" and "'+maxage+'"')
        return render(request,'home.html',{"data":resultobj})
    else:
        data=RegisterForm.objects.all()
        return render(request,"home.html",{'data':data}) 


def insert(request):
    if request.method=='POST':
        form= MyRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("Home")
            except:
                pass
    else:
        form= MyRegisterForm()
    return render(request,"register.html",{'form':form})   


def update(request,id):
    data=RegisterForm.objects.get(id=id)
    if request.method== 'POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']

        data.name=name
        data.age=age
        data.address=address
        data.contact=contact
        data.email=email
        data.save()
        return redirect("Home")

    return render(request,"update.html",{'data':data})

def delete(request,id):
    data=RegisterForm.objects.get(id=id)
    data.delete()
    return redirect('Home')


    


       

