from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "creates_at"]
    inlines = [ChoiceInline]


# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ["question", "choice_text", "votes"]
#     list_display_links = ["choice_text"]
