expenses = []


def sort_expenses(month):
    total_amount_this_month = ((expense_amount, expense_type, expense_month) for expense_amount, expense_type, expense_month in expenses if expense_month == month)
    total_amount_this_month = list(total_amount_this_month)
    total_amount_this_month.sort(key=lambda x:x[0])
    print(total_amount_this_month)


def show_type(month, type):
    total_amount_this_month = ((expense_amount, expense_type, expense_month) for expense_amount, expense_type, expense_month in expenses if expense_type == type and expense_month == month)
    print(list(total_amount_this_month))


def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')


def add_expense(month):
    print()
    expense_amount = int(input("Enter the amount [zl]: "))
    expense_type = input("Specify the type of expense (food, entertainment, home, other): ")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)


def show_stats(month):
    total_amount_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for expense_amount, _, expense_month in expenses if expense_month == month)
    average_expense_this_month = total_amount_this_month / number_of_expenses_this_month

    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    average_expense_all = total_amount_all / len(expenses)

    print("All expenses this month: ", total_amount_this_month)
    print("All expenses [zł]")
    print("Average spend this month [zł] ", average_expense_this_month)
    print("Average expense [zl] ", average_expense_all)


while True:
    print()

    while True:
        month = int(input("Select a month [1-12]: "))
        if month not in range(1, 12+1):
            print("There is no such month")
        else:
            if month == 1:
                print("January")
            elif month == 2:
                print("February")
            elif month == 3:
                print("March")
            elif month == 4:
                print("April")
            elif month == 5:
                print("May")
            elif month == 6:
                print("June")
            elif month == 7:
                print("July")
            elif month == 8:
                print("August")
            elif month == 9:
                print("September")
            elif month == 10:
                print("October")
            elif month == 11:
                print("November")
            else:
                print("December")
            break

    if month == 0:
        break

    while True:
        print()
        print("0. Return to choose of month")
        print("1. Show all expenditure")
        print("2. Add expenditure ")
        print("3. Show statistic")
        print("4. Sort")
        print("5. Type")
        choice = int(input("Choose option: "))

        if choice not in range(5+1):
            print("The correct option has not been chosen, one more time")
        else:
            if choice == 0:
                break

            if choice == 1:
                print("All expenses")
                show_expenses(month)

            if choice == 2:
                print("Add an expense")
                add_expense(month)

            if choice == 3:
                show_stats(month)

            if choice == 4:
                sort_expenses(month)

            if choice == 5:
                show_type(month, "home")
            break
