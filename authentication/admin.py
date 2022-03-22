from django.contrib import admin
from .models import Lead, Remark
# Register your models here.

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','password','status','assigned_to')


@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    list_display = ('id','created_at','remark','lead_id')