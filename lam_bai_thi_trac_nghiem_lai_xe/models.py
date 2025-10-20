from django.db import models


class Quiz(models.Model):
    """Đại diện cho một bài trắc nghiệm."""

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255, blank=True)
    badge_label = models.CharField(max_length=50, default="Trắc nghiệm")

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:  # pragma: no cover - biểu diễn đơn giản
        return self.title


class Question(models.Model):
    """Một câu hỏi trong bài trắc nghiệm."""

    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:  # pragma: no cover - biểu diễn đơn giản
        return f"{self.quiz.title} - Câu {self.order + 1}"


class AnswerOption(models.Model):
    """Lựa chọn trả lời cho một câu hỏi."""

    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:  # pragma: no cover - biểu diễn đơn giản
        prefix = "✔" if self.is_correct else "✘"
        return f"{prefix} {self.text}"
