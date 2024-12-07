def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    
    return f"{formatted_f_name} {formatted_l_name}"
    
print(format_name("yaSiN", "tAsaSiz"))    


def function_1(text):
    return text + " " + "Tasasiz"

def function_2(text):
    return text.title()

output = function_2(function_1("yaSIn"))

print(output)

