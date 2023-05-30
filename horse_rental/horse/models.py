from django.db import models


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
    sername = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Тренер')

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
    service_sell = models.CharField(max_length=50, verbose_name='Цена')
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, verbose_name='Порода')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Тренер')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, verbose_name='Тренировки')
    description = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Описание')

    class Meta:
        ordering = ('service_name',)
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.service_name
