from django.contrib import admin

# Register your models here.

from .models import Book
from .models import Author
from .models import Address
from .models import Country

# set various settings
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)  # comment this if u want pre-populated field
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)  # filtering data
    list_display = ("author", "title",)  # display data


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)