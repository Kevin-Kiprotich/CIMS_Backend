from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.Homepage,name='Homepage'),
    path('login/', views.LoginView.as_view()),
    path('signup/',views.SignUpView.as_view()),
    path('report/',views.Report.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
