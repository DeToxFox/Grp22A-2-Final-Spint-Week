
# HAB Taxi Services

# Written by: Group 22A-2, Makenzie Roberts, Tyler Dinn, Eoin Hurley, and David Turner
# Date written: April 22, 2022
# Project ID: Final Sprint Week. Project 2: HAB Taxi Services

import datetime as dt


def Dollar(num):
    dollar = "${:,.2f}".format(num)
    return dollar


# Add Values From Defaults File To Variables
with open("defaults.dat", "r") as f:
    NEXT_TRANS_NUM = int(f.readline())
    NEXT_DRIVER_NUM = int(f.readline())
    MON_STAND_FEE = float(f.readline())
    DAILY_RENT = float(f.readline())
    WEEKLY_RENT = float(f.readline())
    TAX_RATE = float(f.readline())


def new_emp():
    # Add Values From Defaults File To Variables
    with open("defaults.dat", "r") as f:
        NEXT_TRANS_NUM = int(f.readline())
        NEXT_DRIVER_NUM = int(f.readline())
        MON_STAND_FEE = float(f.readline())
        DAILY_RENT = float(f.readline())
        WEEKLY_RENT = float(f.readline())
        TAX_RATE = float(f.readline())

    # Input Driver's First Name
    while True:
        driverFirstName = input("Enter Driver First Name: ").title()
        if driverFirstName == "":
            print("Driver First Name cannot be Blank - Please Re-Enter")
        else:
            break

    # Input Driver's Last Name
    while True:
        driverLastName = input("Enter Driver Last Name: ").title()
        if driverLastName == "":
            print("Driver Last Name cannot be Blank - Please Re-Enter")
        else:
            break

    # Input Driver's Street address
    while True:
        stAdd = input("Enter Street Address: ").title()
        if stAdd == "":
            print("Street Address cannot be Blank - Please Re-Enter")
        else:
            break

    # Input Driver's City
    while True:
        city = input("Enter City: ").title()
        if city == "":
            print("City cannot be Blank - Please Re-Enter")
        else:
            break

    # Input Driver's Province
    while True:
        prov = input("Enter Province (XX): ").upper()
        if prov == "":
            print("Province cannot be Blank - Please Re-Enter")
        else:
            break

    # Input Driver's Postal Code
    while True:
        postCode = input("Enter Postal Code (A1A1A1): ").upper()
        if postCode == "":
            print("Postal Code cannot be Blank - Please Re-Enter")
        elif len(postCode) != 6:
            print("Postal Code must be 6 Characters Long. Please Re-Enter")
        elif not postCode[0].isalpha():
            print("First Character Must Be A Letter")
        elif not postCode[1].isdigit():
            print("Second Character Must Be A Number")
        elif not postCode[2].isalpha():
            print("Third Character Must Be A Letter")
        elif not postCode[3].isdigit():
            print("Fourth Character Must Be A Number")
        elif not postCode[4].isalpha():
            print("Fifth Character Must Be A Letter")
        elif not postCode[5].isdigit():
            print("Sixth Character Must Be A Number")
        else:
            break

    # Input Driver's Phone Number
    while True:
        phoneNum = input("Enter Phone Number (10 Digits): ")
        if not phoneNum.isdigit():
            print("Phone Number must only contain digits. Please Re-Enter")
        elif len(phoneNum) != 10:
            print("Phone Number must be 10 digits long. Please Re-Enter")
        else:
            break

    # Input Driver's License Number
    while True:
        driverLicenseNum = input("Enter Drivers License Number (1 Letter Then 9 Numbers) : ").capitalize()
        if not driverLicenseNum[0].isalpha():
            print("Driver's License Number Should Start With A Letter. Please Re-Enter")
        elif not driverLicenseNum[1:9].isdigit():
            print("Driver's License Number Should Start With A Letter than 9 Numbers. Please Re-Enter")
        elif len(driverLicenseNum) != 10:
            print("Driver's License Number Must Be 10 Characters Long. Please Re-Enter")
        else:
            break

    # Input Driver's License Expiry Date
    while True:
        try:
            licenseExpiry = input("Enter Drivers License Expiry Date (YYYY-MM-DD):  ")
            licenseExpiry = dt.datetime.strptime(licenseExpiry, "%Y-%m-%d")
            licenseExpiry = dt.datetime.strftime(licenseExpiry, "%Y-%m-%d")
        except:
            print("Invalid Date - Please Re-Enter")
        else:
            break

    # Input Driver's Insurance Company and Policy Number
    while True:
        insurPolComp = input("Enter Insurance Policy Company: ").title()
        if insurPolComp == "":
            print("Insurance Company cannot be Blank - Please Re-Enter")
        else:
            break

    while True:
        policyNum = input("Enter Insurance Policy Number: ")
        if policyNum == "":
            print("Policy Number cannot be Blank - Please Re-Enter")
        else:
            break

    # Ask If Driver Uses Their Own car, Rents Daily or Rents Weekly
    dailyRent = ""
    weeklyRent = ""
    while True:
        ownCar = input("Does Driver Own Car (Y for Yes/ N for No): ").upper()
        if ownCar == "Y":
            break
        elif ownCar == "N":
            dailyRent = input("Does Driver Rent Car Daily (Y for Yes/ N for No): ").upper()
            if dailyRent == "Y":
                break
            elif dailyRent == "N":
                weeklyRent = input("Does Driver Rent Car Weekly (Y for Yes/ N for No): ").upper()
                if weeklyRent == "Y":
                    break
                else:
                    print("No Option Chosen")

        else:
            print("Invalid Option")

    # Based On Own Car Or Rent Assign Balance Due
    # "car" Variable is For Display In File
    balDue = 0
    car = ""
    if ownCar == "Y":
        balDue = MON_STAND_FEE
        car = "Own Car"
    elif dailyRent == "Y":
        balDue = DAILY_RENT
        car = "Daily Rent"
    elif weeklyRent == "Y":
        balDue = WEEKLY_RENT
        car = "Weekly Rent"

    NEXT_TRANS_NUM += 1  # this is not appended below so it wont update
    NEXT_DRIVER_NUM += 1  # this now updates 1 at a time

    with open("defaults.dat", "w") as f:
        f.write("{}\n".format(str(NEXT_TRANS_NUM)))
        f.write("{}\n".format(str(NEXT_DRIVER_NUM)))
        f.write("{}\n".format(str(MON_STAND_FEE)))
        f.write("{}\n".format(str(DAILY_RENT)))
        f.write("{}\n".format(str(WEEKLY_RENT)))
        f.write("{}\n".format(str(TAX_RATE)))

    # Append All Inputs And Calculations For Driver Into "employee.dat" File
    with open("employees.dat", "a") as f:
        f.write("{}, ".format(str(NEXT_DRIVER_NUM)))
        f.write("{}, ".format(driverFirstName))
        f.write("{}, ".format(driverLastName))
        f.write("{}, ".format(stAdd))
        f.write("{}, ".format(city))
        f.write("{}, ".format(prov))
        f.write("{}, ".format(postCode))
        f.write("{}, ".format(phoneNum))
        f.write("{}, ".format(driverLicenseNum))
        f.write("{}, ".format(str(licenseExpiry)))
        f.write("{}, ".format(insurPolComp))
        f.write("{}, ".format(policyNum))
        f.write("{}, ".format(car))
        f.write("{}\n".format(str(balDue)))

    # Driver Dsp
    driversNameDsp = "{} {}".format(driverFirstName, driverLastName)
    driversLocationDsp = "{}, {}, {}".format(city, prov, postCode)

    balDueDSp = "${:,.2f}".format(balDue)

    print()
    print("===========================================")

    print("Driver Number:                        {:>5}".format(NEXT_DRIVER_NUM))
    print("Driver's Name:         {:>20}".format(driversNameDsp))
    print("Driver's Address:      {:>20}".format(stAdd))
    print("City:                  {:>20}".format(city))
    print("Province:                                {:>2}".format(prov))
    print("Postal Code:                         {:>6}".format(postCode))
    print("Driver's Phone Number:           {:>10}".format(phoneNum))
    print("Driver's License Number:         {:>10}".format(driverLicenseNum))
    print("License Expiry Date:             {:>10}".format(licenseExpiry))
    print("Insurance Company:     {:>20}".format(insurPolComp))
    print("Policy Number:                   {:>10}".format(policyNum))
    print("Own or Rent:                   {:>12}".format(car))
    print("Balance Due:                      {:>9}".format(balDueDSp))
    print("============================================")
    print()


