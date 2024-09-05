from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"bookdata", views.Bookdata)

urlpatterns = [
    path("api/", include(router.urls)),
    
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),

    path("home/", views.index, name="index"),
    path("base/", views.base, name= "base"),
    path("delete/<int:id>/", views.delete,name="delete"), # type: ignore
    path("edit/<int:id>/", views.edit,name="edit"),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    
    
]
