#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tester para validar responsividade mobile
Checklist de testes básicos
"""

# CHECKLIST DE TESTES MOBILE
# Execute esta lista antes de publicar

tests = {
    "Hero Section": {
        "mobile": [
            "✓ Texto principal tem 1.75rem+",
            "✓ Botões empilhados verticalmente",
            "✓ Lottie animation visível",
            "✓ SVG decorativos ocultos",
            "✓ Sem scroll horizontal"
        ],
        "tablet": [
            "✓ 2 colunas layout",
            "✓ Botões lado a lado",
            "✓ Tudo proporcional"
        ],
        "desktop": [
            "✓ 7-5 cols layout",
            "✓ Animações rodando",
            "✓ SVG backgrounds visíveis"
        ]
    },
    
    "Header/Navbar": {
        "mobile": [
            "✓ Logo responsive (40px)",
            "✓ Menu hamburger visível",
            "✓ Dark mode toggle presente",
            "✓ Height 56px"
        ],
        "desktop": [
            "✓ Logo grande (56px)",
            "✓ Menu horizontal",
            "✓ Hamburger oculto",
            "✓ Dark mode funcionando"
        ]
    },
    
    "Menu Drawer": {
        "mobile": [
            "✓ Abre ao clicar ☰",
            "✓ Backdrop semi-transparente",
            "✓ Links navegáveis",
            "✓ Fecha ao clicar fora",
            "✓ Fecha ao clicar em link",
            "✓ Sem scroll body enquanto aberto"
        ]
    },
    
    "Como Funciona": {
        "mobile": [
            "✓ Stack vertical (4 items)",
            "✓ Setas rotacionadas 90°",
            "✓ Descrições visíveis",
            "✓ Responsive font sizes"
        ],
        "desktop": [
            "✓ Layout horizontal",
            "✓ Setas 0°",
            "✓ Alinhadas no centro"
        ]
    },
    
    "Buttons": {
        "all": [
            "✓ Mínimo 44x44px (toque)",
            "✓ Padding: py-2 sm:py-3",
            "✓ Font size responsive",
            "✓ Click feedback",
            "✓ Sem hover em touch"
        ]
    },
    
    "Forms": {
        "mobile": [
            "✓ Full width inputs",
            "✓ Font size 16px+ (sem zoom)",
            "✓ Labels acima",
            "✓ Padding interno 12px+",
            "✓ Focus ring visível"
        ]
    },
    
    "Images": {
        "all": [
            "✓ max-w-full",
            "✓ height: auto",
            "✓ rounded-lg",
            "✓ Sem crop indesejado",
            "✓ Comprimidas (<500KB)"
        ]
    },
    
    "Performance": {
        "mobile": [
            "✓ SVG decorativos ocultados",
            "✓ Animações otimizadas",
            "✓ Sem jank/lag",
            "✓ Carrega em <3s em 4G"
        ]
    },
    
    "Accessibility": {
        "all": [
            "✓ Color contrast OK",
            "✓ Focus outline visível",
            "✓ Alt text em imagens",
            "✓ Semantic HTML",
            "✓ Links identificados"
        ]
    }
}

# PASSOS PARA TESTAR

print("""
╔══════════════════════════════════════════════════════════════════╗
║           TESTE DE RESPONSIVIDADE MOBILE - CHECKLIST             ║
╚══════════════════════════════════════════════════════════════════╝

PASSO 1: Abrir DevTools Chrome
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Pressione: F12 ou Ctrl+Shift+I
  2. Clique em "Toggle device toolbar" (Ctrl+Shift+M)
  3. Teste em:
     • iPhone 12 (390x844)
     • iPad (768x1024)
     • Desktop (1920x1080)

PASSO 2: Testar Dispositivos Reais
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Abrir em Safari (iPhone real)
  2. Abrir em Chrome (Android real)
  3. Testar em landscape/portrait
  4. Verificar touch targets (44x44px)

PASSO 3: Validações Chrome DevTools
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Lighthouse > Performance (objetivo: 90+)
  2. Lighthouse > Accessibility (objetivo: 90+)
  3. Console > sem erros vermelhos
  4. Network > compressão de imagens

PASSO 4: Testes Específicos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

""")

# Printando checklist por seção
for secao, testes_secao in tests.items():
    print(f"\n📋 {secao.upper()}")
    print("─" * 70)
    
    if isinstance(testes_secao, dict):
        for device, items in testes_secao.items():
            print(f"   {device.upper()}:")
            for item in items:
                print(f"   {item}")
    else:
        for item in testes_secao:
            print(f"   {item}")

print("""

RESUMO DO QUE FOI IMPLEMENTADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ CSS Responsivo (mobile-responsive.css)
   • Breakpoints: 320px, 480px, 768px, 1024px+
   • Touch friendly (44x44px min)
   • Dark mode support

✅ Header Responsivo (base.html)
   • Logo: h-10 mobile → h-14 desktop
   • Menu horizontal desktop
   • Menu hamburger + drawer mobile
   • Dark toggle em ambos

✅ Menu Drawer (components/mobile-menu.html)
   • Opens/closes com animation
   • Backdrop semi-transparente
   • Todos links funcionais

✅ Hero Section (components/hero.html)
   • 1 col mobile → 2 cols desktop
   • Textos escalados (3xl → 5xl)
   • Botões empilhados mobile
   • SVG ocultos (economiza dados)

✅ Como Funciona (home.html)
   • Stack vertical mobile
   • Horizontal desktop
   • Setas rotacionadas

✅ Documentação
   • MOBILE_RESPONSIVO.md (completo)
   • QUICK_START_RESPONSIVO.md (template)
   • RESUMO_IMPLEMENTACAO.md (overview)

PRÓXIMOS PASSOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Testar em iPhone/Android reais
2. Aplicar responsive nas outras páginas:
   • blog_list.html
   • blog_post.html
   • contact.html
   • solutions.html
   • why.html
   • for_who.html
   • process.html
   • about.html

3. Google PageSpeed Insights (objetivo: 90+)

4. Otimizar imagens (WebP, compressão)

5. Implementar lazy loading

6. PWA (Service Worker) - futuro


COMANDOS ÚTEIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Iniciar servidor local
python manage.py runserver

# Abrir em mobile (substituir IP)
http://<seu-ip>:8000

# Chrome DevTools
F12 ou Ctrl+Shift+I
Ctrl+Shift+M (toggle device)

# Performance
Google PageSpeed Insights (copie URL)
GTmetrix.com


PROBLEMAS COMUNS E SOLUÇÕES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ Texto muito pequeno em mobile
✅ Aumentar class: "text-base sm:text-lg"

❌ Imagem cortada
✅ Adicionar: "w-full h-auto max-w-full"

❌ Botão muito pequeno
✅ Adicionar: "min-h-[44px] min-w-[44px]"

❌ Scroll horizontal
✅ Verificar overflow hidden no pai

❌ Menu não fecha
✅ Verificar Alpine.js carregado


═══════════════════════════════════════════════════════════════════
                    BOM TESTE! 🚀
═══════════════════════════════════════════════════════════════════
""")
