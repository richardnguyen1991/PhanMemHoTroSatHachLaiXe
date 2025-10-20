from django.contrib import admin

from .models import AnswerOption, Question, Quiz


class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerOptionInline]
    list_display = ("quiz", "order", "text")
    list_filter = ("quiz",)
    ordering = ("quiz", "order")


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")


admin.site.register(Question, QuestionAdmin)
