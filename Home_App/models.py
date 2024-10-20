from django.db import models

# Create your models here.
class Book_Table(models.Model):
    Name = models.CharField(max_length=50)
    Email= models.EmailField(max_length=254)
    Number=models.IntegerField()
    Date=models.DateField()
    Person=models.IntegerField()

    def __str__(self):
        return self.Name

class ItemList(models.Model):
    Category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.Item_name
    




    
    

