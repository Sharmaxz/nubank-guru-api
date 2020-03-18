from django.db import models

LEVEL = (('apprentice', 'aprendiz'),
         ('conscious', 'consciente'),
         ('saver', 'poupador'),
         ('investor', 'Investidor'),
         ('master', 'investidor mestre'),
         )


class Level(models.Model):
    level = models.CharField('nível', choices=LEVEL, max_length=20)
    number = models.PositiveIntegerField('número')
    question_number = models.PositiveIntegerField('número de questões')
    description = models.CharField('descrição', max_length=200)

    class Meta:
        verbose_name = 'Fase'
        verbose_name_plural = 'Fases'

    def __str__(self):
        return f'{self.level} - {self.question_number}'
