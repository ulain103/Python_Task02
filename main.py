class ComputerShop:
    def __init__(self):
        # Define arrays to store item information
        self.case_items = [("A1", "Compact", 75.00), ("A2", "Tower", 150.00)]
        self.ram_items = [("B1", "8 GB", 79.99), ("B2", "16 GB", 149.99), ("B3", "32 GB", 299.99)]
        self.hdd_items = [("C1", "1 TB HDD", 49.99), ("C2", "2 TB HDD", 89.99), ("C3", "4 TB HDD", 129.99)]

        # Initialize selected items and computer price
        self.selected_items = {"Case": None, "RAM": None, "HDD": None}
        self.basic_components_cost = 200.00
        self.computer_price = self.basic_components_cost

    def choose_item(self, category, items):
        print(f"\nAvailable {category} items:")
        for item in items:
            print(f"{item[0]} - {item[1]} (${item[2]:.2f})")

        while True:
            choice = input(f"Choose a {category} item (Enter item code): ").strip().upper()
            if any(choice == item[0] for item in items):
                return choice
            else:
                print("Invalid item code. Please try again.")

    def calculate_and_display_price(self, additional_items):
        num_additional_items = len(additional_items)
        discount = 0

        if num_additional_items == 1:
            discount = 0.05
        elif num_additional_items >= 2:
            discount = 0.10

        discounted_price = self.computer_price * (1 - discount)
        amount_saved = self.computer_price - discounted_price

        print("\nSelected Items:")
        for item in additional_items:
            print(f"{item[1]} (${item[2]:.2f})")

        print(f"Computer Price (before discount): ${self.computer_price:.2f}")
        print(f"Discount: {discount * 100}%")
        print(f"Amount Saved: ${amount_saved:.2f}")
        print(f"Computer Price (after discount): ${discounted_price:.2f}")

    def run_task_1(self):
        print("Welcome to the Online Computer Shop!")
        self.selected_items["Case"] = self.choose_item("Case", self.case_items)
        self.selected_items["RAM"] = self.choose_item("RAM", self.ram_items)
        self.selected_items["HDD"] = self.choose_item("Main Hard Disk Drive", self.hdd_items)

        # Calculate the initial computer price
        for item in self.selected_items.values():
            self.computer_price += next(i[2] for i in (self.case_items + self.ram_items + self.hdd_items) if i[0] == item)

        print("\nInitial Computer Configuration:")
        for category, item_code in self.selected_items.items():
            item_info = next(i for i in getattr(self, f"{category.lower()}_items") if i[0] == item_code)
            print(f"{category}: {item_info[1]} (${item_info[2]:.2f})")

        print(f"Computer Price (before additional items): ${self.computer_price:.2f}")

    def run_task_2(self):
        additional_items = []
        while True:
            additional = input("Do you want to purchase additional items (Y/N)? ").strip().lower()

            if additional == "n":
                break
            elif additional == "y":
                additional_category = input("Enter the category of the additional item (e.g., SSD, Optical Drive): ").strip().lower()

                if additional_category in ["ssd", "second hdd", "optical drive"]:
                    items = getattr(self, f"{additional_category}_items")
                    additional_item = self.choose_item(additional_category.capitalize(), items)
                    additional_items.append([additional_item, items[0][1], next(i[2] for i in items if i[0] == additional_item)])
                    self.computer_price += additional_items[-1][2]
                else:
                    print("Invalid category. Please try again.")

        print("\nAdditional Items:")
        for item in additional_items:
            print(f"{item[1]} (${item[2]:.2f})")

        print(f"Computer Price (after additional items): ${self.computer_price:.2f}")

        self.calculate_and_display_price(additional_items)

    def run_task_3(self):
        self.calculate_and_display_price([])  # Display initial price without additional items


# Create an instance of the ComputerShop class
computer_shop = ComputerShop()

# Run Task 1
computer_shop.run_task_1()

# Run Task 2
computer_shop.run_task_2()

# Run Task 3
computer_shop.run_task_3()
