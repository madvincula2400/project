def create_sample_file():
        sample_data = """Jones
    I
    12
    Adams
    I
    10
    Baker
    O
    12
    Smith
    O
    16
    Wilson
    I
    15
    Johnson
    O
    8
    Brown
    I
    14
    Davis
    O
    18"""

        with open('students.txt', 'w') as file:
            file.write(sample_data)
        print("Sample student file 'students.txt' created.")

def calculate_tuition(filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            lines = [line.strip() for line in lines]

            if len(lines) % 3 != 0:
                print("Error: File must contain groups of three lines (name, district code, credits)")
                return

            total_tuition = 0.0
            student_count = 0

            print("Student Tuition Report")
            print("=" * 50)
            print("Student Name    Credits    Tuition Owed")
            print("-" * 50)

            for i in range(0, len(lines), 3):
                last_name = lines[i]
                district_code = lines[i + 1].upper()
                credits = int(lines[i + 2])

                if district_code == 'I':
                    cost_per_credit = 250.00
                else:
                    cost_per_credit = 500.00

                tuition_owed = credits * cost_per_credit

                print(last_name.ljust(15), str(credits).ljust(10), "$" + str(tuition_owed))

                total_tuition += tuition_owed
                student_count += 1

            print("-" * 50)
            print("Summary:")
            print("Total tuition owed: $" + str(total_tuition))
            print("Number of students: " + str(student_count))

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
        print("Student Tuition Calculator")
        print("=" * 30)

        calculate_tuition('students.txt')

if __name__ == "__main__":
        main()