from django.db import models

# Create your models here.

# class dummy_table(models.Model):
#     Settings_Name = models.CharField(max_length=140, unique=True)
    
#     def __str__(self):
#         return self.Settings_Name

class tbStockList(models.Model):
    CompanyName = models.CharField(max_length=140, unique=True,null=True, blank=True)
    Symbol = models.CharField(max_length=140, unique=True)
    Sector  = models.CharField(max_length=100,null=True, blank=True)
    Exchange = models.CharField(max_length=100,null=True, blank=True)
    Market = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return self.Symbol

class tbMyStocks(models.Model):
    Symbol = models.CharField(max_length=140, unique=True)
    #Symbol = models.ForeignKey(tbStockList)

    def __str__(self):
       return self.Symbol
    
    # @classmethod
    # def add_symbol(cls, asymbol):
    #     friend = tbMyStocks(Symbol=asymbol)
    #     friend.save()

    # @classmethod
    # def remove_symbol(cls, asymbol):
    #     friend = tbMyStocks(Symbol=asymbol)
    #     friend.delete()
         

