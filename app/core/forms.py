from core.erp.models import Category

from django.forms import *


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for form in self.visible_fields():
          #  form.field.widget.attrs['class'] = 'form-control'
           # form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True


    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Nombre'
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripcion',
                    'autocomplete': 'off',
                    'rows': 3,
                    'cols': 3
                }
            )
        }
