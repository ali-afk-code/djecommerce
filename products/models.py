from django.db import models
from commerce_project.settings import AUTH_USER_MODEL as User

from django.shortcuts import reverse
CATEGORY_CHOICES=(
    ('Smartphones','Smartphones'),
    ('Tablets','Tablets'),
    ('Headphones','Headphones'),
)
LABEL_CHOICES=(
    ('primary','Primary'),
    ('secondary','Secondary'),
    ('danger','Danger'),
)


class Customer(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField(null=True,blank=True, max_length=54)
    name = models.CharField(max_length=120,null=True)
    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    d_price = models.FloatField(blank=True,null=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=11)
    label = models.CharField(choices=LABEL_CHOICES,max_length=9)
    slug = models.SlugField()
    description = models.TextField(blank=True,null=True)
    image=models.ImageField(default='/static/img/placeholder.jpg',blank=True,null=True)
    

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    def add_to_cart_url(self):
        return reverse("cart",kwargs={
            'slug':self.slug
        })


class Order(models.Model):
    customer = models.ForeignKey(Customer,
                            on_delete=models.SET_NULL,
                            null=True,blank=True)
    # items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    # def __str__(self):
    #     return str(self.)

class OrderItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return f"{self.quantity} of {self.item.title}"
    @property
    def get_total(self):
        if (self.item.d_price is None):
            return (self.quantity)*(self.item.price )
        return self.quantity*self.item.d_price

    