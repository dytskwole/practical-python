principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

month = 0

while principal > 0:
    month += 1
    interest = principal * rate / 12

    if extra_payment_start_month <= month <= extra_payment_end_month:
        current_extra_payment = extra_payment
    else:
        current_extra_payment = 0

    principal_payment = payment + current_extra_payment - interest

    if principal_payment > principal:
        principal_payment = principal
    principal -= principal_payment
    total_paid += payment + current_extra_payment if principal > 0 else principal + interest

    print(month, round(total_paid, 2), round(principal, 2))
print('Total paid', round(total_paid, 2))
print('Months', month)
