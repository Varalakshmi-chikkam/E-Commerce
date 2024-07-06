from django.shortcuts import render
from django.http import HttpResponse
from .product import Product
from .category import Category
from django.contrib.auth.hashers import make_password
from .customer import Customer
# Create your views here.
def home(request):
    
    categories=Category.objects.all()
    categoryID=request.GET.get('category')
    if categoryID:
        products=Product.get_category_id(categoryID)
    
    else:
        products=Product.objects.all()
    data={'products':products, 'categories':categories}
    return render(request, "index.html", data)

#signup form
def signup(request):
    if request.method=='GET':
       
       return render(request,"signup.html")
    else:
       fn=request.POST['fn']
       ln=request.POST['ln']
       email=request.POST['email']
       mobile=request.POST['mobile']
       password=request.POST['password']
       password=make_password(password)
       userdata=[fn,ln,email,mobile,password]
       print(userdata)
       uservalues={
           'fn':fn,
           'ln':ln,
           'email':email,
       }

       #storing object
       customerdata=Customer(first_name=fn, last_name=ln, email=email, mobile=mobile, password=password)

       #validation
       error_msg=None
       success_msg=None
       if(not fn):
           error_msg="first name not found"
       elif(not ln):
           error_msg="last name not found"
       elif(not email):
           error_msg="email not found"
       elif(not mobile):
           error_msg="mobile number not found"
       elif(not password):
           error_msg="password not found"  
       elif(customerdata.isexit()):
           error_msg="Email already exist:enter valid email id"
      
       if(not error_msg):
           success_msg="Account created successfully"
           customerdata.save()
           msg={'success':success_msg}
           return render(request,'signup.html',msg)
       else:
           msg={'error':error_msg, 'value':uservalues}
           return render(request,'signup.html',msg)