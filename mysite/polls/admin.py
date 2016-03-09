from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3
#lista para crear, extra cantidad de formularios 

class QuestionModelAdmin(admin.ModelAdmin):	
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
	inlines = [ChoiceInline]
#class collapse esconde el panel

class ChoiceModelAdmin(admin.ModelAdmin):	
	class Meta:
		model = Choice

		
admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice, ChoiceModelAdmin)