def company_revenue():
    pass


def company_expenses():
    pass


def track_car_rentals():
    pass


def record_emp_payment():
    pass


def pr_comp_profit_tbl():
    totalRevAcc = 0
    totalExpenAcc = 0
    tranCounter = 0
    invoiceCounter = 0

    while True:
        try:
            startDate = input("Enter Start Date: ")
            startDate = dt.datetime.strptime(startDate, "%Y-%m-%d")
        except:
            print("Invalid Date - Please Re-Enter")
        else:
            break

    while True:
        try:
            endDate = input("Enter End Date: ")
            endDate = dt.datetime.strptime(endDate, "%Y-%m-%d")
        except:
            print("Invalid Date - Please Re-Enter")
        else:
            break

    print()
    print("                                               HAB Taxi Services")
    print("                                                Profit Listing")
    print("From: {}".format(startDate.strftime("%Y-%m-%d")))
    print("To:   {}".format(endDate.strftime("%Y-%m-%d")))
    print("                                     Driver")
    print("REVENUE        Date          ID      Number          Desc.             Amount       HST       Total    ")
    print("-------     =========================================================================================")

    with open("revenues.dat", "r") as f, open("expenses.dat", "r") as e:
        # Revenue File
        for revDataLine in f:
            revLine = revDataLine.split(", ")
            transID = revLine[0].strip()
            transDate = revLine[1].strip()
            revDesc = revLine[2].strip()
            revDriverNum = revLine[3].strip()
            revAmt = float(revLine[4].strip())
            revTax = float(revLine[5].strip())
            revTotal = float(revLine[6].strip())

            # Dsp For Revenue File
            revAmtDsp = Dollar(revAmt)
            revTaxDsp = Dollar(revTax)
            revTotalDsp = Dollar(revTotal)
            transDateDsp = dt.datetime.strptime(transDate, "%Y-%m-%d")

            if transDateDsp >= startDate and transDateDsp <= endDate:
                tranCounter += 1
                # Total Revenue
                totalRevAcc += revTotal
                totalRevAccDsp = Dollar(totalRevAcc)

                print("            {:<10}      {:<3}       {:>4}     {:<10}   {:>9}      {:>6}  {:>9}".format(transDate,
                                                                                                              transID,
                                                                                                              revDriverNum,
                                                                                                              revDesc,
                                                                                                              revAmtDsp,
                                                                                                              revTaxDsp,
                                                                                                              revTotalDsp))
        print("======================================================================================================")
        print(
            "TOTAL TRANSACTIONS: {:<3}                                                       TOTAL REVENUE: {:>9}".format
            (tranCounter, totalRevAccDsp))

        print()

        print("            Invoice     Inv    Driver     Item")
        print("EXPENSES     Date        #       #         #     Description   Cost     Qty  Subtotal   HST     Total")
        print("--------   ============================================================================================")

        # Expenses File
        for expenDataLine in e:
            expenLine = expenDataLine.split(", ")
            invoiceNum = expenLine[0].strip()
            invoiceDate = expenLine[1].strip()
            expenDriverNum = expenLine[2].strip()
            itemNum = expenLine[3].strip()
            expenDescrip = expenLine[4].strip()
            expenCost = float(expenLine[5].strip())
            quantity = expenLine[6].strip()
            subtotal = float(expenLine[8].strip())
            expenTax = float(expenLine[9].strip())
            expenTotal = float(expenLine[10].strip())

            # Dsp For Expenses File
            expenCostDsp = Dollar(expenCost)
            subtotalDsp = Dollar(subtotal)
            expenTaxDsp = Dollar(expenTax)
            expenTotalDsp = Dollar(expenTotal)
            invoiceDateDsp = dt.datetime.strptime(invoiceDate, "%Y-%m-%d")

            if invoiceDateDsp >= startDate and invoiceDateDsp <= endDate:
                invoiceCounter += 1
                # Total Expenses
                totalExpenAcc += expenTotal
                totalExpenAccDsp = Dollar(totalExpenAcc)

                print(
                    "           {:<10}  {:<5}    {:<4}     {:<5}    {:<10}  {:<9} {:>2}   {:<9} {:<9}{:<9}".format(
                        invoiceDate, invoiceNum,
                        expenDriverNum,
                        itemNum, expenDescrip,
                        expenCostDsp,
                        quantity, subtotalDsp,
                        expenTaxDsp,
                        expenTotalDsp))

        # Profit/Loss
        profit = totalRevAcc - totalExpenAcc

        # Dsp For Profit/Loss
        profitDsp = Dollar(profit)

    print("========================================================================================================")
    print(
        "TOTAL INVOICES: {:<3}                                                             TOTAL EXPENSES: {:<9}".format(
            invoiceCounter, totalExpenAccDsp))
    print()
    print("*********************************************************************************************************")
    print("                                                                                 Profit/Loss: {:>9}".format(
        profitDsp))
    print("*********************************************************************************************************")


