from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    date = models.DateField()
    is_smok = models.BooleanField()

    def __str__(self):
        return f"{self.user} - {self.date} - {'Usou' if self.is_smok else 'Não usou'}"
