from django.contrib import admin

from .models import Question, Choice

class QuestionModelAdmin(admin.ModelAdmin):	
	class Meta:
		model = Question

class ChoiceModelAdmin(admin.ModelAdmin):	
	class Meta:
		model = Choice
		
admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice, ChoiceModelAdmin)