def pr_comp_dr_fin_tbl():
    amtAcc = 0
    HSTAcc = 0
    totalAcc = 0
    tranCounter = 0

    driveNum = input("Enter the Driver's Number: ")

    while True:
        try:
            startDate = input("Enter Start Date: ")
            startDate = dt.datetime.strptime(startDate, "%Y-%m-%d")
        except:
            print("Invalid Date - Please Re-Enter")
        else:
            break

    while True:
        try:
            endDate = input("Enter End Date: ")
            endDate = dt.datetime.strptime(endDate, "%Y-%m-%d")
        except:
            print("Invalid Date - Please Re-Enter")
        else:
            break

    print()
    print("                             HAB Taxi Services")
    print("                          Driver Financial Listing")
    print()
    print("From: {}".format(startDate.strftime("%Y-%m-%d")))
    print("To:   {}".format(endDate.strftime("%Y-%m-%d")))
    print()
    print("   Tran.       Tran.                   ")
    print("   Date         ID         Desc.          Amount         HST         Total    ")
    print("============================================================================")

    with open("revenues.dat", "r") as f, open("expenses.dat", "r") as e:
        # Revenue File
        for revDataLine in f:
            revLine = revDataLine.split(", ")
            transID = revLine[0].strip()
            transDate = revLine[1].strip()
            revDesc = revLine[2].strip()
            revDriverNum = revLine[3].strip()
            revAmt = float(revLine[4].strip())
            revTax = float(revLine[5].strip())
            revTotal = float(revLine[6].strip())

            # Dsp For Revenue File
            revAmtDsp = Dollar(revAmt)
            revTaxDsp = Dollar(revTax)
            revTotalDsp = Dollar(revTotal)
            transDateDsp = dt.datetime.strptime(transDate, "%Y-%m-%d")

            if driveNum == revDriverNum and transDateDsp >= startDate and transDateDsp <= endDate:
                tranCounter += 1
                # Amount, HST, and Total Accumulators
                amtAcc += revAmt
                HSTAcc += revTax
                totalAcc += revTotal

                # Dsp For Accumulators
                amtAccDsp = Dollar(amtAcc)
                HSTAccDsp = Dollar(HSTAcc)
                totalAccDSp = Dollar(totalAcc)

                print("{:<10}     {:<3}   {:>10} {:>9}       {:>6}     {:>9}".format(transDate, transID, revDesc,
                                                                                     revAmtDsp,
                                                                                     revTaxDsp, revTotalDsp))

        print("============================================================================")
        print("TOTAL TRANSACTIONS: {:<2}                  {:>9}    {:>9}     {:>9}".format
              (tranCounter, amtAccDsp, HSTAccDsp, totalAccDSp))

        print()


