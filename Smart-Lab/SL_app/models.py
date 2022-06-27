from telnetlib import STATUS
from tkinter.messagebox import YES
from django.db import models

# Create your models here.

class Admin(models.Model):
    use_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=16)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return f"{self.__dict__}"


class User(models.Model):
    use_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=16)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

class SL_Master(models.Model):
    ORG_CODE = models.CharField(max_length=500)
    DOMAIN_CODE = models.CharField(max_length=500)
    SUBDOMAIN_CODE = models.CharField(max_length=500)
    PRODUCT_NAME = models.CharField(max_length=500)
    PRODUCT_ID= models.IntegerField(primary_key=True)
    SERIAL_ID = models.CharField(max_length=255,unique=True)
    ISACTIVE = models.BooleanField(default=YES)

    class Meta:
        db_table = 'sl_master'


class LAB(models.Model):

    ID = models.IntegerField(primary_key=True)
    DUT_ID = models.CharField(max_length=500)
    SUT_NAME = models.CharField(max_length=500)
    ITP_C_STATUS = models.BooleanField(default=True)
    DEBUG_SERVER_IP = models.CharField(max_length=500)
    CCA_C_STATUS = models.BooleanField(default=True)
    TEST_SERVER_IP = models.CharField(max_length=500)
    UART_C_STATUS = models.BooleanField(default=True)
    TEST_PC_IP = models.CharField(max_length=500) 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    available_start_date = models.DateTimeField()
    available_end_date = models.DateTimeField()


    class Meta:
        db_table = 'lab'

    def __str__(self):
        return f"{self.__dict__}"


class SL_DEVICE_LIST(models.Model):
    ORG_CODE = models.CharField(max_length=400)
    DOMAIN_CODE = models.CharField(max_length=400)
    SUBDOMAIN_CODE = models.CharField(max_length=400)
    PRODUCT_ID= models.ForeignKey(SL_Master,on_delete=models.CASCADE)
    SERIAL_ID = models.CharField(max_length=255,unique=True)
    STATUS = models.BooleanField(default=True)
    LAB_ID= models.ForeignKey(LAB,on_delete=models.CASCADE)
    ISACTIVE = models.BooleanField(default=True)
    SPECIFICATION = models.CharField(max_length=1000)

    class Meta:
        db_table = 'sl_device_list'

    def __str__(self):
        return f"{self.__dict__}"



