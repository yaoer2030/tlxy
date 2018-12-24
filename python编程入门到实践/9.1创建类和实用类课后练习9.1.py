# 9.1餐馆:创建一个名为Restaurant的类,其方法__init__()设置两个属性:
# restaurant_name和cuisine_type,其中一个名为describe_restaurant()的
# 方法和一个名为open_resaurant()的方法,其中前者打印前面两项信息,而后
# 者打印一条消息.指出餐馆正在营业
# 根据这个类创建1个名为restaurant的实例,分别打印其两个属性,在调用前述两个方法

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title() + "餐馆很干净")
    def open_resaurant(self):
        print(self.restaurant_name.title() + "餐馆正在营业")

restaurant = Restaurant("来福","pizza")
print("这家餐馆名叫" + restaurant.restaurant_name.title())
print("主要卖" + restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_resaurant()