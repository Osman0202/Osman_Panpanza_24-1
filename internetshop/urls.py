from django.contrib import admin
from django.urls import path
from products.views import main, product_view,product_detail_view,categories_view,create_product_view
from django.conf.urls.static import static
from internetshop.settings import MEDIA_URL,MEDIA_ROOT



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main),
    path('products/', product_view),
    path('products/<int:id>/', product_detail_view),
    path('categories/', categories_view),
    path('products/create/', create_product_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)