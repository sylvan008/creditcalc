import sys
import argparse
import math

INCORRECT_PARAMETERS = "Incorrect parameters"
DIFF = "diff"
ANNUITY = "annuity"
PAYMENT = "payment"
PRINCIPAL = "principal"
PERIODS = "periods"
INTEREST = "interest"


def sys_exit():
    print(INCORRECT_PARAMETERS)
    sys.exit()


def nominal_percent(interest):
    return float(interest) / (12 * 100)


def validation_arguments(argv, arguments):
    if len(argv[1:]) < 4:
        sys_exit()
    type_ = arguments.type
    principal = arguments.principal
    payment = arguments.payment
    interest = arguments.interest
    for value in [principal, payment, interest]:
        if value < 0:
            sys_exit()
    if not interest or not type_:
        sys_exit()
    if type_ not in [DIFF, ANNUITY]:
        sys_exit()
    if type_ == DIFF and payment:
        sys_exit()


parser = argparse.ArgumentParser(description="Расчёт кредита")
parser.add_argument("--type", help="Выберите тип расчёта кредита зи списка: 'diff', 'annuity'")
parser.add_argument("--payment", type=int, default=0, help="Ежемесячный платёж. Не указывается, если тип рассчёта: 'diff'")
parser.add_argument("--principal", type=int, default=0, help="Сумма займа.")
parser.add_argument("--periods", type=int, default=0, help="Количетсво платежей. Обычно равно количеству месяцев.")
parser.add_argument("--interest", type=nominal_percent, help="Обязательный параметр. Указывается без знака процентов.")

args = parser.parse_args()
validation_arguments(sys.argv, args)


def get_loan_principal(payment, periods, interest):
    pow_loan_interest = math.pow(1 + interest, periods)
    principal = payment / ((interest * pow_loan_interest) / (pow_loan_interest - 1))
    return round(principal)


def get_annuity_payment(principal, periods, interest):
    pow_loan_interest = math.pow(1 + interest, periods)
    payment = principal * (interest * pow_loan_interest / (pow_loan_interest - 1))
    return math.ceil(payment)


def get_diff_payment(principal, periods, current_period, interest):
    return math.ceil(principal / periods + interest * (principal - (principal * (current_period - 1) / periods)))


def get_number_of_payments(principal, payment, interest):
    body = payment / (payment - (interest * principal))
    base = 1 + interest
    return math.ceil(math.log(body, base))


def get_overpayment(principal, payment, periods):
    return periods * payment - principal


def plural(word, count):
    return word if count == 1 else f"{word}s"


def annuity_payment(interest, principal, periods, payment):
    if not periods:
        periods = get_number_of_payments(principal, payment, interest)
        year_count = periods // 12
        month_count = periods % 12

        year_message = f"{year_count} {plural('year', year_count)}" if year_count > 0 else ""
        month_message = f"{month_count} {plural('month', month_count)}" if month_count > 0 else ""
        and_ = " and " if year_message and month_message else ""
        message = f"It will take {year_message}{and_}{month_message} to repay this loan!"

        print(message)
    elif not principal:
        principal = get_loan_principal(payment, periods, interest)
        print(f"Your loan principal = {principal}")
    elif not payment:
        payment = get_annuity_payment(principal, periods, interest)
        print(f"Your monthly payment = {payment}!")
    overpayment = get_overpayment(principal, payment, periods)
    print(f"Overpayment = {overpayment}")


def diff_payment(principal, periods, interest):
    payments = 0
    for period in range(1, periods + 1):
        payment = get_diff_payment(principal, periods, period, interest)
        print(f"Month {period}: payment is {payment}")
        payments += payment
    overpayment = payments - principal
    print(f"Overpayment = {overpayment}")


if args.type == "annuity":
    annuity_payment(args.interest, args.principal, args.periods, args.payment)
else:
    diff_payment(args.principal, args.periods, args.interest)
