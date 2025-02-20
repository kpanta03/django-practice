# logical parts ya lekhni.
from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    # peoples lai uta pass gareko
    peoples=[
          {'name':'Kritika','age':21 },
          {'name':'krisha','age':17}
     ]
    for people in peoples:
          print(people)

    # text lai uta pass gareko
    text="""
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam asperiores iste natus optio explicabo saepe a quae, perferendis vel aspernatur maxime tempora deserunt in eius consequatur molestias tempore quibusdam odio rem minima quo officia. Excepturi, assumenda? Dolor earum, quos delectus qui necessitatibus non enim eligendi, deleniti ipsa voluptatem iste etc.
"""
    # vegetables list lai index.html ma pass gareko
    vegetables=["potato","tomato","cucumber"]
     

    
    return render(request,"index.html",context={'peoples':peoples,'text':text,'vegetables':vegetables,'page':'All about dyango'})
   

#     return HttpResponse("""
# <h1>Hey, I am django server</h1>
# <p>This is a paragraph</p>

# """)

# HttpResponse mai sabai kura lekhnu is not a good method. so yesko lagi template folder banayera teta html file haru rakhni and teslai render garni.

    
   
def about(request):
    context={'page':'About'}
    return render(request,"about.html",context)
def contact(request):
    context={'page':'Contact'}
    return render(request,"contact.html",context)

    


# Create your views here.
