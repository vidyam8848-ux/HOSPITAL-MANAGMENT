from django.db import models


class dept(models.Model):
    dept_name = models.CharField(max_length=255)
    dept_desc = models.TextField()

    def __str__(self):
        return self.dept_name


class Doctors(models.Model):
    doc_name = models.CharField(max_length=200)
    doc_spec = models.CharField(max_length=255)
    dept_name = models.ForeignKey(dept, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors', null=True, blank=True)

    def __str__(self):
        return self.doc_name
    
class booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_email = models.EmailField()
    p_phone = models.CharField(max_length=20)
    
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booked_on = models.DateField() 

    def __str__(self):
        return  f"{self.p_name} - {self.doc_name} "
    