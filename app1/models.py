from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=11)
    def __str__(self):
        return f"{self.name}  {self.address}  {self.mobileno}"
class paymentdetails(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    amount=models.IntegerField()
    dateofpayment=models.DateField()
    paymentmode=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.student}  {self.amount}  {self.dateofpayment}  {self.paymentmode}"
# Create your models here.
