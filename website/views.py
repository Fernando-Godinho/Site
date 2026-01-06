from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ContactRequest
import requests
import json


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def for_who(request):
    return render(request, 'website/for_who.html')


def solutions(request):
    return render(request, 'website/solutions.html')


def process_view(request):
    return render(request, 'website/process.html')


def why(request):
    return render(request, 'website/why.html')


def contact(request):
    if request.method == 'POST':
        # Coletar dados do formulário
        data = {
            'name': request.POST.get('name', ''),
            'company': request.POST.get('company', ''),
            'role': request.POST.get('role', ''),
            'employees_count': request.POST.get('employees_count') or None,
            'main_challenge': request.POST.get('main_challenge', ''),
            'whatsapp': request.POST.get('whatsapp', ''),
        }
        
        # Salvar no banco de dados
        ContactRequest.objects.create(**data)
        
        # Enviar para webhook n8n
        try:
            webhook_url = 'https://n8n.sumconnectia.tech/webhook/novoLead'
            response = requests.post(webhook_url, json=data, timeout=10)
            print(f"✅ Webhook enviado com sucesso! Status: {response.status_code}")
            print(f"Resposta: {response.text}")
        except requests.exceptions.Timeout:
            print(f"❌ Timeout ao enviar para webhook")
        except requests.exceptions.ConnectionError as e:
            print(f"❌ Erro de conexão ao webhook: {e}")
        except Exception as e:
            print(f"❌ Erro ao enviar para webhook: {e}")
        
        # Retornar JSON se for AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Contato enviado com sucesso!'})
        return redirect('contact')
    return render(request, 'website/contact.html')


def blog_list(request):
    posts = [
        {'title': 'Quanto custa não automatizar processos administrativos?', 'slug': 'custo-nao-automatizar'},
        {'title': 'Automação não é software: é estratégia', 'slug': 'automatizacao-estrategia'},
        {'title': 'Planilhas não escalam', 'slug': 'planilhas-nao-escalam'},
    ]
    return render(request, 'website/blog_list.html', {'posts': posts})


def blog_post(request, slug):
    sample_posts = {
        'custo-nao-automatizar': 'Conteúdo sobre custos de não automatizar.',
        'automatizacao-estrategia': 'Conteúdo sobre visão estratégica da automação.',
        'planilhas-nao-escalam': 'Conteúdo sobre limitações de planilhas.',
    }
    title = next((p['title'] for p in [
        {'title': 'Quanto custa não automatizar processos administrativos?', 'slug': 'custo-nao-automatizar'},
        {'title': 'Automação não é software: é estratégia', 'slug': 'automatizacao-estrategia'},
        {'title': 'Planilhas não escalam', 'slug': 'planilhas-nao-escalam'},
    ] if p['slug'] == slug), 'Post')
    content = sample_posts.get(slug, 'Conteúdo em desenvolvimento.')
    return render(request, 'website/blog_post.html', {'title': title, 'content': content})
