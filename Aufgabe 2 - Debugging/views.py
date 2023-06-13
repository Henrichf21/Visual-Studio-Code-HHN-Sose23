from logic import sum_number 
def main():
    num1 = input("Erste Zahl eingeben: ")
    num2 = input("Zweite Zahl eingeben: ")
    result = sum_number(num1,num2)
    print(f"Die Summe von {num1} und {num2} = {result}")

main()
