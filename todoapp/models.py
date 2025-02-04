from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# todo_list_app/models.py
class TODO(models.Model):
    status_choice=[
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    priority_choice=[
        ('1','1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
        ('4','4️⃣'),
        ('5','5️⃣'),
        ('6','6️⃣'),
        ('7','7️⃣'),
        ('8','8️⃣'),
        ('9','9️⃣'),
        ('10','🔟'),
    ]

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=2 , choices=status_choice )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=20, choices=priority_choice)
