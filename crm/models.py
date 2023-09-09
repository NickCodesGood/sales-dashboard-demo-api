from django.db import models
# Create your models here.

class Lead(models.Model):        
    name = models.TextField()
    email = models.EmailField(unique=True)
    STATUS_CHOICES = [
        ('prospect', 'Prospect'),
        ('active', 'Active'),
        ('unqualified', 'Unqualified'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='prospect')
    estimatedSaleAmount = models.DecimalField(max_digits=15, decimal_places=2) # 1 trillion + .00 cents
    estimatedCommission = models.DecimalField(max_digits=15, decimal_places=2, default=0, editable=False)


    def save(self, *args, **kwargs):    
        LEAD_COMMISSION_AS_DECIMAL = 0.05 # currently 5%
        if self.status == "unqualified":
            self.estimatedCommission = 0
        else:
            self.estimatedCommission = self.estimatedSaleAmount.__float__() * LEAD_COMMISSION_AS_DECIMAL
        super(Lead, self).save(*args, **kwargs)

    def __str__(self):
        return f"Lead(id={self.id}, name='{self.name}', email='{self.email}', status='{self.status}', estimatedSaleAmount={self.estimatedSaleAmount}, estimatedCommission={self.estimatedCommission})"

