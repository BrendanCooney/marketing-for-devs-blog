from django.contrib import admin
from .models import Tools, Rating
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Tools)
class ToolsAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.header}: {self.average_rating()}"