from django.contrib import admin

from reportsPage.models import Feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('tour', 'username', 'text', 'time',)
    list_filter = ('tour', 'time',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)



