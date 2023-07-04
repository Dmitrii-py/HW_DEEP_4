# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.
MODES = """Действия:
пополнение - 1
снятие - 2
выйти - 3
Выберите действие: """

LUXURY_LIMIT = 5_000_000
TAX_LUXURY = 0.9
TAX_OUTCOME = 0.015
MAX_TAX_OUT = 600
MIN_TAX_OUT = 30

MONEY_DIV = 50
BONUS_FOR_OPERATION = 1.03
OPERATIONS_FOR_BONUS = 3

balance = 0
operations_count = 0
operations_tracking = []

def tax_luxury():
    global balance
    out = balance - balance * TAX_LUXURY
    if balance >= LUXURY_LIMIT:
        balance -=out
        print('налог на роскошь')
    else:
        return

        operations_tracking.append((out, 'налог на роскошь'))

def bonus_three():
    global balance, operations_count
    profit = balance * BONUS_FOR_OPERATION - balance
    if operations_count % OPERATIONS_FOR_BONUS == 0 and operations_count:
        balance += profit
        print('Бонус за 3 операции')
    else:
        return
    operations_tracking.append((profit, 'Бонус за 3 операции'))

def refil():
    global balance, operations_count
    income = int(input())
    if income % MONEY_DIV == 0:
        balance += income
    else:
        print('incorrect sum')
        operations_count += 1
        operations_tracking.append((income, 'пополнение'))

def withdraw():
    global balance, operations_count
    outcome = int(input())
    if outcome % MONEY_DIV == 0:
        comission = balance * TAX_OUTCOME
        if comission >= MAX_TAX_OUT:
            comission = MAX_TAX_OUT
        elif comission <= MIN_TAX_OUT:
            comission = MIN_TAX_OUT
            balance -= comission
            balance -= outcome
        else:
            print('incorrect sum')
            operations_count += 1
            operations_tracking.append((outcome, 'снятие'))
            operations_tracking.append((comission, 'комиссия за пополнение'))

def main():
    while True:
        choose = input(f'{MODES}')

        tax_luxury()
        bonus_three()

        if choose ==1:
            refil()
        elif choose == 2:
            withdraw()
        elif choose == 3:
            break
        else:
            print('Incorrect')
            print(f'current balance: {balance}')

if __name__ == '__main__':
    main()
    print(operations_tracking)


while True:
    choose = input(f"{MODES}")

    if balance >= LUXURY_LIMIT:
        balance *= TAX_LUXURY
        print('Раскулачивание')
    if operations_count % OPERATIONS_FOR_BONUS == 0:
        balance *= BONUS_FOR_OPERATION
        print('Бонус за 3 операции')

    if choose == '1':
        income = int(input())
        if income % MONEY_DIV == 0:
            balance += income
        else:
            print('incorrect summ')
        operations_count += 1

    elif choose == '2':
        outcome = int(input())
        if outcome % MONEY_DIV == 0:
            comission = balance * TAX_OUTCOME
            if comission >= MAX_TAX_OUT:
                comission = MAX_TAX_OUT
            elif comission <= MIN_TAX_OUT:
                comission = MIN_TAX_OUT
            balance -= comission
            balance -= outcome
        else:
            print('incorrect summ')
        operations_count += 1

    elif choose == '3':
        break

    else:
        print(f'Incorrect')

    print(f'current balance: {balance}')