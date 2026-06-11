from django.contrib import admin
from .models import Feedback, Review


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'created_at'
    )

    search_fields = (
        'name',
        'email',
        'subject'
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'rating',
        'is_published',
        'created_at'
    )

    list_filter = (
        'rating',
        'is_published'
    )

    search_fields = (
        'author',
    )