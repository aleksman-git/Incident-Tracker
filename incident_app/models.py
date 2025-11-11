from django.db import models


class Incident(models.Model):

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(max_length=200, verbose_name='Описание')
    status = models.CharField(max_length=20, verbose_name='Статус')
    source = models.CharField(max_length=20, verbose_name='Источник')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        db_table = 'incident'
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'
        ordering = ['-created_at']


    def __str__(self):
        return self.title
