def get_formatted(first_name, last_name):
    full_name = (first_name + " " +  last_name + ".")
    return  full_name.title()
    
musian = get_formatted("john", "timothy")
print(musian)