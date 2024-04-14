from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Vlan(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class IPAddressManager(models.Manager):
    def get_subnets(self):
        array = self.values_list("subnet", flat=True).distinct()
        return [a for a in array if a != ""]


class IPAddress(models.Model):
    address = models.GenericIPAddressField()
    mask = models.GenericIPAddressField(null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    label = models.ManyToManyField(Label)
    vlan = models.ForeignKey(Vlan, on_delete=models.CASCADE, null=True, blank=True)
    subnet = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    objects = IPAddressManager()

    def __str__(self):
        return str(self.address)


class PingStat(models.Model):
    address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    avarage_response = models.FloatField()
    is_alive = models.BooleanField()

    def __str__(self):
        return f"{self.address} - {self.timestamp} - {self.is_alive}"
