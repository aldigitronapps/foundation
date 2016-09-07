from django.contrib import admin
from .models import Chapter, supChapter

class supChapterInline(admin.TabularInline):
	model = supChapter
	

class ChapterAdmin (admin.ModelAdmin):
	# fieldsets = [
	# (None, {'fields': ['question_text']}), 
	# ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']}),
	# ]
	inlines = [supChapterInline]
	list_display = ('heading', 'date_completed',)
	list_filter = ['heading', 'date_completed']
	# search_fields = ['question_text']


admin.site.register(Chapter, ChapterAdmin)
