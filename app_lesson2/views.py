from django.shortcuts import render, redirect
from .models import Client, Product, Order
from .forms import ClientForm

def index(request):

    return render(request, 'index.html')
# Представление для создания клиента
def create_client_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_clients')  
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

# Представление для отображения всех клиентов
def all_clients_view(request):
    clients = Client.objects.all()
    return render(request, 'all_clients.html', {'clients': clients})

# Представление для обновления клиента
def update_client_view(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('all_clients')  
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form, 'client': client})

# Представление для удаления клиента
def delete_client_view(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('all_clients') 
    return render(request, 'delete_client.html', {'client': client})
