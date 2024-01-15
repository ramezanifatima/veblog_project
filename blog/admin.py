from django.contrib import admin
from . import models

class FilterByTitle(admin.SimpleListFilter):
    title = "عنوان"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (

            ("django","جنگو"),
            ("html","اچ تی ام ال ")
        )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author", "show_image")
    list_filter = ("created", FilterByTitle)
    search_fields = ("title", )







admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Massage)
admin.site.register(models.Like)
