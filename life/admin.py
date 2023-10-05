from django.contrib import admin

from .models import DiaryModel

class DiaryModel(admin.ModelAdmin):
  list_display = "__all__"

admin.site.register(DiaryModel, DiaryModel)
