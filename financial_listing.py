import datetime as dt


def Dollar(num):
    dollar = "${:,.2f}".format(num)
    return dollar


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

            print("{:<10}     {:<3}   {:>10} {:>9}       {:>6}     {:>9}".format(transDate, transID, revDesc, revAmtDsp,
                                                                                 revTaxDsp, revTotalDsp))

    print("============================================================================")
    print("TOTAL TRANSACTIONS: {:<2}                  {:>9}    {:>9}    {:>9}".format
          (tranCounter, amtAccDsp, HSTAccDsp, totalAccDSp))

    print()
