from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Complexity(models.Model):
    complexity_name = models.CharField(max_length=30, verbose_name='Уровень сложности')

    class Meta:
        verbose_name = 'Сложность'
        verbose_name_plural = 'Сложности'

    def __str__(self):
        return self.complexity_name


class Types_of_training(models.Model):
    types_training_name = models.CharField(max_length=30, verbose_name='Тип тренировки')

    class Meta:
        verbose_name = 'Вид тренировки'
        verbose_name_plural = 'Виды тренировок'

    def __str__(self):
        return self.types_training_name


class Training(models.Model):
    training_name = models.CharField(max_length=30, verbose_name='Название тренировки')
    types_training_name = models.ForeignKey(Types_of_training, on_delete=models.CASCADE, verbose_name='Тип тренировки')
    complexity_name = models.ForeignKey(Complexity, on_delete=models.CASCADE, verbose_name='Сложность')

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    def __str__(self):
        return self.training_name


class Trainer(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    image = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Фото')
    sername = models.CharField(max_length=30, verbose_name='Фамилия')
    lastname = models.CharField(max_length=30, verbose_name='Отчество', blank=True)
    date_of_employment = models.DateTimeField(auto_now_add=True, verbose_name='Дата устройства')
    types_training_name = models.ForeignKey(Types_of_training, on_delete=models.CASCADE, verbose_name='Виды тренировок')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'

    def __str__(self):
        return self.name


class Horse(models.Model):
    horse_name = models.CharField(max_length=30, verbose_name='Имя')
    horse_img = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Фото')
    breed = models.CharField(max_length=30, verbose_name='Порода')
    status = models.CharField(max_length=50, verbose_name='Статус')
    birthday = models.DateTimeField(auto_now_add=True, verbose_name='День рождения')
    trainer = models.ManyToManyField(Trainer, verbose_name='Тренер')

    class Meta:
        ordering = ('horse_name',)
        verbose_name = 'Лошадь'
        verbose_name_plural = 'Лошади'

    def __str__(self):
        return self.horse_name


class Route(models.Model):
    route_name = models.CharField(max_length=30, verbose_name='Название')
    length = models.CharField(max_length=50, verbose_name='Протяжённость')
    complexity_name = models.ForeignKey(Complexity, on_delete=models.CASCADE, verbose_name='Сложность')
    description = models.TextField(max_length=250, verbose_name='Описание')

    class Meta:
        ordering = ('length',)
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return self.route_name


class Services(models.Model):
    service_name = models.CharField(max_length=30, verbose_name='Наименование')
    service_img = models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Фото')
    service_sell = models.IntegerField(verbose_name='Цена')
    sale = models.IntegerField('Скидка в процентах', blank=True, null=True, default=0)
    horse = models.ManyToManyField(Horse, verbose_name='Порода', blank=True, symmetrical=False)
    trainer = models.ManyToManyField(Trainer, verbose_name='Тренер', blank=True, symmetrical=False)
    training = models.ForeignKey(Training, on_delete=models.CASCADE, verbose_name='Тренировки')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Описание')

    def get_trainer(self):
        return ", ".join([str(p) for p in self.trainer.all()])

    def get_horse(self):
        return ", ".join([str(p) for p in self.horse.all()])

    class Meta:
        ordering = ('service_name',)
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    @property
    def sell(self):
        return int(self.service_sell * (100 - self.sale) / 100)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга')
    text = models.TextField(blank=False, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date', ]

    def __str__(self):
        return '{}'.format(self.user)


class Order(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_start = models.DateTimeField(auto_now_add=False, verbose_name='Дата заезда')
    date_of_create = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')
    trainer = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, verbose_name='Тренер', related_name='order_trainer')
    horse = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, verbose_name='Лошадь', related_name='order_horse')

    class Meta:
        ordering = ('-date_of_create',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
