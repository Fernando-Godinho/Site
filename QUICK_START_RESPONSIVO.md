# Quick Start - Implementar Responsividade Nas Páginas

## 🚀 Como Aplicar Rapidamente

Siga este padrão para cada página: **Blog, Soluções, Quem Somos, etc.**

---

## 📋 Template Básico Responsivo

```html
<!-- Título da página responsivo -->
<section class="py-8 sm:py-12 md:py-16 lg:py-20">
  <div class="container mx-auto lg:container px-4 sm:px-6">
    <h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold mb-4">
      Título da Página
    </h1>
    <p class="text-base sm:text-lg text-gray-600 max-w-2xl">
      Descrição breve responsiva
    </p>
  </div>
</section>
```

---

## 🔧 Aplicar Aos Componentes

### 1. **Blog List (blog_list.html)**

```html
<section class="py-8 sm:py-12">
  <div class="container mx-auto lg:container px-4">
    <h1 class="text-3xl sm:text-4xl font-bold mb-8">Blog</h1>
    
    <!-- Grid responsivo -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
      {% for post in posts %}
      <article class="card p-4 sm:p-6 rounded-lg">
        <h3 class="text-lg sm:text-xl font-semibold mb-2">{{ post.title }}</h3>
        <p class="text-sm sm:text-base text-gray-600 line-clamp-3">
          {{ post.excerpt }}
        </p>
        <a href="{{ post.get_absolute_url }}" class="text-sc-accent text-sm sm:text-base mt-4 inline-block">
          Leia mais →
        </a>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
```

---

### 2. **Blog Post (blog_post.html)**

```html
<article class="py-8 sm:py-12 md:py-16">
  <div class="container mx-auto lg:container px-4 max-w-3xl">
    <!-- Header do post -->
    <header class="mb-6 sm:mb-8">
      <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold mb-4">
        {{ post.title }}
      </h1>
      <div class="flex flex-col sm:flex-row gap-3 sm:gap-4 text-sm sm:text-base text-gray-600">
        <span>{{ post.author }}</span>
        <span>•</span>
        <span>{{ post.published_date|date:"d \\d\\e M \\d\\e Y" }}</span>
      </div>
    </header>

    <!-- Imagem hero -->
    {% if post.featured_image %}
    <img 
      src="{{ post.featured_image.url }}" 
      alt="{{ post.title }}"
      class="w-full h-auto rounded-lg mb-6 sm:mb-8 object-cover max-h-96"
    >
    {% endif %}

    <!-- Conteúdo -->
    <div class="prose prose-sm sm:prose md:prose-lg max-w-none">
      {{ post.content|safe }}
    </div>

    <!-- Tags -->
    {% if post.tags.all %}
    <div class="mt-8 flex flex-wrap gap-2">
      {% for tag in post.tags.all %}
      <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs sm:text-sm rounded-full">
        {{ tag }}
      </span>
      {% endfor %}
    </div>
    {% endif %}
  </div>
</article>
```

---

### 3. **Solutions (solutions.html)**

```html
<section class="py-8 sm:py-12 md:py-20">
  <div class="container mx-auto lg:container px-4">
    <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold text-center mb-8 sm:mb-12">
      Nossas Soluções
    </h1>

    <!-- Grid de soluções -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6 lg:gap-8">
      {% for solution in solutions %}
      <div class="card p-6 sm:p-8 rounded-lg text-center hover:shadow-lg transition">
        <div class="text-4xl sm:text-5xl mb-4">{{ solution.icon }}</div>
        <h3 class="text-lg sm:text-xl font-bold mb-3">{{ solution.title }}</h3>
        <p class="text-sm sm:text-base text-gray-600 mb-4">
          {{ solution.description }}
        </p>
        <a href="{{ solution.get_absolute_url }}" class="btn btn-outline text-sm sm:text-base">
          Saiba mais
        </a>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
```

---

### 4. **Contact Form (contact.html)**

