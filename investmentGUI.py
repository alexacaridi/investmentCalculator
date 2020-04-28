"""
Program: investmentGUI.py
Alexa Caridi 4/28/2020

GUI-based investment program
1.Inputs:
    starting investment amount
    number of years
    interest rate (an integer %)
2.The report is displayed in tabular format
3.Compute interst for each year and add it to the investment
4.Display the ending investment and interest earned as final output
"""

from breezypythongui import EasyFrame

class InvestmentGUI(EasyFrame):
    #an investment calculator that demonstrates the use of multi-line text area
    def __init__(self):
        EasyFrame.__init__(self, title="Investment Calculator")

        #labels for the window
        self.addLabel(text="Initial amount", row=0, column=0)
        self.addLabel(text="Number of years", row=1, column=0)
        self.addLabel(text="Interest rate in %", row=2, column=0)

        #entry fields for inputs
        self.amount = self.addFloatField(value=0.0, row=0, column=1)
        self.period = self.addIntegerField(value=0, row=1, column=1)
        self.rate = self.addIntegerField(value=0, row=2, column=1)

        #button widget
        self.compute = self.addButton(text="Compute", row=3, column=0, columnspan=2, command=self.compute)

        #text-area widget
        self.outputArea = self.addTextArea("", row=4, column=0, columnspan=2, width=50, height=15)

    #event handling method- trigger for button being clicked on
    def compute(self):
        #computes the investment schedule based on the inputs & outputs the schedule
        #obtain and validate the inputs
        startBalance = self.amount.getNumber()
        rate = self.rate.getNumber() / 100
        years = self.period.getNumber()
        if startBalance == 0 or rate == 0 or years == 0:
            return

        #set the header for the table
        result = "%4s%18s%10s%16s\n" % ("Year", "Starting blance", "Interest", "Ending balnce")

        #compute and append the results for each year
        totalInterest = 0.0
        for year in range(1, years+1):
            interest = startBalance * rate
            endBalance = startBalance + interest
            result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
            startBalance = endBalance
            totalInterest += interest
        
        #append the totals for the period
        result += "Ending balance: $%0.2f\n" % endBalance
        result += "Total interest earned: $%0.2f\n" % totalInterest

        #output the result while preserving read-only status
        self.outputArea["state"] = "normal"
        self.outputArea.setText(result)
        self.outputArea["state"] = "disabled"

def main():
    InvestmentGUI().mainloop()

main()

