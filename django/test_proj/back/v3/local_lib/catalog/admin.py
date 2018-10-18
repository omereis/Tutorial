#
# a d m i n . p y
#

from django.contrib import admin

# Register your models here.
#------------------------------------------------------------------------------
from catalog.models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
#------------------------------------------------------------------------------
class BookInline(admin.TabularInline):
    model = Book
#------------------------------------------------------------------------------
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
#------------------------------------------------------------------------------
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
#------------------------------------------------------------------------------
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
#------------------------------------------------------------------------------
@admin.register(BookInstance)
class BookInstanceAdmin (admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'imprint', 'due_back', 'id')

    fieldsets = (
        ('Main',{
            'fields': ('book',)
        }),
        ('Identification', {
            'fields': ('imprint', 'id')
            #'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
#------------------------------------------------------------------------------
