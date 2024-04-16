from django.db import models
from django.utils import timezone

class AdTitle(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
         return self.text
     
class Ad(models.Model):
    title = models.ForeignKey(AdTitle, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описання')
    price = models.CharField(max_length=200, verbose_name='Ціна')
    image = models.ImageField(upload_to='ads/%Y/%m/%d', blank=True)
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публікації')
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('sold', 'Продано'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name='Статус')

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
         return f"{self.description[:50]}..."