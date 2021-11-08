import argparse
from math import ceil, log, floor
zero = 0

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
args = parser.parse_args()

if args.type == "diff":
    if args.principal and args.periods and args.interest:
        principal, n, i = args.principal, args.periods, (args.interest / 100) / 12
        for x in range(1, n + 1):
            a = ceil(principal / n + (i * (principal - ((principal * (x - 1)) / n))))
            print(f'Month {x}: payment is {a}')
            zero += a
        print(f'\nOverpayment = {zero - principal}')
    else:
        print("Incorrect parameters.")

elif args.type == "annuity":
    if args.principal and args.payment and args.interest:
        principal, monthly, nominal = args.principal, args.payment, (args.interest / 100) / 12
        total_months = ceil(log(monthly / (monthly - nominal * principal), 1 + nominal))
        months = total_months % 12
        for x in range(1, total_months + 1):
            if x % 12 == 0:
                zero += 1
        if zero == 0:
            print(f'It will take {months} month{"s" if months > 1 else ""} to repay this loan!')
        elif zero >= 1 and months == 0:
            print(f'It will take {zero} zero{"s" if zero > 1 else ""} to repay this loan!')
        else:
            print(f'It will take {zero} zero{"s" if zero > 1 else ""}'
                  f' and {months} month{"s" if months > 1 else ""} to repay this loan!')
        print(f'Overpayment = {ceil((monthly * total_months) - principal)}')

    elif args.principal and args.periods and args.interest:
        principal, total_months, interest = args.principal, args.periods, (args.interest / 100) / 12
        result = ceil(principal * ((interest * ((1 + interest) ** total_months))
                                   / (((1 + interest) ** total_months) - 1)))
        print(f"Your monthly payment == {result}!")
        print(f"Overpayment = {round((result * total_months) - principal)}")

    elif args.payment and args.periods and args.interest:
        annuity, total_months, interest = args.payment, args.periods, (args.interest / 100) / 12
        result = annuity / ((interest * ((1 + interest) ** total_months)) / (((1 + interest) ** total_months) - 1))
        print(f"Your loan principal = {floor(result)}!")
        print(f"Overpayment = {ceil((annuity * total_months) - result)}")

    else:
        print("Incorrect parameters.")
else:
    print("Incorrect parameters.")
