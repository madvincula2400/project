   

def create_sample_file():
        """Create a sample employee data file"""
        sample_data = """Adams
    50000.00
    Baker
    75000.00
    Smith
    45000.00
    Johnson
    125000.00
    Williams
    62000.00
    Brown
    38000.00
    Davis
    105000.00
    Miller
    52000.00"""

        with open('employees.txt', 'w') as file:
            file.write(sample_data)
        print("Sample employee file 'employees.txt' created.")

def determine_bonus_rate(salary):
        """Determine bonus rate based on salary"""
        if salary >= 100000.00:
            return 0.20  
        elif salary >= 50000.00:
            return 0.15  
        else:
            return 0.10  

def calculate_bonuses(filename):
        """Read employee data and calculate bonuses"""
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            
            lines = [line.strip() for line in lines]

            
            if len(lines) % 2 != 0:
                print("Error: File must contain pairs of data (name, salary)")
                return

            total_bonuses = 0.0

            print("Employee Bonus Report")
            print("=" * 50)
            print("Name            Salary       Bonus Rate   Bonus")
            print("-" * 50)

            
            for i in range(0, len(lines), 2):
                last_name = lines[i]
                salary = float(lines[i + 1])

                
                bonus_rate = determine_bonus_rate(salary)
                bonus = salary * bonus_rate

                
                print(last_name.ljust(15), "$" + format(salary, ",.2f").ljust(11), str(int(bonus_rate*100)) + "%".ljust(11), "$" + format(bonus, ",.2f").ljust(11))

                
                total_bonuses += bonus

            
            print("-" * 50)
            print("Total bonuses paid: $" + format(total_bonuses, ",.2f"))

        except FileNotFoundError:
            print("Error: File '" + filename + "' not found.")
            print("Creating sample file...")
            create_sample_file()
            print("Please run the program again.")
        except ValueError:
            print("Error: Invalid salary format in file.")
        except Exception as e:
            print("Error reading file: " + str(e))

def main():
        """Main function"""
        print("Employee Bonus Calculator")
        print("=" * 30)

        
        calculate_bonuses('employees.txt')

if __name__ == "__main__":
        main()