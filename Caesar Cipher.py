# Caesar Cipher 
message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))
action = input("Would you like to (E)ncrypt or (D)ecrypt?: ").lower()

result = ""

for char in message:
    if char.isalpha():
        base = 'A' if char.isupper() else 'a'
        shift_value = shift if action == 'e' else -shift
        result += chr((ord(char) - ord(base) + shift_value) % 26 + ord(base))
    else:
        result += char

print("Result:", result)
