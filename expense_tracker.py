# Personal Expense Tracker Program

expenses = []


def add_expense():
  item = input("खर्चे का नाम लिखें (जैसे: Books, Food): ")
  amount = float(input("कितने रुपये खर्च हुए: "))
  expenses.append({"item": item, "amount": amount})
  print(f"✅ '{item}' का ₹{amount} का खर्चा जुड़ गया है!\n")


def view_expenses():
  if not expenses:
    print("❌ अभी कोई खर्चा दर्ज नहीं है।\n")
    return

  print("\n--- आपके खर्चे की लिस्ट ---")
  total = 0
  for index, exp in enumerate(expenses, 1):
    print(f"{index}. {exp['item']}: ₹{exp['amount']}")
    total += exp["amount"]
  print(f"💰 कुल खर्चा: ₹{total}\n")


# Main Menu Loop
while True:
  print("=== Expense Tracker Menu ===")
  print("1. नया खर्चा जोड़ें (Add Expense)")
  print("2. कुल खर्चा देखें (View Expenses)")
  print("3. बाहर निकलें (Exit)")

  choice = input("अपना ऑप्शन चुनें (1/2/3): ")

  if choice == "1":
    add_expense()
  elif choice == "2":
    view_expenses()
  elif choice == "3":
    print("प्रोग्राम बंद हो गया है। धन्यवाद!")
    break
  else:
    print("गलत विकल्प! कृपया 1, 2 या 3 चुनें।\n")
