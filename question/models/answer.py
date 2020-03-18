from django.db import models


class Answer(models.Model):
    level = models.ForeignKey('question.Level', on_delete=models.CASCADE,
                              related_name='answers', verbose_name='Respostas')
    text = models.CharField('resposta', max_length=140)
    order = models.PositiveIntegerField('ordem')
    is_correct = models.BooleanField('é a resposta certa?', default=False)

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"


