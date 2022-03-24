from django.contrib import admin
from .models import Lead, Remark
# Register your models here.

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email','status','assigned_to','public')
    list_per_page = 10
    search_fields = ('assigned_to',)
    list_filter = ('status',)


@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    list_display = ('id','created_at','remark','lead_id')