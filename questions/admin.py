from django.contrib import admin

from questions.models import Question, Comment

class CommentInline(admin.TabularInline):
	model = Comment
	extra = 0
# Allows the Question data to be edited in Djangos admin
class QuestionAdmin(admin.ModelAdmin):
	# Defines the visable im the Django Admin
	fieldsets = [
		('Discussion', 		{'fields': ['question']}),
		('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	# Displays the Comment Model as apart of the Questions datasets
	inlines = [CommentInline]
	list_display = ('question', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
