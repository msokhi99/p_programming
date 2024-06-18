# Unlimited Positional Arguments. These are stored as a tuple.
def add(*args):
    print(sum(args))
    # print(type(args))

add(1,2,3,4,5)

# Unlimited KeyWord Arguments. These are stored as a dictionary.

def test_function(x,**kwargs):
    x+=kwargs["num_one"]
    # A better way: 
    # x+=kwargs.get("num_one")
    print(f"X with NUM ONE: {x}")
    x*=kwargs["num_two"]
    # x+=kwargs.get("num_two")
    print(f"X with NUM TWO: {x}")

test_function(10,num_one=10,num_two=20)

class Car_Class():
    def __init__(self,**kwargs):
        self.car_model=kwargs.get("car_model")
        self.car_whp=kwargs.get("car_whp")

car_one=Car_Class(car_model="Chevy",car_whp=1000)
print(f"Car Model; {car_one.car_model}\nCar WHP: {car_one.car_whp}")
