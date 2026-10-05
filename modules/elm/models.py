from django.db import models
from modules.directory.models import UserRef

class LeaveCategory(models.Model):
    """Model representing the type of leave."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'elm_leave_category'

    def __str__(self):
        return self.name


class LeaveApplication(models.Model):
    """Model representing a leave application."""
    employee = models.ForeignKey(UserRef, on_delete=models.CASCADE)
    leave_category = models.ForeignKey(LeaveCategory, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ])

    class Meta:
        db_table = 'elm_leave_application'

    def __str__(self):
        return f'{self.employee.username} - {self.leave_category.name}'


class LeaveBalance(models.Model):
    """Model representing the leave balance of an employee."""
    employee = models.ForeignKey(UserRef, on_delete=models.CASCADE)
    leave_category = models.ForeignKey(LeaveCategory, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField()

    class Meta:
        db_table = 'elm_leave_balance'
        unique_together = ('employee', 'leave_category')

    def __str__(self):
        return f'{self.employee.username} - {self.leave_category.name} - {self.balance}'
