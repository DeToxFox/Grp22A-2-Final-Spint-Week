# HAB Taxi Services

# Written by: Group 22A-2, Makenzie Roberts, Tyler Dinn, and David Turner
# Date written: April 11, 2022
# Project ID: Final Sprint Week. Project 2: HAB Taxi Services


import datetime as dt
import string

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
    # Welcome message
    print()
    print("     -----------------------------------------")
    print("      Option 1: Enter a New Employee (driver)")
    print("     -----------------------------------------")
    print()
    while True:
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
            driverFirstName = input("Enter Driver First Name (type \"End\" to exit to main menu): ").title()
            if driverFirstName == "End":
                print()
                return
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

        # counter for the next driver number
        NEXT_DRIVER_NUM += 1  # this now updates 1 at a time

        # update defaults file
        with open("defaults.dat", "w") as f:
            f.write("{}\n".format(str(NEXT_TRANS_NUM)))
            f.write("{}\n".format(str(NEXT_DRIVER_NUM)))
            f.write("{}\n".format(str(MON_STAND_FEE)))
            f.write("{}\n".format(str(DAILY_RENT)))
            f.write("{}\n".format(str(WEEKLY_RENT)))
            f.write("{}\n".format(str(TAX_RATE)))

        # string.capwords, if any string has an apostrophe the letter after stays lowercase, St. John's,
        # where .title() will display St. John'S, the letter at the end would be capitalized
        city_Dsp = string.capwords(city)

        # Append All Inputs And Calculations For Driver Into "employee.dat" File
        with open("employees.dat", "a") as f:
            f.write("{}, ".format(str(NEXT_DRIVER_NUM)))
            f.write("{}, ".format(driverFirstName))
            f.write("{}, ".format(driverLastName))
            f.write("{}, ".format(stAdd))
            f.write("{}, ".format(city_Dsp))
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
        balDueDSp = "${:,.2f}".format(balDue)
        print()
        print()
        print(" " * 12, "HAB Taxi Services")
        print(" " * 8, "New Employee Information")
        print("===========================================")

        print("Driver Number:                        {:>5}".format(NEXT_DRIVER_NUM))
        print("Driver's Name:         {:>20}".format(driversNameDsp))
        print("Driver's Address:      {:>20}".format(stAdd))
        print("City:                  {:>20}".format(city_Dsp))
        print("Province:                                {:>2}".format(prov))
        print("Postal Code:                         {:>6}".format(postCode))
        print("Driver's Phone Number:           {:>10}".format(phoneNum))
        print("Driver's License Number:         {:>10}".format(driverLicenseNum))
        print("License Expiry Date:             {:>10}".format(licenseExpiry))
        print("Insurance Company:     {:>20}".format(insurPolComp))
        print("Policy Number:                   {:>10}".format(policyNum))
        print("Own or Rent:                   {:>12}".format(car))
        print("Balance Due:                      {:>9}".format(balDueDSp))
        print("===========================================")
        print()

        while True:
            Continue = input("Do you want to enter another new employee  (Y / N): ").upper()
            print()
            if Continue != "Y" and Continue != "N":
                print("Not Valid Try Again")
            else:
                break
        if Continue == "N":
            break