```html
<section class="py-8 sm:py-12 md:py-20">
  <div class="container mx-auto lg:container px-4 max-w-2xl">
    <h1 class="text-3xl sm:text-4xl font-bold text-center mb-8">Fale Conosco</h1>

    <form method="POST" class="space-y-4 sm:space-y-6">
      {% csrf_token %}
      
      <!-- Campos lado a lado em desktop -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div class="form-group">
          <label for="name" class="block text-sm font-medium mb-2">Nome</label>
          <input 
            type="text" 
            id="name" 
            name="name" 
            class="w-full px-4 py-2 sm:py-3 border rounded-lg focus:outline-none focus:border-sc-accent"
            required
          >
        </div>
        <div class="form-group">
          <label for="email" class="block text-sm font-medium mb-2">Email</label>
          <input 
            type="email" 
            id="email" 
            name="email" 
            class="w-full px-4 py-2 sm:py-3 border rounded-lg focus:outline-none focus:border-sc-accent"
            required
          >
        </div>
      </div>

      <!-- Campo full width -->
      <div class="form-group">
        <label for="subject" class="block text-sm font-medium mb-2">Assunto</label>
        <input 
          type="text" 
          id="subject" 
          name="subject" 
          class="w-full px-4 py-2 sm:py-3 border rounded-lg focus:outline-none focus:border-sc-accent"
          required
        >
      </div>

      <!-- Textarea -->
      <div class="form-group">
        <label for="message" class="block text-sm font-medium mb-2">Mensagem</label>
        <textarea 
          id="message" 
          name="message" 
          rows="6"
          class="w-full px-4 py-2 sm:py-3 border rounded-lg focus:outline-none focus:border-sc-accent resize-vertical"
          required
        ></textarea>
      </div>

      <!-- Botão responsivo -->
      <button 
        type="submit" 
        class="btn btn-primary w-full sm:w-auto px-6 sm:px-8 py-2 sm:py-3 font-semibold"
      >
        Enviar Mensagem
      </button>
    </form>
  </div>
</section>
```

---

### 5. **About/Why (why.html, about.html)**

```html
<section class="py-8 sm:py-12 md:py-20">
  <div class="container mx-auto lg:container px-4">
    
    <!-- Alternando imagem e texto -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8 lg:gap-12 items-center mb-16">
      <div class="order-2 md:order-1">
        <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">
          Por Que Nos Escolher?
        </h2>
        <ul class="space-y-3 sm:space-y-4">
          <li class="flex gap-3">
            <span class="text-sc-accent text-xl flex-shrink-0">✓</span>
            <span class="text-sm sm:text-base">Benefício 1 com descrição breve</span>
          </li>
          <li class="flex gap-3">
            <span class="text-sc-accent text-xl flex-shrink-0">✓</span>
            <span class="text-sm sm:text-base">Benefício 2 com descrição breve</span>
          </li>
        </ul>
      </div>
      <div class="order-1 md:order-2">
        <img 
          src="/static/image.jpg" 
          alt="Por que nos escolher"
          class="w-full h-auto rounded-lg"
        >
      </div>
    </div>

    <!-- Segunda seção invertida -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8 lg:gap-12 items-center">
      <div>
        <img 
          src="/static/image2.jpg" 
          alt="Descrição"
          class="w-full h-auto rounded-lg"
        >
      </div>
      <div>
        <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">
          Nossa Experiência
        </h2>
        <p class="text-sm sm:text-base text-gray-600 mb-4">
          Texto descritivo...
        </p>
      </div>
    </div>
  </div>
</section>
```

---

## 📏 Classes Tailwind Mais Usadas

```html
<!-- Spacing responsivo -->
py-8 sm:py-12 md:py-16 lg:py-20    <!-- Padding vertical -->
px-4 sm:px-6 lg:px-8                <!-- Padding horizontal -->
gap-4 sm:gap-6 lg:gap-8             <!-- Gap entre elementos -->

<!-- Tipografia -->
text-lg sm:text-xl md:text-2xl lg:text-3xl
font-semibold sm:font-bold

<!-- Grid/Flex -->
grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 lg:grid-cols-4
flex flex-col sm:flex-row
space-y-4 sm:space-y-6

<!-- Display -->
hidden sm:block md:hidden lg:block
flex flex-col md:flex-row

<!-- Sizes -->
max-w-2xl max-w-4xl
w-full sm:w-auto

<!-- Visibility -->
order-1 md:order-2    <!-- Reordenar em mobile -->
```

---

## ✅ Checklist Antes de Publicar

- [ ] Testei em iPhone (375px)
- [ ] Testei em iPad (768px)
- [ ] Testei em Desktop (1920px)
- [ ] Botões têm 44x44px mínimo
- [ ] Textos legíveis (não menor que 16px)
- [ ] Sem scroll horizontal
- [ ] Imagens carregam rápido
- [ ] Links com cor/underline visíveis
- [ ] Modo dark funciona
- [ ] Formulários funcionam em mobile

---

## 🧪 Testar Responsividade Rápido

**Chrome DevTools:**
1. Pressione `F12`
2. Clique em "Toggle device toolbar" (`Ctrl+Shift+M`)
3. Teste tamanhos: 
   - iPhone 12 (390x844)
   - iPad (768x1024)
   - Desktop (1920x1080)

---

**Dúvidas? Consulte o arquivo `MOBILE_RESPONSIVO.md` para mais detalhes!**
