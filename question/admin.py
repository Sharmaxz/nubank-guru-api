from django.contrib import admin

from question.models import Answer, Level


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text',)


class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ('text', 'order', 'is_correct')
    extra = 0


class LevelAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    inlines = (AnswerInline,)


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Level, LevelAdmin)
