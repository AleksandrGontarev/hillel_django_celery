from django.contrib import admin

from reminder.models import Author, Quotes


class QuotesInline(admin.StackedInline):
    model = Quotes
    extra = 1


@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('text', 'authors')
    list_filter = ['text', 'authors']
    search_fields = ['text', 'authors']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',  'description')
    list_filter = ['name', ]
    search_fields = ['name', ]
    inlines = [QuotesInline, ]
