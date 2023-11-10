from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.get_all_results, name='all_results'),
    path('polling_unit/<str:polling_unit_uniqueid>/', views.get_polling_unit_results, name='polling_unit_results'),
    # path('result-entry/', views.result_entry, name='result_entry'),
    # path('success-page/', views.success_page, name='success_page'),
    path('local_government_result/', views.local_government_result, name='local_government_result'),
    # path('success-page/<str:selected_parties>/', views.success_page, name='success_page'),
    path('add_results/<int:polling_unit_id>/', views.AddResultsView.as_view(), name='add_results'),
]

