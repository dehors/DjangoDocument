from django.contrib import admin

from .models import Question, Choice

class QuestionModelAdmin(admin.ModelAdmin):	
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
    ]

class ChoiceModelAdmin(admin.ModelAdmin):	
	class Meta:
		model = Choice
		
admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice, ChoiceModelAdmin)

