from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser



ROLES = [
    ("MANAGEMENT", "MANAGEMENT"),
    ("SALES", "SALES"),
    ("SUPPORT", "SUPPORT")
]


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLES)

    def __str__(self):
        return f"{self.username} ({self.role})"

    def save(self, *args, **kwargs):
        if self.role == "MANAGEMENT":
            self.is_superuser = True
            self.is_staff = True
        else:
            self.is_superuser = False
            self.is_staff = False

        user = super(User, self)
        user.save()

        return user


class Client (models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=12, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    company_name = models.CharField(max_length=128, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      blank=True)
    status = models.BooleanField(default=False, verbose_name="Existing")

    def __str__(self):
        if self.status is False:
            stat = "POTENTIAL"
        else:
            stat = "EXISTING"
        return f"Clients {self.pk} : {self.last_name}, {self.first_name}, ({stat})"


class Contract (models.Model):
    client = models.ForeignKey(to=Client,
                               on_delete=models.CASCADE,
                               limit_choices_to={"status": True},
                               related_name="contract",
                               )
    status = models.BooleanField(default=False, verbose_name="Signed")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    payment_invoice = models.BooleanField(default=False, verbose_name="Payed")
    date_payment = models.DateField()

    def __str__(self):
        name = f"{self.client.last_name}, {self.client.first_name}"
        if self.status is False:
            stat = "NOT SIGNED"
        else:
            stat = "SIGNED"
        return f"Contract {self.pk} : {name} ({stat})"


class Event(models.Model):
    contract = models.OneToOneField(to=Contract,
                                    on_delete=models.CASCADE,
                                    limit_choices_to={"status": True},
                                    related_name="event"
                                    )
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        blank=True,)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_name = models.CharField(max_length=150, null=True, blank=True)
    event_status = models.BooleanField(default=False, verbose_name="Completed")
    event_place = models.CharField(max_length=200, null=True, blank=True)
    event_participants = models.PositiveIntegerField()
    event_date = models.DateTimeField()
    event_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        name = f"{self.contract.client.last_name}, {self.contract.client.first_name}"
        date = self.event_date.strftime("%Y-%m-%d")
        if self.event_status is False:
            stat = "UPCOMMING"
        else:
            stat = "COMPLETED"
        return f"Event {self.pk} : {name} | Date : {date} ({stat})"
