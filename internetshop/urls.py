from django.contrib import admin
from django.urls import path
from products.views import MainView, ProductView, ProductDetailView, CategoryView, CreateProductView
from django.conf.urls.static import static
from internetshop.settings import MEDIA_URL, MEDIA_ROOT
from users.views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path('', MainView.as_view()),
    path('admin/', admin.site.urls),
    path('products/', ProductView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('products/create/', CreateProductView.as_view()),

    #users
    path('users/login/', LoginView.as_view()),
    path('users/logout/', LogoutView.as_view()),
    path('users/register/', RegisterView.as_view())
]

urlpatterns += static(MEDIA_URL, document_root= MEDIA_ROOT)