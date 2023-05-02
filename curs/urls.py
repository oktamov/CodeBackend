from django.conf.urls.static import static
from django.urls import path

from courses import settings
from curs.views import BaseCategoryListView, BaseCategoryDetail
from curs.views.category import CategoryListView

urlpatterns = [
    path('', BaseCategoryListView.as_view(), name='base_list'),
    path('<slug:slug>/', BaseCategoryDetail.as_view(), name='base_detail'),
    path('courses/Backend/', CategoryListView.as_view(), name='category_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
