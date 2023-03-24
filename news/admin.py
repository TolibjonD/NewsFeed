from django.contrib import admin
from .models import News, Category, Contact

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "published_time", "status"]
    date_hierarchy = "published_time"
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Contact)
