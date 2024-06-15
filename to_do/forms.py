from django import forms
from .models import Tarea, Category

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['title', 'description', 'deadline', 'state', 'category']  # Campos que queremos incluir en el formulario

        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),  # Widget para mostrar el campo fecha como un input de fecha
        }

    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all() 