print()
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
    # Welcome message
    print()
    print("     ------------------------------------------")
    print("          Option 6: Company Profit Listing")
    print("     ------------------------------------------")
    print()
    while True:
            totalRevAcc = 0
            totalExpenAcc = 0
            tranCounter = 0
            invoiceCounter = 0
            monFeeCounter = 0
            dailyFeeCounter = 0
            weekFeeCounter = 0

            while True:
                try:
                    startDate = input("Enter Start Date (YYYY-MM-DD): ")
                    startDate = dt.datetime.strptime(startDate, "%Y-%m-%d")
                except:
                    print("Invalid Date - Please Re-Enter")
                else:
                    break

            while True:
                try:
                    endDate = input("Enter End Date (YYYY-MM-DD): ")
                    endDate = dt.datetime.strptime(endDate, "%Y-%m-%d")
                except:
                    print("Invalid Date - Please Re-Enter")
                else:
                    if endDate < startDate:
                        print("End Date Can't Be Before The Start Date")
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
                        if revDesc == "Monthly Stand Fees":
                            monFeeCounter += 1
                        elif revDesc == "Daily Rental Fees":
                            dailyFeeCounter += 1
                        elif revDesc == "Weekly Rental Fees":
                            weekFeeCounter += 1

                        tranCounter += 1
                        # Total Revenue
                        totalRevAcc += revTotal

                        print("            {:<10}      {:<3}       {:>4}     {:<10}   {:>9}      {:>6}  {:>9}".format(transDate,
                                                                                                                      transID,
                                                                                                                      revDriverNum,
                                                                                                                      revDesc,
                                                                                                                      revAmtDsp,
                                                                                                                      revTaxDsp,
                                                                                                                      revTotalDsp))
                    else:
                        # Add nothing to counters and accumulators if not within date range
                        totalRevAcc += 0

                totalRevAccDsp = Dollar(totalRevAcc)

                if tranCounter == 0:
                    print("{:^104}".format("N/A"))


                print("======================================================================================================")
                print(
                    "TOTAL TRANSACTIONS: {:<3}                                                TOTAL REVENUE:   {:>11}".format
                    (tranCounter, totalRevAccDsp))
                print("              Monthly Standard Trans: {:<3}   Daily Rent Trans: {:<3}  Weekly Rent Trans: {:>3}".format(
                    monFeeCounter, dailyFeeCounter, weekFeeCounter))
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

                        print(
                            "           {:<10}  {:<5}    {:<4}     {:<5}    {:<10}  {:<9} {:>2}   {:<9} {:<9}{:<9}".format(
                                invoiceDate, invoiceNum,
                                expenDriverNum,
                                itemNum, expenDescrip,
                                expenCostDsp,
                                quantity, subtotalDsp,
                                expenTaxDsp,
                                expenTotalDsp))
                    else:
                        # If not inside date range, add nothing to the accumulator
                        totalExpenAcc += 0

                    # Dsp for expense accumulator
                    totalExpenAccDsp = Dollar(totalExpenAcc)

                # Profit/Loss
                profit = totalRevAcc - totalExpenAcc

                # Dsp For Profit/Loss
                profitDsp = Dollar(profit)

            if invoiceCounter == 0:
                print("{:^104}".format("N/A"))



            print("=======================================================================================================")
            print(
                "TOTAL INVOICES: {:<3}                                                       TOTAL EXPENSES:   {:>11}".format(
                    invoiceCounter, totalExpenAccDsp))
            print()
            print("*******************************************************************************************************")
            if profit >= 0:
                print(
                    "                                                                                  Profit:   {:>11}".format(
                        profitDsp))
                print(
                    "*******************************************************************************************************")
            else:
                print(
                    "                                                                                    Loss:   {:>11}".format(
                        profitDsp))
                print("*******************************************************************************************************")
            print()
            while True:
                Continue = input("Do you want to enter another date range for the Profit Listing  (Y / N): ").upper()
                print()
                if Continue != "Y" and Continue != "N":
                    print("Not Valid Try Again")
                else:
                    break
            if Continue == "N":
                break


def pr_comp_dr_fin_tbl():
    while True:
        # Welcome message
        print()
        print("     ------------------------------------------")
        print("         Option 7: Driver Financial Listing")
        print("     ------------------------------------------")
        print()
        amtAcc = 0
        HSTAcc = 0
        totalAcc = 0
        tranCounter = 0

        print()
        print(" Driver's         Driver's")
        print("  Name             Number")
        print("==========================")

        employNumList = []

        with open("employees.dat", "r") as f:
            for employDataLine in f:
                employLine = employDataLine.split(", ")
                employNum = employLine[0].strip()
                employFirstName = employLine[1].strip()
                employLastName = employLine[2].strip()

                employName = "{} {}".format(employFirstName, employLastName)
                print("{:<15}     {:<4}".format(employName, employNum))



                employNumList.append(employNum)



            print("==========================")
            print()

        while True:
            allowed_chars = set('1234567890 ')
            driverNumInput = input("Enter the Driver Number: ")
            if driverNumInput == "" or driverNumInput.isspace() == True:
                print("The driver number cannot be blank. Please re-enter.")
            elif set(driverNumInput).issubset(allowed_chars) == False:
                print("The driver number must include digits only. Please re-enter.")
            elif driverNumInput not in employNumList:
                print("The driver number {} cannot be found. Please re-enter".format(driverNumInput))
            else:
                break

        f = open("employees.dat", "r")
        for empData in f:
            empLine = empData.split(",")
            empNum = empLine[0].strip()
            empFirstName = empLine[1].strip()
            empLastName = empLine[2].strip()

            if empNum == driverNumInput:
                empFullName = empFirstName + " " + empLastName
            else:
                pass

        f.close()

        while True:
            try:
                startDate = input("Enter Start Date (YYYY-MM-DD): ")
                startDate = dt.datetime.strptime(startDate, "%Y-%m-%d")
            except:
                print("Invalid Date - Please Re-Enter")
            else:
                break
        while True:
            try:
                endDate = input("Enter End Date (YYYY-MM-DD): ")
                endDate = dt.datetime.strptime(endDate, "%Y-%m-%d")
            except:
                print("Invalid Date - Please Re-Enter")
            else:
                if endDate < startDate:
                    print("End Date Can't Be Before The Start")
                else:
                    break


        print()
        print("                             HAB Taxi Services")
        print("                          Driver Financial Listing")
        print()
        print("From: {}          Drivers Number: {} ".format(startDate.strftime("%Y-%m-%d"), driverNumInput))
        print("To:   {}          Drivers Name:   {} ".format(endDate.strftime("%Y-%m-%d"), empFullName))
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

                if driverNumInput == revDriverNum and transDateDsp >= startDate and transDateDsp <= endDate:
                    tranCounter += 1
                    # # Amount, HST, and Total Accumulators
                    amtAcc += revAmt
                    HSTAcc += revTax
                    totalAcc += revTotal

                    print("{:<10}     {:<3}   {:>10} {:>9}       {:>6}     {:>9}".format(transDate, transID, revDesc,
                                                                                         revAmtDsp,
                                                                                         revTaxDsp, revTotalDsp))
                else:
                    # Amount, HST, and Total Accumulators
                    amtAcc += 0
                    HSTAcc += 0
                    totalAcc += 0

                    # Dsp For Accumulators

                amtAccDsp = Dollar(amtAcc)
                HSTAccDsp = Dollar(HSTAcc)
                totalAccDSp = Dollar(totalAcc)
            if tranCounter == 0:
                print("{:^76}".format("N/A"))
            print("============================================================================")
            print("TOTAL TRANSACTIONS: {:<2}                  {:>9}    {:>9}   {:>11}".format
                  (tranCounter, amtAccDsp, HSTAccDsp, totalAccDSp))
            print()
            while True:
                Continue = input("Do you want to enter another driver number and date range for the Driver Financial Listing (Y / N): ").upper()
                print()
                if Continue != "Y" and Continue != "N":
                    print("Not Valid Try Again")
                else:
                    break
            if Continue == "N":
                break


