# HAB Taxi Services

# Written by: Group 22A-2, Makenzie Roberts, Tyler Dinn, Eoin Hurley, and David Turner
# Date written: Feb 25, 2022
# Project ID: Final Sprint Week. Project 2: HAB Taxi Services


def new_emp():
    print("New Employee")


def company_revenue():
    pass


def company_expenses():
    pass


def track_car_rentals():
   pass


def record_emp_payment():
    pass


def pr_comp_profit_tbl():
    print("Print Company Profit Listing/Table")


def pr_comp_dr_fin_tbl():
    print("Print Driver Financial Listing/Table")


# Main

print()
print(" " * 8, "HAB Taxi Services")
print(" " * 5, "Company Services System")
print("-" * 42)
print("Enter a New Employee (driver) - Press 1")
print("Enter Company Revenues  - Press 2")
print("Enter Company Expenses - Press 3")
print("Track Car Rentals - Press 4")
print("Record Employee Payment - Press 5")
print("Print Company Profit Listing - Press 6")
print("Print Driver Financial Listing - Press 7")
print("Quit the Program - Press 8")
print()

while True:

    Choice = input("Enter choice: (1-8): ")
    print()
    if Choice == "1":
        new_emp()
    elif Choice == "2":
        company_revenue()
    elif Choice == "3":
        company_expenses()
    elif Choice == "4":
        track_car_rentals()
    elif Choice == "5":
        record_emp_payment()
    elif Choice == "6":
        pr_comp_profit_tbl()
    elif Choice == "7":
        pr_comp_dr_fin_tbl()
    elif Choice == "8":
        print("Thank you for utilizing the \"Company Services System\", have a wonderful day.")
        break
    else:
        print("Not a valid choice - please re-enter")
        print()