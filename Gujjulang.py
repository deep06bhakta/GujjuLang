# Here are all the grammar interpretation from Gujarati to python
def gujjulang_to_python(code):
    translations = {
        'aa che ': '',
        'bolo(': 'print(',
        'jo ': 'if ',
        'ane jo ': 'elif ',
        'naito': 'else',
        'kaini': 'None',
        'jyare ': 'for ',
        ' hoi(': ' in range(',
        'jya sodhi ': 'while ',
        'prayas karo:': 'try:',
        'sivay:': 'except:'
    }


    # Translate Gujjulang to Python
    for gujju, py in translations.items():
        code = code.replace(gujju, py)
    
    # Additional check for 'prayas karo' and 'sivay'
    if 'prayas karo:' in code:
        code = code.replace('prayas karo:', 'try:')
    if 'sivay:' in code:
        code = code.replace('sivay:', 'except:')

    # Handling do-while loop
    while 'jya sodhi{' in code:
        start = code.find('jya sodhi{')
        end = code.find('}karo(', start)
        condition = code[end + 6:code.find(')', end)]
        do_while_body = code[start + 6:end]
        # Convert to a while loop with a condition at the end
        python_while = f"while True:\n{do_while_body}\n    if not({condition}):\n        break\n"
        code = code[:start] + python_while + code[code.find(')', end) + 1:]
    return code


def read_gujjulang_code(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Replace 'your_gujjulang_file.txt' with the path to your Gujjulang code file
gujjulang_file_path = 'test.gj'
gujjulang_code = read_gujjulang_code(gujjulang_file_path)


# Example usage
gujjulang_code = """

bolo("--------------------------------------------------------")
bolo("Test Case: 1")
bolo("--------------------------------------------------------")
bolo(" ")

aa che x = 0
jyare i hoi(1, 101):
    bolo(i)
bolo(" ")

bolo("--------------------------------------------------------")
bolo("Test Case: 2")
bolo("--------------------------------------------------------")

aa che num1 = 4 + 2
aa che num2 = 5 + 1

jo num1 == num2:
    bolo("Sarkha che")
jo num1 > num2:
    bolo("Num 1 moto che")
jo num2 > num2:
    bolo("Num 2 moto che")
jo num1 < num2:
    bolo("Num 1 nano che")
jo num2 < num2:
    bolo("Num 2 nano che")
naito:
    kaini
    bolo(" ")


bolo("--------------------------------------------------------")
bolo("Test Case: 3")
bolo("--------------------------------------------------------")

jya sodhi x < 10:
    bolo(x)
    x = x + 1

bolo("--------------------------------------------------------")
bolo("Test Case: 4")
bolo("--------------------------------------------------------")

prayas karo:
    bolo(10 / 5)
sivay:
    bolo("Division by zero error caught")

"""


# Now use this function to translate and then execute your Gujjulang code
translated_code = gujjulang_to_python(gujjulang_code)
print("Translated Python Code:\n", translated_code)

# Execute the translated code
try:
    exec(translated_code)
except SyntaxError as e:
    print("There is a syntax error in the translated code:", e)