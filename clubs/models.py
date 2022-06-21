from django.db import models


# Create your models here.
from django.db.models import TimeField


class Attribute(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'Аттрибут "{self.name}"'


class Club(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField(null=True)
    mosru_link = models.URLField()
    attributes = models.ManyToManyField(Attribute, through="clubattribute")

    def __str__(self) -> str:
        return f'Кружок "{self.name}"'


class ClubAttribute(models.Model):
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    attribute_id = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'Аттрибут кружка "{self.club_id.name}" - {self.attribute_id.name} = {self.value}'


class ClubPicture(models.Model):
    image = models.ImageField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Картинка кружка "{self.club.name}"'


DAY_OF_THE_WEEK = {
    '1': u'Понедельник',
    '2': u'Вторник',
    '3': u'Среда',
    '4': u'Четверг',
    '5': u'Пятница',
    '6': u'Суббота',
    '7': u'Воскресенье',
}


class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(DayOfTheWeekField, self).__init__(*args, **kwargs)


class ClubDay(models.Model):
    day = DayOfTheWeekField()
    start_time = TimeField()
    end_time = TimeField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'День кружка "{self.club.name}" - {DAY_OF_THE_WEEK[self.day]}, с {self.start_time} до {self.end_time}'
