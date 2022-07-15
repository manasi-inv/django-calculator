from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "input.html")



def addition(request):

    num1= request.POST['num1']
    num2= request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a= int(num1)
        b=int(num2)
        result=a+b
       
    else:
        result= "only digits are allowed"

    return render(request, "result.html", {"result":result})



def subtraction(request):

    num1= request.POST['num1']
    num2= request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a= int(num1)
        b=int(num2)
        result=a-b
       
    else:
        result= "only digits are allowed"

    return render(request, "result.html", {"result":result})



def multiplication(request):

    num1= request.POST['num1']
    num2= request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a= int(num1)
        b=int(num2)
        result=a*b
       
    else:
        result= "only digits are allowed"

    return render(request, "result.html", {"result":result})



def division(request):

    num1= request.POST['num1']
    num2= request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a= int(num1)
        b=int(num2)

        if b==0:
            result = "zero divide error"
        else:
            result=a/b         
               
    else:
        result= "only digits are allowed"

    return render(request, "result.html", {"result":result})


    






