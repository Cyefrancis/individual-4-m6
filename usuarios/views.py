from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import Group
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():  # Asegura que la creación del usuario y perfil sean atómicas
                user = form.save()
                UserProfile.objects.create(user=user)  # Crea un perfil vacío al registrar
                try:
                    group = Group.objects.get(name='User')
                    user.groups.add(group)
                    messages.success(request, 'Registro exitoso. Bienvenido!')
                except ObjectDoesNotExist:
                    messages.warning(request, 'El grupo User no existe y no fue asignado.')
                return redirect(reverse('login'))
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = CustomUserCreationForm()

    for field in form:
        field.field.widget.attrs['class'] = 'form-control'
        if field.errors:
            field.field.widget.attrs['class'] += ' is-invalid'

    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = CustomUserCreationForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form })

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        messages.success(self.request, 'Inicio de sesión exitoso, Bienvenido(a)!')
        return reverse_lazy('home')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
@login_required
def home(request):
    return render(request, 'home.html')