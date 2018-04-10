from django.contrib import admin
from.models import author,catagory,article

# Register your models here.

class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        model=author
admin.site.register(author)
class articleModel(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","details"]
    list_per_page = 10
    list_filter = ["posted_on","catagory"]
    class Meta:
        model=article
admin.site.register(article, articleModel)
class catagoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        model=catagory
admin.site.register(catagory,catagoryModel)

