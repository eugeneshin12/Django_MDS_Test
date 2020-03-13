from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class PJT(models.Model):
    #Fields
    P_No = models.CharField(max_length=20,verbose_name='PJT_No')
    P_Name = models.CharField(max_length=50,verbose_name='PJT_Name')
    P_Country = models.CharField(max_length=20,verbose_name='PJT_Country')
    P_Client = models.CharField(max_length=30,verbose_name='PJT_Client')

    # Metadata
    class Meta:
        ordering = ['P_No']

    # Methods
    def __str__(self):
        return self.P_No
    def get_absolute_url(self):
        return reverse('pjt_detail',args=[str(self.id)])


class MR(models.Model):
    # Fields
    P_No = models.ForeignKey(PJT, on_delete=models.CASCADE,verbose_name='PJT_No')
    M_No = models.CharField(max_length=15,verbose_name='MR_No')
    M_Name = models.CharField(max_length=50,verbose_name='MR_No')
    M_Remark = models.TextField(default=None,verbose_name='MR_Note')

    # Methods
    def __str__(self):
        return self.M_No

class EQT(models.Model):
    # Fields
    P_No = models.ForeignKey(PJT, on_delete=models.CASCADE,verbose_name='PJT_No')
    M_No = models.ForeignKey(MR, on_delete=models.CASCADE,verbose_name='MR_No')
    E_No = models.CharField(max_length=20,verbose_name='EQT_No')
    E_Name = models.CharField(max_length=40,verbose_name='EQT_No')
    E_User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True,verbose_name='Username')

    # Methods
    def __str__(self):
        return self.E_No

class PDS(models.Model):
    # Fields
    P_No = models.ForeignKey(PJT, on_delete=models.CASCADE,verbose_name='PJT_No')
    M_No = models.ForeignKey(MR, on_delete=models.CASCADE,verbose_name='MR_No')
    E_No = models.ForeignKey(EQT, on_delete=models.CASCADE,verbose_name='EQT_No')
    E_Name = models.CharField(max_length=40,verbose_name='EQT_Name')
    PD_Fluid = models.CharField(max_length=20,verbose_name='Fluid')
    PD_Head = models.IntegerField(verbose_name='Head')
    PD_Dens = models.IntegerField(verbose_name='Density')
    PD_NPSH = models.IntegerField(verbose_name='NPSH')
    PDS_Note = models.TextField(default=None,verbose_name='PDS_Note')
    #PDS_Image = models.ImageField(default=None,blank=True,verbose_name='PDS_Image')

    # Methods
    def __str__(self):
        return self.E_No

class MDS(models.Model):
    # Fields
    P_No = models.ForeignKey(PJT, on_delete=models.CASCADE,verbose_name='PJT_No')
    M_No = models.ForeignKey(MR, on_delete=models.CASCADE,verbose_name='MR_No')
    E_No = models.ForeignKey(EQT, on_delete=models.CASCADE,verbose_name='EQT_No')
    E_Name = models.CharField(max_length=40,verbose_name='EQT_Name')
    MD_Type = models.CharField(max_length=20,verbose_name='Type')
    MD_Seal = models.CharField(max_length=20,verbose_name='Seal')
    MD_Matl = models.CharField(max_length=20,verbose_name='Material')
    MDS_Note = models.TextField(default=None,verbose_name='MDS_Note')
    #MDS_Image = models.ImageField(default=None,blank=True,verbose_name='MDS_Image')

    # Methods
    def __str__(self):
        return self.E_No