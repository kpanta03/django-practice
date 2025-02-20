from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User#Authentication ko lagi
from django.contrib import messages#alert message ko lagi
from django.contrib.auth import authenticate,login,logout#authenticate euta function ho jasma hami username and password halni and check garera boolean value/object dinxa if username and password right vayo vani. Login le session maintain garxa. Logout is used to logging out
from django.contrib.auth.decorators import login_required#mathhi url bata ni authenticate banauxa
from django.core.paginator import Paginator#pagination ko lagi use hunxa in report project
from  django.db.models import Q,Sum#multiple columns filter garna ko lagi use hunxa.Sum aggregate ma use hunxa
# Create your views here.


@login_required(login_url="/login/")
def recipes(request):
    if request.method=="POST":
        data=request.POST#form ko data backend ma pathauna ko lagi.

        # recipe_image=request.FILES.get('recipe_image') Image xa vani yesto garni

        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_category=data.get('recipe_category')

        # yetai print garna lai
        print(recipe_name)
        print(recipe_description)
        print(recipe_category)

        # sql ma pathauna ko lagi
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_category=recipe_category
        )

        return redirect('/recipes/')#redirect garna use hunxa.
    
    queryset=Recipe.objects.all()

    #  search ko lagi this is a another method instead of request post method
    if request.GET.get('search'):
        queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))#search ma search gareko value recipe_name ma auxa ki nai check garxa.
    # ya samma search ko lagi

    context={'recipes':queryset}
    return render(request,'recipes.html',context)

# Delete garna ko lagi

def delete_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')
    
# update
def update_recipe(request, id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST

        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_category=data.get('recipe_category')

        queryset.recipe_name=recipe_name,
        queryset.recipe_description=recipe_description,
        queryset.recipe_category=recipe_category

        queryset.save()
        return redirect('/recipes/')
    
    context={'recipe':queryset}
    return render(request,'update_recipes.html',context)

# login ko lagi
def login_page(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        # username exists garena vani.
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username.")
            return redirect('/login/')
        
        # username ko password correct xaki nai check garxa. if correct return object otherwise none.
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/login/')
        # ekchoti login garesi feri garna naparos vanera session use garni until that session expires
        else:
            login(request,user)
            return redirect('/recipes/')        
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')        
    
def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        

# username same haleko case ma k garni
        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already exists.")
            return redirect('/register/')
# 

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            # password=password password lai encrypt garni vaye yeta nalekha.
        )

        user.set_password(password)#this will encrypt password
        user.save()
        messages.info(request, "Account created successfully")
        return redirect('/register/')

    return render(request,'register.html')


# report card project ko lagi
def get_students(request):
    queryset=Student.objects.all()
    # filter/search ko code
    if request.GET.get('search'):
        search=request.GET.get('search')
        # queryset=queryset.filter(student_name__icontains=search)#yesle student_name ma matra check garxa.
        # dherai column filter garna ko lagi Q import garni natra euta matra vaye mathi kai.
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(student_email__icontains=search)|
            Q(student_age__icontains=search)
        )

    
    # rank paxi gara.
    
    # pagination ko code
    paginator = Paginator(queryset,10)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    # ya samma
    print(page_obj.object_list)


    # return render(request,'report/students.html',{'queryset':queryset})#folder banau report name ko and file banau students.html in templates.
    return render(request,'report/students.html',{'queryset':page_obj})#pagination agryo vani yesto garni.
    
    
# user le marks herni(19)
def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    print(total_marks)
    return render(request,'report/see_marks.html',{'queryset':queryset,'total_marks':total_marks})#pagination agryo vani yesto garni.
