from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title=forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete el titulo',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ]*$','El titulo no cumple con la validacion','invalid_title')
        ]
        
    )
    
    content=forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(100,'Te has pasado has puesto mucho texto')
        ]
        
        )   
    
    
    content.widget.attrs.update({
        'placeholder':'Mete el contenido YAA',
        'class':'contenido_form_article dos',
        'id':'contenido_form'
    })
    
    public_option=[
        (1,'Si'),
        (0,'No')
    ]
    
    public=forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_option
    )