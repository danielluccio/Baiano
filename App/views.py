from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from .models import Register
from .forms import RegisterForm

# Função de registro de usuário
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro realizado com sucesso!")
            return redirect('calendario')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Função para exibir o calendário e salvar registros diários
@login_required
def calendario(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.user = request.user
            registro.is_smok = form.cleaned_data['is_smok'] == 'true'  # Converte para booleano
            registro.save()
            messages.success(request, "Registro diário salvo com sucesso!")
            return redirect('calendario')
    else:
        form = RegisterForm()

    # Obtém os registros do usuário logado para exibir no calendário
    registros = Register.objects.filter(user=request.user)
    return render(request, 'calendario.html', {'form': form, 'registros': registros})


# Função para deletar um registro específico
@login_required
def deletar_registro(request, id):
    registro = get_object_or_404(Register, id=id, user=request.user)
    registro.delete()
    messages.success(request, "Registro excluído com sucesso!")
    return redirect('calendario')

# Função para deletar todos os registros do usuário
@login_required
def deletar_todos_registros(request):
    Register.objects.filter(user=request.user).delete()
    messages.success(request, "Todos os registros foram excluídos com sucesso!")
    return redirect('calendario')

# Função para obter os eventos do calendário no formato esperado pelo FullCalendar
@login_required
def calendar_events(request):
    registros = Register.objects.filter(user=request.user)

    events = []
    for registro in registros:
        events.append({
            'title': 'Usou Cigarro' if registro.is_smok else 'Não Usou Cigarro',
            'start': registro.date.strftime('%Y-%m-%d'),
            'is_smok': registro.is_smok,
        })

    return JsonResponse(events, safe=False)

# Função para registrar ou atualizar o uso de cigarro
@csrf_exempt
@login_required
def registrar_uso_cigarro(request):
    if request.method == 'POST':
        date = parse_date(request.POST.get('date'))
        is_smok = request.POST.get('is_smok') == 'true'

        Register.objects.update_or_create(
            user=request.user,
            date=date,
            defaults={'is_smok': is_smok},
        )

        return JsonResponse({'status': 'success'})

def confirmar_exclusao(request, id):
    registro = get_object_or_404(Register, id=id)
    if request.method == "POST":
        registro.delete()
        return redirect('calendario')  
    return render(request, 'confirmar_exclusao.html', {'registro': registro})
