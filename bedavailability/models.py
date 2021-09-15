from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='hospitals')

    def __str__(self):
        return self.name


class Facility(models.Model):
    # hospital = models.OneToOneField(
    #     Hospital, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(
        max_length=60, null=False, blank=False, default="")

    def __str__(self):
        return self.title


class Availability(models.Model):
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name='availabilies')
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, related_name='availabilies')
    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.hospital.name} - {self.facility.title}'