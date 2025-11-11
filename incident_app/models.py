from django.db import models


class Incident(models.Model):
    status_new = 'new'
    status_in_progress = 'in_progress'
    status_resolved = 'resolved'
    status_closed = 'closed'

    status_choices = [
        (status_new, 'Новый'),
        (status_in_progress, 'В работе'),
        (status_resolved, 'Решен'),
        (status_closed, 'Закрыт'),
    ]

    incident_id = models.BigIntegerField(verbose_name='ID инцидента', primary_key=True)
    description = models.TextField(max_length=200, verbose_name='Описание')
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default=status_new,
        verbose_name='Статус')
    source = models.CharField(max_length=20, verbose_name='Источник')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        db_table = 'incident'
        verbose_name = 'incident'
        verbose_name_plural = 'incidents'
        ordering = ['-created_at']

    def __str__(self):
        return self.title



