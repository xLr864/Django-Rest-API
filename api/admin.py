from django.contrib import admin
from .models import Review
# Register your models here.
@admin.register(Review)
class SudoReview(admin.ModelAdmin):
    list_display = ['id','title','ratting','verdict']