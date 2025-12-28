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

Design & Visual Guidance
-----------------------

Paleta principal:
- Preto técnico: #0F172A
- Cinza carvão: #1E293B
- Cinza claro (background): #F8FAFC
- Cinza médio: #CBD5E1
- Azul estratégico (accent): #2563EB

Tipografia:
- Família: `Inter` (Google Fonts) para títulos e textos.
- Pesos: 400, 500, 600, 700, 800.

Ícones:
- Biblioteca: Lucide (inclusa via CDN).
- Estilo: stroke/outline; monocromático com `--sc-accent` para destaque.

Imagens:
- Evitar fotos genéricas de pessoas; preferir ilustrações abstratas, mockups de dashboards, gráficos estilizados e 3D abstrato.
- Fontes recomendadas: ls.graphics, Figma Community, UI8, DrawKit, Storyset e Unsplash (apenas abstratas/arquitetura/tech).

Motion & Interações:
- Parallax leve no hero (5–10% deslocamento) — reduzido em mobile e quando `prefers-reduced-motion` está ativo.
- Microinterações: hover em cards (elevação + sombra), transições suaves em CTAs e entrada ao scroll via Intersection Observer/Alpine.

Onde estão as implementações:
- `templates/website/base.html` — inclui as definições de fonte, extensão do tema Tailwind (cores e fontFamily), Lucide e microinteractions simples via Alpine/JS.

Próximos passos de design:
- Substituir backgrounds temporários por assets abstratos de alta qualidade.
- Gerar tokens do design (variáveis CSS + arquivo de referência) para consumo no frontend.
- Integrar pipeline de build do Tailwind para produção (opcional).
