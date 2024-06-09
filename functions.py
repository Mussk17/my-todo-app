# note:
# filepath="todos.txt" (is a default-arg)
# default arg comes after non-default
# no need to repeat/write default arg everywhere
# this is modules
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list
    of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# print(f"__name__ is: {__name__}")

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
