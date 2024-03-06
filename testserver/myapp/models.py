from django.db import models

class CallBack(models.Model):
    name = models.CharField(max_length = 100,blank = True,null = True)
    mobile_no = models.CharField(max_length = 10,blank = True,null = True)
    email  = models.CharField(max_length = 100,blank = True,null = True)
    paragraph = models.TextField(null = True,blank = True)
    
    def __str__(self):
        return self.name
