def uppercase(input_str):
    return input_str.upper()
def lowercase(input_str):
    return input_str.lower()
def capitalize(input_str):
    return input_str.capitalize()
def reverse(input_str):
    return input_str[::-1]
def title_case(input_str):
    return input_str.title(
def swapcase(input_str):
    return input_str.swapcase()
def strip_whitespace(input_str):
    return input_str.strip()
def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_str if char in vowels)
def is_palindrome(input_str):
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]
def main():
    user_input = input("Enter a string: ")
    options = {
        '1': uppercase,
        '2': lowercase,
        '3': capitalize,
        '4': reverse,
        '5': title_case,
        '6': swapcase,
        '7': strip_whitespace,
        '8': count_vowels,
        '9': is_palindrome
    }
    print("\nChoose a string operation:")
    print("1. Uppercase")
    print("2. Lowercase")
    print("3. Capitalize")
    print("4. Reverse")
    print("5. Title Case")
    print("6. Swapcase")
    print("7. Strip Whitespace")
    print("8. Count Vowels")
    print("9. Check Palindrome")
    choice = input("Enter your choice (1-9): ")
    selected_function = options.get(choice, None)
    if selected_function:
        result = selected_function(user_input)
        print("Result:", result)
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
if __name__ == "__main__":
    main()
