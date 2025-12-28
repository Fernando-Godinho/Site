Sum Connect — Projeto inicial

Setup rápido (Windows):

1. Criar virtualenv e ativar

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Rodar migrações e servidor

```powershell
python manage.py migrate
python manage.py runserver
```

Observações:
- Tailwind, DaisyUI e Alpine.js estão incluídos via CDN no `base.html` para protótipo rápido.
- Substitua `SECRET_KEY` em `sumconnect/settings.py` para produção.
