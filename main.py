from datetime import datetime
class BudgetManager():
    
    def __init__(self,balance):
        self.transactions  =[]
        self.__balance = balance
        
    def add_transaction(self, transaction):

        """print("TYPE:", transaction.transaction_type)
        print("AMOUNT:", transaction.amount)"""

        

        if transaction.transaction_type == "income":
            self.__balance += transaction.amount

        elif transaction.transaction_type == "expense":
            if transaction.amount > self.__balance:
                raise ValueError("Balansınızda kifayət qədər pul yoxdur")

            self.__balance -= transaction.amount
        self.transactions.append(transaction)
        print("YENİ BALANS:", self.__balance)
        

        
        
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        
        if value <0:
            raise ValueError("mebleg menfi ola bilmez")
        self.__balance =value
        

        
class Transaction:
    def __init__(self,amount,type,description,date):
        if amount <0:
            raise ValueError("daxil edilen mebleg menfi ola bilmez")
        self.amount = amount
        self.transaction_type = type
        self.description = description
        self.date = date






def get_amount():
    while True:
        try:
            amount = int(input("Məbləğ daxil edin: "))
            return amount
        except ValueError:
            print("Zəhmət olmasa eded daxil edin.")
def get_date():
    while True:
        try:
            date_input = input("Tarix(year-month-day): ")
            return datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Tarix düzgün deyil.")


   


def get_description():
    while True:
        description = input("Açıqlama: ").strip()

        if description:
            return description

        print("Açıqlama hissesini doldurun")
def create_transaction(transaction_type):
    amount = get_amount()
    description = get_description()
    date = get_date()

    return Transaction(
        amount,
        transaction_type,
        description,
        date
    )
"""transaction = create_transaction()"""

"""print(transaction.amount)
print(transaction.transaction_type)
print(transaction.description)
print(transaction.date)"""
            



        
        


def filter_by_date(transactions, start_date, end_date):
    filtered_transactions = []

    for transaction in transactions:
        if start_date <= transaction.date <= end_date:
            filtered_transactions.append(transaction)

    return filtered_transactions
          
def save_to_file(transactions):
    with open("transactions.txt", "w") as file:
        for transaction in transactions:
            file.write(
                f"{transaction.amount}|"
                f"{transaction.transaction_type}|"
                f"{transaction.description}|"
                f"{transaction.date}\n"
            )
def load_from_file(manager):
    try:
        with open("transactions.txt", "r") as file:

            for line in file:
                line = line.strip()

                if not line:
                    continue

                amount, transaction_type, description, date = line.split("|")

                amount = int(amount)

                date = datetime.strptime(
                    date,
                    "%Y-%m-%d %H:%M:%S"
                )

                transaction = Transaction(
                    amount,
                    transaction_type,
                    description,
                    date
                )

                manager.transactions.append(transaction)

                if transaction_type == "income":
                    manager.balance += amount

                elif transaction_type == "expense":
                    manager.balance -= amount

    except FileNotFoundError:
        print("transactions.txt faylı movcud deyil")

def menu(manager):
    while True:

        print("\n--- ŞƏXSİ BÜDCƏ ---")
        print("1. Gəlir əlavə et")
        print("2. Xərc əlavə et")
        print("3. Balansı göstər")
        print("4. Əməliyyatları göstər")
        print("5. Tarixə görə filtr et")
        print("6. Fayla yadda saxla")
        print("7. Çıxış")

        choice = input("Seçim: ")

        try:

            if choice == "1":
                transaction = create_transaction("income")
                manager.add_transaction(transaction)
                print("Gəlir əlavə edildi.")

            elif choice == "2":
                transaction = create_transaction("expense")
                manager.add_transaction(transaction)
                print("Xərc əlavə edildi.")

            elif choice == "3":
                print("Balans:",manager.balance)

            elif choice == "4":
                if not manager.transactions:
                    print("Heç bir əməliyyat yoxdur.")
                else:
                    for transaction in manager.transactions:
                        print(
                            f"Məbləğ: {transaction.amount} | "
                            f"Növ: {transaction.transaction_type} | "
                            f"Açıqlama: {transaction.description} | "
                            f"Tarix: {transaction.date}"
                        )

            elif choice == "5":
                start_date = get_date()
                end_date = get_date()

                filtered = filter_by_date(
                    manager.transactions,
                    start_date,
                    end_date
                )

                for transaction in filtered:
                    print(
                        f"Məbləğ: {transaction.amount} | "
                        f"Növ: {transaction.transaction_type} | "
                        f"Açıqlama: {transaction.description} | "
                        f"Tarix: {transaction.date}"
                    )

            elif choice == "6":
                save_to_file(manager.transactions)
                print("Fayla yadda saxlanıldı.")

            elif choice == "7":
                save_to_file(manager.transactions)
                print("Proqramdan çıxılır...")
                break

            else:
                print("Yanlış seçim.")

        except ValueError as error:
            print("Xəta:", error)




manager = BudgetManager(1200)

load_from_file(manager)

menu(manager)










