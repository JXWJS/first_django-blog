from django.contrib import admin

from django.urls import path,include
import password_reset.urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('article/',include('article.urls',namespace='article')),
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('password-reset/',include('password_reset.urls')),
    path('comment/',include('comment.urls',namespace='comment')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)