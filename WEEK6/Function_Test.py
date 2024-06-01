def process_to_print (text_to_print):
    global cycle
    print(f"Process {cycle}: {text_to_print}")
    cycle += 1

def first_function (text_to_print):
    text_to_print = text
    process_to_print(text_to_print)
    second_function(text_to_print)

def second_function(text_to_print):
    text_second_function = text_to_print
    process_to_print(text_second_function)


cycle = 1
text = input("Enter a text: \n")
while cycle < 10:
    first_function(text)