from django.db import models


class Question(models.Model):
    title = models.CharField('título', max_length=30, blank=True)
    position = models.PositiveIntegerField('número da questão')
    text = models.CharField('texto da questão', max_length=200)

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'

    def __str__(self):
        return f'{self.title} - {self.position}'
