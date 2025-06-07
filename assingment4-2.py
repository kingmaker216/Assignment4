filename="output.txt"

try:
        inputs = input("Enter text to write to the file: ")
        with open(filename, 'w') as file:
            file.write(inputs + "\n")
        print("Data successfully written to output.txt.")

        next_text = input("\nEnter additional text to append: ")
        with open(filename, 'a') as file:
            file.write(next_text + "\n")
        print("Data successfully appended.")

        print("\nFinal content of output.txt:")
        with open(filename, 'r') as file:
            final_content = file.read()
            print(final_content.strip())

except IOError :
        print("An  error occurred")
finally:
    print('operation completed')


