from django.urls import path
from tracking.views import CategoryList, CategoryDetail, SpendingList, SpendingDetail

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('spending/', SpendingList.as_view()),
    path('spending/<int:pk>/', SpendingDetail.as_view()),

]

