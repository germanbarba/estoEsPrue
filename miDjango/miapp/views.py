from django.shortcuts import render,HttpResponse,redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages


# Create your views here.
layout="""
<h1>sitio web con Django -- GERMAN BARBOSA</h1>
<hr/>
<ul>
    <li>
       <a href="/inicio">Inicio</a>
    </li>
     <li>
       <a href="/hola-mundo">Hola Mundo</a>
    </li>
     <li>
       <a href="/pagina-pruebas">Pagina de Pruebas</a>
    </li>
     <li>
       <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>
"""
def index(request):
    """
    html=""
        <h1>Inicio</h1>
        <p>Años hasta el 2050</p>
        <ul>
    ""
    year=2021
    while year <=2060:
        if year % 2 ==0:
            html += f"<li>{str(year)}</li>"
         
        year += 1

    html +="</ul>"
    """
    year=2021
    hasta=range(year,2051)
    
    nombre='german barbosa'
    lenguajes=['javaScript','python','php','C']
    # lenguajes=[] 

    return render(request,'index.html',{
        'title':'Inicio desde Django con python',
        'mi_variable':'soy un dato que esta en la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'years':hasta})
    #return render(request,'index.html')

def prueba(request):
    return render(request,'prueba.html')
    
def pagina(request,redirigir=0):
   
    if redirigir==1:
        return redirect('/inicio/')

    return render(request,'pagina.html')


def contacto(request,nombre="",apellido=""):
    html=""
    if nombre and apellido:
        html+="<p>El nombre completo es: </p>"
        html+=f"<h3>{nombre} {apellido}<h3>"
    
    return HttpResponse(layout+f"<h2>Contacto </h2>"+html)


 
def hola_mundo(request):
    return render(request,'hola-mundo.html')

def crear_articulo(request,title,content,public):
    articulo=Article(
        title=title,
        content=content,
        public=public
    )
    articulo.save()
    return HttpResponse(f"articulo creado: <strong>{articulo.title}</strong>-{articulo.content}")

def save_article(request):
    if request.method=='POST':
        title=request.POST['title']
        if len(title)<=5:
            return HttpResponse("El titulo es muy pequeño")
        content=request.POST['content']
        public=request.POST['public']
        
        articulo=Article(
        title=title,
        content=content,
        public=public,
    )
        articulo.save()
        return HttpResponse(f"articulo creado: <strong>{articulo.title}</strong>-{articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")
    

def create_articles(request):
    return render(request,'create_article.html')

def create_full_article(request):
    
    if request.method=='POST':
        formulario=FormArticle(request.POST)
        if formulario.is_valid():
            data_form=formulario.cleaned_data
            
            title=data_form.get('title')
            content=data_form['content']
            public=data_form['public']
            
            articulo=Article(
               title=title,
               content=content,
               public=public
             
            )
        
            articulo.save()
            #crear mensaje flash (sesion que solo se muestra una vez)
            messages.success(request,f'has creado correctamente el articulo {articulo.id}')
        
            return redirect('articulos')
            
            
            #return HttpResponse(articulo.title + '' + articulo.content + '' +str(articulo.public))
        
    formulario=FormArticle()
    return render(request, 'create_full_article.html',{'form': formulario})

def articulo(request):
    try:
        articulo=Article.objects.get(title="segundo articulo",public=True)
        response=f"Articulo: <br/>{articulo.id} -{articulo.content}"
    except:
        response="<h1>Articulo no encontrado</h1>"
    return HttpResponse(response)

def editar_articulo(request, id):
    articulo=Article.objects.get(pk=id)
    articulo.title="Batman"
    articulo.content="pelicula del 2017"
    articulo.public=False
    
    articulo.save()
    return HttpResponse(f"articulo {articulo.id} modificado: <strong>{articulo.title}</strong>-{articulo.content}")
    
def articulos(request):
    """
    consultas con condiciones
    articulos=Article.objects.all()
    articulos=Article.objects.filter(id__gt=3)
    articulos=Article.objects.filter(id__gte=5)
    articulos=Article.objects.filter(title__contains="Articulo")
    articulos=Article.objects.filter(id__lt=5)
    articulos=Article.objects.filter(
        title="reloj de mano",
          public=False
    )
    """
    
    #consulta SQL desde dajango
    #articulos=Article.objects.raw("select * from miapp_article where title='primer articulo' and public=1")
    
    """
    articulos=Article.objects.filter(
        Q(title__contains="Bat")|Q(title__contains="calculadora")
  
    
    )
    """
    articulos=Article.objects.all().order_by('-id')
    
    
    return render(request,'articulos.html',{
        'articulos':articulos
    })
    
def borrar_articulo(request, id):
    articulo=Article.objects.get(pk=id)
    articulo.delete()
    
    return redirect('articulos')