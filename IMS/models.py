from django.db import models

# Create your models here.
class Insurance_list(models.Model):
    
    Insurance_name = models.CharField(max_length=100)
    Insurance_img = models.ImageField(upload_to='policyimage')
    Insurance_desc = models.TextField()


class Primary_insurance(models.Model):
    Ispolicy =  models.CharField(max_length=100)
    customer_name= models.TextField()
    mobile=models.IntegerField()
    reg_no= models.TextField()
    company_name= models.TextField()
    model_name= models.TextField()
    reg_in= models.TextField()
    reg_date=models.DateField() 
    policy_status=models.TextField()
    expiry_date=models.DateField() 
    pincode=models.IntegerField()

class belowcontent(models.Model):    
    
    b_contentname = models.CharField(max_length=100)
    b_contentdesc = models.TextField()
    

