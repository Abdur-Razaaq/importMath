# Import the math module to use the gcd function
import math

# Define a function to check if the books can be organized based on their counts
def can_organize_books(shelf):
    # Initialize the current_gcd with the first book count from the shelf
    current_gcd = shelf[0]
    
    # Loop through the remaining book counts in the shelf
    for count in shelf[1:]:
        # Update the current_gcd by finding the gcd between the current_gcd and the next book count
        current_gcd = math.gcd(current_gcd, count)
    
    # If the final gcd is greater than 1, return "YES" (indicating the books can be organized)
    # Otherwise, return "NO" (indicating they cannot be organized)
    return "YES" if current_gcd > 1 else "NO"

# List of book counts on the shelf
shelf = [1234567, 1234567, 2345678, 2345678, 3456789, 3456789, 1234567, 2345678, 3456789, 
         4567890, 4567890, 5678901, 5678901, 6789012, 6789012, 1234567, 2345678, 3456789, 
         4567890, 5678901, 4567890, 5678901]

# Call the function to check if the books can be organized and print the result
print(can_organize_books(shelf))