def auto_mon_stand_fee():
    dflt = open("defaults.dat", "r")
    NEXT_TRANS_NUM = int(dflt.readline())
    NEXT_DRIVER_NUM = int(dflt.readline())
    MON_STAND_FEE = float(dflt.readline())
    DAILY_RENT = float(dflt.readline())
    WEEKLY_RENT = float(dflt.readline())
    TAX_RATE = float(dflt.readline())
    dflt.close()

    hstAmt = MON_STAND_FEE * (TAX_RATE)
    total = MON_STAND_FEE + hstAmt
    dflt.close()

    with open("employees.dat", "r") as emp, open("revenues.dat", "a+") as rev, open("defaults.dat", "w") as dflt:
        for line in emp:
            empLine = line.split(",")
            driverNum = empLine[0]
            newRevLine = "{}, {}, Monthly Stand Fees, {}, {}, {}, {}".format(NEXT_TRANS_NUM, todayDate, driverNum,
                                                                             MON_STAND_FEE, hstAmt, total)
            NEXT_TRANS_NUM += 1
            rev.write("{}\n".format(newRevLine))

        dflt.write("{}\n".format(NEXT_TRANS_NUM))
        dflt.write("{}\n".format(NEXT_DRIVER_NUM))
        dflt.write("{}\n".format(MON_STAND_FEE))
        dflt.write("{}\n".format(DAILY_RENT))
        dflt.write("{}\n".format(WEEKLY_RENT))
        dflt.write("{}\n".format(TAX_RATE))


autoChargeCompleted = False

# MAIN MENU
while True:
    # Charge Drivers Standard Fee on 1st

    # NOTE: IF IT IS NOT THE 1ST, THE AUTO-CHARGE WILL NOT HAPPEN.
    #       TO TEST, MANUALLY DEFINE THE DATE AS A VARIABLE

    # Get today's date
    todayDate = dt.datetime.today().date()

    searchDesc = "Monthly Stand Fees"
    autoChargeCount = 0

    # Search revenue file for if auto-charges are needed (If they've already been charged this month)
    f = open("revenues.dat", "r")
    for revData in f:
        revLine = revData.split(",")
        revDate = revLine[1].strip()
        revDesc = revLine[2].strip()
        revDate = dt.datetime.strptime(revDate, '%Y-%m-%d').date()

        if revDate == todayDate and revDesc == searchDesc:  # If Monthly Stand Fees were already charged today
            autoChargeCount += 1
        else:
            autoChargeCount += 0
    f.close()

    # If there are 0 auto-charges with today's date, autoChargeNeeded is True.
    if autoChargeCount == 0:
        autoChargeNeeded = True
    else:
        autoChargeNeeded = False

    # Perform auto-charge if it's the 1st of the month
    # 'autoChargeCompleted' tells the program if it has already happened once this RUN
    # 'autoChargeNeeded' tells the program if it had already happened once this MONTH
    if todayDate.day == 1 and autoChargeNeeded == True and autoChargeCompleted == False:
        auto_mon_stand_fee()
        autoChargeCompleted = True


    # Main

    print()
    print(" " * 10, "HAB Taxi Services")
    print(" " * 7, "Company Services System")
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