from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page,name='Home'),
    path('addContact/',views.AddContact,name='addContactask'),
    path('addFeedback/',views.AddFeedback,name='addFeedback'),
    path('blogpost/<int:task_id>/',views.blogpost),
    path('about/',views.About,name='about'),
    path('appointment/',views.book_appointment,name="appointment"),
    path('medicine/',views.medi,name='medicine'),
    path('acknowledge/',views.Acknowledge,name='acknowledge'),
    path('doct/',views.Doct,name="doct")
]


