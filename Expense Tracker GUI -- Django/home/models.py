from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# admin password == 1qaz@WSX3edc

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRANSPORT', 'Transport'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('HEALTH', 'Health'),
        ('EDUCATION', 'Education'),
        ('OTHERS', 'Others'),
    ]
    
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    srno = models.AutoField(primary_key=True, auto_created = True)
    
    
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='OTHERS')
    description = models.TextField(blank=True,max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    
    
        
    def __str__(self):
        return self.category + ' - ' + str(self.amount) + ' - ' + str(self.date)
    
    def add_category_choice(self, cate):
        # Add new category dynamically
        if cate not in self.category_choices:
            self.category_choices.append(cate)
            self.save()