from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from hikers_haven import views


#the paths to URLs that will conenct to the user sign-up and sign-in links

urlpatterns = [
    path('user/signup/', views.UserCreate.as_view(), name="create_user"),
    #path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]