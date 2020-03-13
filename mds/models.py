from django.db import models

# Create your models here.

class Project(models.Model):
    PJT_No = models.CharField(max_length=20)
    PJT_Name = models.CharField(max_length=50)
    PJT_Country = models.CharField(max_length=20)
    PJT_Client = models.CharField(max_length=30)

    def __str__(self):
        return self.PJT_No

class MR(models.Model):
    PJT_No = models.ForeignKey(Project, on_delete=models.CASCADE)
    MR_No = models.CharField(max_length=15)
    MR_Name = models.CharField(max_length=50)
    MR_Remark = models.TextField

    def __str__(self):
        return self.MR_No

class EQT(models.Model):
    PJT_No = models.ForeignKey(Project, on_delete=models.CASCADE)
    MR_No = models.ForeignKey(MR, on_delete=models.CASCADE)
    EQT_No = models.CharField(max_length=20)
    EQT_Name = models.CharField(max_length=40)

    def __str__(self):
        return self.EQT_No