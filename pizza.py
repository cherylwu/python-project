def make_pizza(*toppings):
    """
    打印顾客点的所有配料
    :param toppings:
    :return:
    """
    print(toppings)


def make_pizza2(*toppings):
    """概述要制作的pizza"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"{topping}")


def make_pizza3(size, *toppings):
    """概述要制作的pizza"""
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


#print('a' * 2)
#make_pizza('pepperoni')
#make_pizza('mushrooms', 'green peppers', 'extra cheese')

#make_pizza3(12,'pepperoni*2')
#make_pizza3(13,'mushrooms*2', 'green peppers2', 'extra cheese2')
