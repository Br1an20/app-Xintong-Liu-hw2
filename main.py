from mongoengine import connect
from brain import process_input

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_database_name = input("Enter a database name: ")
    if input_database_name == 'newdb':
        connect('newdb')
    else:
        connect('appxintong2')
    main_prompt = """
            ====== MENU =======
            Type 'checkout' to borrow a book
            Type 'return' to return a book
            Type 'reset' to reset the database
            Type 'books' to display all the book status
            Type 'exit' to end the program
            Enter a command: """

    print("=================== Welcome to CMU. ===================")
    user_input = input(main_prompt)

    while user_input != "exit":
        process_input(user_input)
        user_input = input(main_prompt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
