from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .models import Event, Ticket

# ۱. نمایش لیست رویدادها
class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

# ۲. نمایش بلیط‌های من
class MyTicketsView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'events/my_tickets.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

# ۳. عملیات رزرو بلیط
def book_ticket(request, event_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    event = get_object_or_404(Event, id=event_id)
    # ساخت بلیط
    Ticket.objects.create(user=request.user, event=event)
    return redirect('my_tickets')

# ۴. عملیات لغو بلیط
class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('my_tickets')
    
    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
