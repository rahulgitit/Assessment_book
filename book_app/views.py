from django.shortcuts import render,redirect,HttpResponseRedirect
from book_app.forms import bookform
from book_app.models import Book
from book_app.models import Book
from book_app.serializers import BookSerializers,LoginSerializer,UserSignupSerialier
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
 

class SignupView(APIView):
    def post(self, request):
        serializers=UserSignupSerialier(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializers = LoginSerializer(data=request.data)
        if serializers.is_valid():
            username=serializers.validated_data["username"] # type: ignore
            password=serializers.validated_data["password"] # type: ignore
            user=authenticate(username=username,password=password)
            if user is not None:
                return Response({"message":"login successfully"},status=status.HTTP_200_OK)
            else:
                return Response({"message":"invalid username or password"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




class Bookdata(ModelViewSet):
    # permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    queryset=Book.objects.all()
    serializer_class=BookSerializers
    def get_permissions(self):
        if self.request.method in ['POST','PUT', 'DELETE']:
                self.permission_classes = [IsAuthenticated]
                
        return super().get_permissions()


# Create your views here.

def base(request):
    return render(request, "base.html")
def index(request):
    if request.method == "POST":
        form=bookform(request.POST)
        if form.is_valid():
            form.save()
            form=bookform()
    else:
        form=bookform()
    data=Book.objects.all()
    # return render(request,"index.html",{"form":form,"data":data})
    return render(request,"home.html",{"form":form,"data":data})
# 


def delete(request,id):
    if request.method == "POST":
        dt=Book.objects.get(pk=id)
        dt.delete()
        return redirect('/home')
def edit(request,id):
    if request.method =="POST":
        dt=Book.objects.get(pk=id)
        fm=bookform(request.POST, instance=dt)
        if fm.is_valid:
            fm.save()
            return redirect('/home')
    else:
        dt=Book.objects.get(pk=id)
        fm=bookform(instance=dt)
    return render(request,'update.html',{"fm":fm})

