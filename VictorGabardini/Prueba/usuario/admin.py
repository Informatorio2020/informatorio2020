from django.contrib import admin

from usuario.models import Usuario, Producto
# Register your models here.

def delete(ModelAdmin, request, queryset):
	queryset.update(email='p')
	delete.short_description = "eliminame esto"

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'email')
	actions = [delete]

class ProductoAmdin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'precio')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto, ProductoAmdin)