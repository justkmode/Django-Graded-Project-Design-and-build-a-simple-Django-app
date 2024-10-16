from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_items = Menu.objects.all().order_by('name')  # Ordering by 'name'
    context = {'menu': menu_items}
    return render(request, 'menu.html', context)

def contact(request):
    # Logic for handling contact form could go here
    return render(request, 'contact.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # Redirect to a success page
    context = {'form': form}
    return render(request, 'book.html', context)

def success(request):
    return render(request, 'success.html')  # Create a success.html template

def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = None
    
    return render(request, 'menu_item.html', {'menu_item': menu_item})
