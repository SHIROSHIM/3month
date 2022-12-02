class product:
    name = 'my product'
    price = 50
    packed_data = "02.08.2022"

    def show_exp_date(self):
        start_day = int(self.packed_data[:2])
        start_day += 10
        exp_date = f'{start_day}{self.packed_data[2:00]}'
        print(exp_date)


apple = product()
apple.name = 'Яблоко'
print(apple.name)

apple = product()
print(apple.price)
print(apple.packed_data)
apple.shoe_exp_date()