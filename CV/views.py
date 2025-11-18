from django.shortcuts import render, redirect
from .forms import ContactForm
import markdown

def index(request):
    return render(request, 'index.html')

def analytics(request):
    return render(request, 'analytics.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aquí se podría añadir la lógica para enviar un correo electrónico
            return redirect('confirmation')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def proyectos(request):
    return render(request, 'proyectos.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def readme(request):
    with open('README.md', 'r') as f:
        readme_content = f.read()
    readme_html = markdown.markdown(readme_content)
    return render(request, 'readme.html', {'readme_html': readme_html})
