import json

from django.test import TestCase
from django.urls import reverse

from .models import Quiz


class QuizHomeViewTests(TestCase):
    def setUp(self):
        self.quiz = Quiz.objects.first()
        self.assertIsNotNone(self.quiz, "Quiz seed data should be available after migrations")

    def test_trang_chu_uses_template_and_payload(self):
        response = self.client.get(reverse("lam_bai_thi_trac_nghiem_lai_xe:trang_chu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lam_bai_thi_trac_nghiem_lai_xe/quiz.html")

        payload = json.loads(response.context["questions_json"])
        self.assertEqual(len(payload), self.quiz.questions.count())
        first_question = payload[0]
        self.assertIn("q", first_question)
        self.assertIn("choices", first_question)
        self.assertIn("correctIndex", first_question)
