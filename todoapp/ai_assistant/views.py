from django.shortcuts import render
from django.http import JsonResponse


def get_ai_response(message: str) -> str:
    message = message.lower().strip()

    # DEBUG (очень важно)
    print("USER MESSAGE:", message)

    # ================= TASKS =================
    if "задач" in message or "todo" in message:
        return "Ты можешь создавать задачи в разделе ToDo на сайте."

    if "добав" in message and "задач" in message:
        return "Чтобы добавить задачу, нажми кнопку 'Добавить задачу' в ToDo разделе."

    if "удал" in message and "задач" in message:
        return "Удаление задачи происходит через кнопку удаления рядом с задачей."

    # ================= FEEDBACK =================
    if "feedback" in message or "обрат" in message:
        return "Обратная связь позволяет отправить сообщение администратору."

    # ================= REVIEWS =================
    if "отзыв" in message:
        return "Отзывы можно оставить в разделе Reviews на сайте."

    # ================= DEFAULT =================
    return "Я могу помочь только с задачами, отзывами и обратной связью."


def ai_chat(request):
    if request.method == "POST":
        message = request.POST.get("message", "")

        answer = get_ai_response(message)

        return JsonResponse({"answer": answer})

    return render(request, "ai_assistant/chat.html")