from django import forms
from .models import Tarea, Category, Etiqueta

class TareaForm(forms.ModelForm):
    # Campos adicionales para filtros
    title_contains = forms.CharField(label='Título contiene', required=False)
    state = forms.ChoiceField(
        label='Estado',
        choices=[('', 'Todos')] + Tarea.STATE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Categoría',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    deadline_before = forms.DateField(
        label='Fecha límite antes de',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    # Campo para seleccionar etiquetas
    etiquetas = forms.ModelMultipleChoiceField(
        queryset=Etiqueta.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Etiquetas'
    )

    class Meta:
        model = Tarea
        fields = ['title', 'description', 'deadline', 'state', 'category', 'etiquetas']  # Campos del modelo Tarea que queremos incluir en el formulario
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['etiquetas'].queryset = Etiqueta.objects.all()