from django.contrib import admin
from .models import Quiz, Question, Answer


class AnswerInline(admin.TabularInline):
    fk_name = 'question'
    model = Answer
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [AnswerInline]
    list_display_links = ['id', 'title']
    search_fields = ['title']



admin.site.register(Quiz)

admin.site.register(Answer)


