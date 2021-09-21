from django.contrib import admin

# Importar a classe Post que criei
from .models import Post

# Register your models here.
@admin.register(Post) # adiciona na pagina de admin uma sessão chamada post para criar um post na pagina de admin

# Organizar tela de posts
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    
# Preencher o slug junto com o title
    prepopulated_fields = {'slug': ('title',)}