while True:
    # Charge Drivers Standard Fee on 1st
    # todayDate = dt.datetime.today()
    # todayDate = input("Enter date: ")
    # todayDate = dt.datetime.strptime(todayDate, "%Y-%m-%d")
    # if todayDate.day == 1:
    #     todayDate = dt.datetime.strftime(todayDate, "%Y-%m-%d")
    #     tax = MON_STAND_FEE * TAX_RATE
    #     total = MON_STAND_FEE + tax
    #
    #     with open("revenue.dat", "a") as f:
    #         f.write("{},".format(str(NEXT_TRANS_NUM)))
    #         f.write("{},".format(str(todayDate)))
    #         f.write("{},".format("Monthly Stand Fees"))
    #         f.write("{},".format(str(NEXT_DRIVER_NUM)))
    #         f.write("{},".format(str(MON_STAND_FEE)))
    #         f.write("{},".format(str(tax)))
    #         f.write("{},".format(str(total)))
    #
    # NEXT_TRANS_NUM += 1
    # NEXT_DRIVER_NUM += 1
    #
    # with open("defaults.dat", "w") as f:
    #     f.write("{}\n".format(str(NEXT_TRANS_NUM)))
    #     f.write("{}\n".format(str(NEXT_DRIVER_NUM)))
    #     f.write("{}\n".format(str(MON_STAND_FEE)))
    #     f.write("{}\n".format(str(DAILY_RENT)))
    #     f.write("{}\n".format(str(WEEKLY_RENT)))
    #     f.write("{}\n".format(str(TAX_RATE)))

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
