def create_sample_file():
        sample_data = """Widget
    10
    50.00
    Hammer
    2
    10.00
    Saw
    4
    8.00
    Screwdriver
    15
    5.50
    Wrench
    3
    12.75
    Drill
    1
    45.00
    Pliers
    6
    7.25"""

        with open('inventory.txt', 'w') as file:
            file.write(sample_data)
        print("Sample inventory file 'inventory.txt' created.")

def calculate_inventory(filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            lines = [line.strip() for line in lines]

            if len(lines) % 3 != 0:
                print("Error: File must contain groups of three lines (item, quantity, price)")
                return

            total_extended_price = 0.0
            order_count = 0

            print("Inventory Report")
            print("=" * 70)
            print("Item            Quantity    Price       Extended Price")
            print("-" * 70)

            for i in range(0, len(lines), 3):
                item_name = lines[i]
                quantity = int(lines[i + 1])
                price = float(lines[i + 2])

                extended_price = quantity * price

                print(item_name.ljust(15), str(quantity).ljust(11), "$" + str(price).ljust(10), "$" + str(extended_price))

                total_extended_price += extended_price
                order_count += 1

            average_order = total_extended_price / order_count if order_count > 0 else 0

            print("-" * 70)
            print("Summary:")
            print("Total extended prices: $" + str(total_extended_price))
            print("Number of orders: " + str(order_count))
            print("Average order: $" + str(average_order))

        except FileNotFoundError:
            print("Error: File '" + filename + "' not found.")
            print("Creating sample file...")
            create_sample_file()
            print("Please run the program again.")
        except ValueError:
            print("Error: Invalid number format in file.")
        except Exception as e:
            print("Error reading file: " + str(e))

def main():
        print("Inventory Calculator")
        print("=" * 30)

        calculate_inventory('inventory.txt')

if __name__ == "__main__":
        main()