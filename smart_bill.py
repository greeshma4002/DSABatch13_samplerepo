cn=input("Customer Name : ")
item=input("Item Name : ")
qty=int(input("Quantity: "))
unitPrice=int(input("Price per unit (Rs):"))
lm=input("Loyalty member? (y/s): ")
paymode=input("Payment mode (cash/upi/card): ")

amt=qty*unitPrice
dis=0
lmb=0


print("="*50)
print("KERALA FRESH MART".center(50))
print("SMART BILLING".center(50))
print("="*50)

print()
print("Customer : ",cn)
print("-"*50)
print(f"{'Item':<20}{'Qty':^5}{'Price':>10}{'Amount':>15}")
print(f"{item:<20}{qty:^5}{unitPrice:>10}{amt:>15,.2f}")
print("-"*50)
print(f"{'Amount: '}{amt:>42,.2f}")

if(amt>=2000):
  print(f"{'Discount rate: '}{'10%':>35}")
  dis=amt*(10/100)
elif(1000<=amt<2000):
  print(f"{'Discount rate: '}{'5%':>35}")
  dis=amt*(5/100)
elif(500<=amt<1000):
  print(f"{'Discount rate: '}{'2%':>35}")
  dis=amt*(2/100)
else:
  print(f"{'Discount rate: '}{'0%':>35}")

print(f"{'Discount: '}{dis:>40,.2f}")

if(lm.lower()=="y" and amt>=500):
  print(f"{'Loyalty Bonus: '}{25.00:>35}")
  lmb=25.00
else:
  print(f"{'Loyalty Bonus: '}{0.00:>35}")
  lmb=0
txamt =amt-dis-lmb
gst=txamt*(5/100)
gTotal=txamt+gst
print(f"{'Taxable amount: '}{txamt:>34,.2f}")
print(f"{'GST (5%): '}{gst:>40,.2f}")
print(f"{'Grand Total: '}{gTotal:>37,.2f}")
print("="*50)

if(qty%12==0) :
  print("Bonous: Free cloth bag with this order!")
if(paymode.lower() != "cash" and paymode.lower() != "upi" and paymode.lower() != "card"):
  print("Invalid payment mode. Bill not settled.")
elif(gTotal>=10000 and paymode.lower()=="cash"):
  print("Cash limit of Rs 10,000 exceeded.Please pay by UPI or card.")
else:
  print(f"{"Payment accepted via "}{paymode.upper()}")