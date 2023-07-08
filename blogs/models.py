from django.db import models

# Create your models here.

class Authors(models.Model):
    name=models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    place = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural  = 'Authors'
        
    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    sub_title = models.CharField(max_length=355)
    author = models.ForeignKey(Authors,on_delete=models.DO_NOTHING)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.author}"
    
