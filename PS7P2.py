"""
Fibonacci Sequence Generator
Generates and displays the first 20 numbers in the Fibonacci sequence
"""

def generate_fibonacci():
    """Generate and display first 20 Fibonacci numbers using a for loop"""

    print("First 20 numbers in the Fibonacci sequence:")
    print()

    # Initialize first two Fibonacci numbers
    first = 1
    second = 1

    # Display first two numbers
    print(f"1: {first}")
    print(f"2: {second}")

    # Generate remaining 18 numbers using for loop
    for position in range(3, 21):  # positions 3 through 20
        next_fib = first + second
        print(f"{position}: {next_fib}")

        # Update for next iteration
        first = second
        second = next_fib

def main():
    """Main function"""
    print("Fibonacci Sequence Generator")
    print("=" * 30)

    generate_fibonacci()

if __name__ == "__main__":
    main()