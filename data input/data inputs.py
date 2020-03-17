Basic_salary=1500
Bonus_rate=200
Commission_rate=0.02

Number_of_laptops=int(input("Number_of_laptops\n"))
Price_of_laptops=int(input("Price_of_laptops\n"))

Bonus=int(Bonus_rate * Number_of_laptops )
print(Bonus)

Commission = (Commission_rate * Number_of_laptops * Price_of_laptops )
print(Commission)

Gross_salary=Basic_salary + Bonus + Commission
print(Gross_salary)


