from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100, help_text='username аккаунта')
    # имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=7, decimal_places=2)
    # баланс(DecimalField)
    age = models.IntegerField()
    # возраст
    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    # название игры
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    # цена(DecimalField)
    size = models.DecimalField(max_digits=7, decimal_places=3)
    # размер файлов игры(DecimalField)
    description = models.TextField()
    # описание(неограниченное кол - во текста)
    age_limited = models.BooleanField(default=False)
    # ограничение возраста 18 + (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, related_name='username')
    # покупатель обладающий игрой(ManyToManyField).У каждого покупателя может
    # быть игра и у каждой игры может быть несколько обладателей.
    # DecimalField - поле для дробных чисел.
    # BooleanField - поле для булевых значений.
    def __str__(self):
        return self.title

### Game.objects.get(id=1).buyer.set((first_buyer, second_buyer))
### Game.objects.get(id=3).buyer.set((2, 3))