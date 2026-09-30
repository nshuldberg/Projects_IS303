# Noah Shuldberg
# Personal expense tracker

add_expense = -1
expense_list = []
small_expense = 0
moderate_expense = 0
large_expense = 0
expense_counter = 0

# Begin expense input prompting
while add_expense != 0.00:
    add_expense = float(input("Enter expense or 0 to finish: "))
    if add_expense < 0:
        print("Invalid input. Please try again.")
        continue
    if add_expense == 0:
        break
    expense_list.append(add_expense)
    expense_counter += 1

# Categorize expenses
for expense in expense_list:
    if expense < 25.00:
        small_expense += 1
    elif 25.00 <= expense <= 100.00:
        moderate_expense += 1
    elif expense > 100.00:
        large_expense += 1
# Print summary
print("\nEXPENSE SUMMARY")
print("=============================")
print(f"\nTotal number of expenses: {expense_counter}")
print("Total expenses: " + "${:,.2f}".format(sum(expense_list)))
print("Average expense: " + "${:,.2f}".format(sum(expense_list)/(len(expense_list))))
print("\nSmallest Expense: " + "${:,.2f}".format(min(expense_list)))          
print("Largest expense: " + "${:,.2f}".format(max(expense_list)))
print(f"\nNumber of small expenses: {small_expense}")
print(f"Number of moderate expenses: {moderate_expense}")
print(f"Number of large expenses: {large_expense}")



