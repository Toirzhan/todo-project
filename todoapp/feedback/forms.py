from django import forms
from .models import Feedback, Review


# =========================
# ОБРАТНАЯ СВЯЗЬ
# =========================
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']


# =========================
# ОТЗЫВЫ
# =========================
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating', 'text']