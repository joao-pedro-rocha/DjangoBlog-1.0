from django.db import models
from django.contrib.auth.models import User # para usar a variavel author

# Para criar link clicável
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255) # limitando o titulo titulo a 255 caracteres
    slug = models.SlugField(max_length=255, unique=True) # url (www.meusite.com/blog/introcao-ao-django)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # id de autor e post /// precisa importar o user de django.contrib.auth.models
    body = models.TextField() # liberdade para o autor usar quantos caracteres quiser
    created = models.DateTimeField(auto_now_add=True) # adiciona adata e a hora em que o post foi publicado automaticamente 
    updated = models.DateTimeField(auto_now=True) # adiciona a data e a hora de atualizaçoẽs do post automaticamente
 
 # Classe para colocar os posts em ordem de
 # mais recente para mais antigo
    class Meta:
        ordering = ("-created",)
 
# Tira o "post object 1" e coloca o titulo do post na lista de posts na pagina de admin
    def __str__(self):
        return self.title
    
# Torna o título do post na lista de posts clicável
# !!! OBS !!!: É necessário usar o shell do django para definir a url exata de cada post
    def get_absolute_url(self):
        return reverse ('blog:detail', kwargs = {'slug': self.slug})
    