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


    # Added a loop to iterate over the translations that we have already initiated above.
    # This allows the python interpreter to acknowledge the initialized translations
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

# The function helps reading the gj file that is in the same folder
def read_gujjulang_code(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Replace 'your_gujjulang_file.txt' with the path to your Gujjulang code file
gujjulang_file_path = 'test.gj' # Could be named whatever e.g .txt, .gj
gujjulang_code = read_gujjulang_code(gujjulang_file_path)


# Now use this function to translate and then execute your Gujjulang code
translated_code = gujjulang_to_python(gujjulang_code)
# print("Translated Python Code:\n", translated_code) #  This prints the code script and then the output 
print("Translated Python Code:\n") #This prints only  the output of the given code


# Execute the translated code
# Added a try and except calls so that it will show where the error has occured in the testing file
try:
    exec(translated_code)
except SyntaxError as e:
    print("There is a syntax error in the translated code:", e)