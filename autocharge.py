import datetime as dt

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
    autoChargeCompleted = True


autoChargeCompleted = False

# MAIN MENU
while True:
    # Charge Drivers Standard Fee on 1st

    # Get todays date
    todayDate = "2022-01-01"
    todayDate = dt.datetime.strptime(todayDate, '%Y-%m-%d').date()

    # Perform auto-charge if it's the 1st of the month
    if todayDate.day == 1 and autoChargeCompleted == False:
        auto_mon_stand_fee()

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
