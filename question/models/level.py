from django.db import models

LEVEL = (('apprentice', 'aprendiz'),
         ('conscious', 'consciente'),
         ('saver', 'poupador'),
         ('investor', 'Investidor'),
         ('master', 'investidor mestre'),
         )


class Level(models.Model):
    title = models.CharField('título', max_length=30, null=True, blank=True)
    level = models.CharField('nível', choices=LEVEL, max_length=20)
    position = models.PositiveIntegerField('número da fase', null=True, blank=True)
    content = models.CharField('descrição', max_length=255, null=True, blank=True)

    questions = models.ManyToManyField('question.Question', null=True, blank=True)

    class Meta:
        verbose_name = 'Fase'
        verbose_name_plural = 'Fases'

    def __str__(self):
        return f'{self.level} - {self.position}'
