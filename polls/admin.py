from django.contrib import admin
from .models import Question,Choice

# Register your models here.
class ChoiceIncline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pub_date','question_text')
    fields = ['pub_date','question_text']
    inlines = [ChoiceIncline]

admin.site.register(Question,QuestionAdmin)
