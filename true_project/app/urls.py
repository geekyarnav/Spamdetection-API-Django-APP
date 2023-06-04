from django.urls import path,include
from app import views

# API_VERSION="v1"

urlpatterns = [
    path('v1/user/login/', views.Login_List.as_view()),
    path('v1/user/signup/', views.Signup_List.as_view()),
    path('v1/contact/<int:user_id>/',views.Contact_Info_List.as_view()),
    path('v1/search_name/', views.Search_Name.as_view()),
    path('v1/search_phone/', views.Search_Phone.as_view()),
 ]