from math import ceil, log, floor
import argparse


def calculation(no_in, per):
    return no_in * pow((1 + no_in), per) / (pow(1 + no_in, per) - 1)


def logarithm(mon, nom, pri):
    return log((mon / (mon - (nom * pri))), (1 + nom))


parser = argparse.ArgumentParser(description="This program prints recipes consisting of the ingredients you provide.")

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if args.type == 'annuity':

    if args.principal and args.payment and args.interest and args.periods is None:

        args.principal = float(args.principal)
        args.payment = float(args.payment)
        nominal_i = float(args.interest) / 1200
        number_of_months = logarithm(args.payment, nominal_i, args.principal)
        c_number_of_months = ceil(number_of_months)  # number of months of paying by client
        years = floor(c_number_of_months / 12)
        reminder = c_number_of_months % 12
        if reminder == 0 and years != 0:
            print(f'It will take {years} years to repay this loan!')
        elif years > 0 and reminder != 0:
            print(f'It will take {years} years and {reminder} months to repay this loan!')
        else:
            print(f'It will take {reminder} months to repay this loan!')
        print(f'Overpayment = {int(args.payment * c_number_of_months - args.principal)}')  # printing overpayment

    elif args.principal and args.periods and args.interest and args.payment is None:

        args.principal = float(args.principal)
        args.periods = float(args.periods)
        n_i = float(args.interest) / 1200  # nominal interest

        monthly_payment = args.principal * calculation(n_i, args.periods)
        monthly_payment_fc = ceil(monthly_payment)
        print(f'Your annuity payment = {monthly_payment_fc}!')
        print(f'Overpayment = {int(monthly_payment_fc * args.periods - args.principal)}')

    elif args.payment and args.periods and args.interest and args.principal is None:

        args.payment = float(args.payment)
        args.periods = float(args.periods)
        nominal_i = float(args.interest) / 1200
        principal = floor(args.payment / calculation(nominal_i, args.periods))
        o_v = args.payment * args.periods - principal  # overpayment
        print(f"Your loan principal = {principal}!")
        print(f'Overpayment = {int(o_v)}')

    else:
        print('Incorrect parameters.')
############################################################
############################################################

if args.type == 'diff':

    if args.periods and args.interest and args.principal and args.payment is None:
        args.principal = float(args.principal)
        args.periods = float(args.periods)
        n_i = float(args.interest) / 1200  # nominal interest
        m = 1  # current repayment month
        c = 0  # counter of overpayment
        d = 0  # difference after using ceil()
        while m <= args.periods:
            diff_payment = (args.principal / args.periods) + (n_i * (args.principal - (args.principal * (m - 1) / args.periods)))
            d = ceil(diff_payment)
            print(f'Month {m}: payment is {d}')
            m += 1
            c = c + d
        print(f'Overpayment = {int(c - args.principal)}')

    else:
        print('Incorrect parameters.')
