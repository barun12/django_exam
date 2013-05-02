from django.contrib import admin
from exam.models import UserDetail, Question

#for ordering in a specific way
#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']

#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3

#class PollAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    inlines = [ChoiceInline]
#    list_display = ('question', 'pub_date')

admin.site.register(UserDetail)
admin.site.register(Question)