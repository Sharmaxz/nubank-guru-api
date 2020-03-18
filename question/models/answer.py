from django.db import models


class Answer(models.Model):
    question = models.ForeignKey('question.Question', on_delete=models.CASCADE,
                              related_name='questions', verbose_name='Questão')
    text = models.CharField('resposta', max_length=140)
    order = models.PositiveIntegerField('ordem')
    is_correct = models.BooleanField('é a resposta certa?', default=False)

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"


