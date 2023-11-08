def get_formatted_name(first_name, last_name):
    " " "返回标准格式的姓名" " "
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name2(first_name, mid_name ='', last_name =''):
    " " "返回标准格式的姓名" " "
    if mid_name:
        full_name = f"{first_name} {mid_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician2 = get_formatted_name2('jimi', last_name='hendirx')
print(musician2)

musician2 = get_formatted_name2('john', 'hooker', 'lee')
print(musician2)