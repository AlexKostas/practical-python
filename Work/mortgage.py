# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    extra = 0
    if months >= extra_payment_start_month - 1 and months < extra_payment_end_month:
        extra = extra_payment

    if payment + extra <= principal * (1+rate/12):
        principal = principal * (1+rate/12) - payment - extra
        total_paid = total_paid + payment + extra
    else:
        total_paid += principal
        principal = 0

    months = months + 1
    print(f'{months} {total_paid:0.2f} {principal:0.2f}')

print(f'\nTotal paid {total_paid:0.2f} over {months} months')
