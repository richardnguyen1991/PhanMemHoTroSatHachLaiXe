import json

from django.http import Http404
from django.shortcuts import render

from .models import Quiz


def trang_chu(request):
    """Hiển thị bài thi trắc nghiệm lấy dữ liệu từ cơ sở dữ liệu."""

    quiz = (
        Quiz.objects.prefetch_related("questions__options")
        .order_by("id")
        .first()
    )
    if quiz is None:
        raise Http404("Không tìm thấy bài trắc nghiệm nào.")

    questions_payload = []
    for question in quiz.questions.all():
        options = list(question.options.all())
        questions_payload.append(
            {
                "q": question.text,
                "choices": [option.text for option in options],
                "correctIndex": next(
                    (idx for idx, option in enumerate(options) if option.is_correct),
                    None,
                ),
            }
        )

    context = {
        "quiz": quiz,
        "questions_json": json.dumps(questions_payload, ensure_ascii=False),
    }
    return render(request, "lam_bai_thi_trac_nghiem_lai_xe/quiz.html", context)
