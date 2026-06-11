from django.shortcuts import render
from django.http import JsonResponse

from .forms import FeedbackForm, ReviewForm
from .models import Review


# =========================
# ОБРАТНАЯ СВЯЗЬ (оставляем как есть)
# =========================
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback/success.html')
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})


# =========================
# ОТЗЫВЫ (AJAX версия)
# =========================
def reviews_view(request):
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')

    # AJAX отправка отзыва
    if request.method == "POST":
        author = request.POST.get("author")
        rating = request.POST.get("rating")
        text = request.POST.get("text")

        # защита от пустых данных
        if not author or not rating or not text:
            return JsonResponse({
                "status": "error",
                "message": "Заполните все поля"
            })

        Review.objects.create(
            author=author,
            rating=int(rating),
            text=text,
            is_published=False
        )

        return JsonResponse({
            "status": "ok"
        })

    return render(request, 'feedback/reviews.html', {
        'reviews': reviews
    })