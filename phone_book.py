def input_id():
    return input('Введите id контакта: ')

def input_surname():
    return input('Введите фамилию контакта: ').title()

def input_name():
    return input('Введите имя контакта: ').title()

def input_patronymic():
    return input('Введите отчество контакта: ').title()

def input_phone():
    return input('Введите телефон контакта: ')

def input_address():
    return input('Введите адрес(город) контакта: ').title()

def create_contact():
    id_contact = input_id()
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{id_contact} - {surname} {name} {patronymic}: {phone}\n{address}\n\n'

def add_contact():
    contact_str = create_contact()
    with open("phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(contact_str)
           
def print_contacts():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')
    for contact in contacts_list:
        print(contact)
 
def copy():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        print(contacts_str)

        search = input('Введите id контакта для копирование: ').title()
        with open("phonebook.txt", 'r', encoding='utf-8') as file:
            contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')

        for str_contact in contacts_list:
            lst_contact = str_contact.replace(':', '').split()
            if search in lst_contact[0]:
                copy_cont = f"{str_contact} \n"   
                with open("New_phone.txt", 'a', encoding='utf-8') as file:
                    file.write(copy_cont)
                
def search_contact():
    print(
            'Возможные варианты поиска:\n'
            '1. По id\n'
            '2. По фамилии\n'
            '3. По имени\n'
            '4. По отчество\n'
            '5. По телефону\n'
            '6. По адресу(город)'
            )
    var = input('выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5', '6'):
        print('некорректный ввод!')
        var = input('выберите вариант поиска: ')
    i_var = int(var) - 1    

    search = input('Введите данные для поиска: ').title()
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:
            print(str_contact)

def interface():
    with open("phonebook.txt", 'a', encoding='utf-8'):
        pass

    var = 0
    while var != '5':
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Копирование контакта\n'
            '4. Поиск контакта\n'
            '5. Выход'
            )
        print()
        var = input('выберите вариант действия: ')
        while var not in ('1', '2', '3', '4', '5'):
            print('некорректный ввод!')
            var = input('выберите вариант действия: ')
        print()    

        match var: 
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                copy()
            case '4': 
                search_contact()
            case '5':
                print('До свидания') 
        print()        

if __name__ == '__main__':
    interface()

