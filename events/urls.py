from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('my-tickets/', views.MyTicketsView.as_view(), name='my_tickets'),
    path('book/<int:event_id>/', views.book_ticket, name='book_ticket'),
    path('cancel/<int:pk>/', views.TicketDeleteView.as_view(), name='cancel_ticket'),
]
