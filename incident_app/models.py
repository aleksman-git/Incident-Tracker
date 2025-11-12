from django.db import models


class Incident(models.Model):

    status_new = 'new'
    status_in_progress = 'in_progress'
    status_resolved = 'resolved'
    status_closed = 'closed'
    # вменяемый набор статусов инцидента
    status_choices = [
        (status_new, 'Новый'),
        (status_in_progress, 'В работе'),
        (status_resolved, 'Решен'),
        (status_closed, 'Закрыт'),
    ]
    # автоинкрементный первичный ключ инцидента
    incident_id = models.BigAutoField(primary_key=True, verbose_name='ID инцидента')
    # описание инцидента
    description = models.TextField(verbose_name='Описание')
    # статус инцидента с выбором из набора
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default=status_new,
        verbose_name='Статус')
    # источник инцидента
    source = models.CharField(max_length=20, verbose_name='Источник')
    # автоматическая дата и время создания
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    # настройки метаданных модели
    class Meta:
        db_table = 'incident'
        verbose_name = 'incident'
        verbose_name_plural = 'incidents'

    def __str__(self):
        return f"#{self.incident_id}: {self.description[:40]}"
