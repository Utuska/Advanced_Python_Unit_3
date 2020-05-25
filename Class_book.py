
class Contact:

    def __init__(self, name, surname, number, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        if args == ():
            self.main_number = ("Нет",)
        else:
            self.main_number = args
        self.additional_information = kwargs

    def __str__(self):
        number = "Нет"
        if self.main_number != None:
            number = self.main_number

        variable_telegram = "Нет"
        variable_email = "Нет"
        for i, j in self.additional_information.items():
            if i == "telegram":
                variable_telegram = j
            elif i == "email":
                variable_email = j

        return f'   Имя: {self.name}\n Фамилия: {self.surname}\n Телефон: {self.number}\n В избранных: {number[0]}\n Дополнительная информация:\n ' \
               f'telegram: {variable_telegram}\n email: {variable_email}'

class PhoneBook():

    def __init__(self, name):
        self.name = name
        self.contacts_list = []

    def conclusion_contacts(self):

        print("\n Список контактов \n  ")
        for contact in self.contacts_list:
            print(contact.name)

    def search_chosen_contact(self):

        for item in self.contacts_list:
            print(f'\n Избранные номера контакта {item.number}: \n')
            for number in item.main_number:
                print(number, '\n')


    def append_contacts(self, a):

        return self.contacts_list.append(a)

    def search_name_surname_contact(self,inquiry):

        for item in self.contacts_list:
            if item.name == inquiry or item.surname == inquiry:
                print(item)
                break
            else:
                print('Такого контакта нет в телефонной книге')

    def delete_contacts(self, number):

        for index in self.contacts_list:
            if index.number == number:
                self.contacts_list.remove(index)

Egor = Contact('Egor', 'Kravtsov', '+794394305350', '3544643634646', telegram='@logan', email='aner.@mail.ru')
print('\n Контакт 1 \n')
print(Egor)

jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
print('\n Контакт 2 \n')
print(jhon)

Users = PhoneBook("Телефонная книга")


Users.append_contacts(Egor)
#print(*Users.contacts_list)

Users.append_contacts(jhon)    #  добавление контакта

Users.conclusion_contacts() # вывод контактов

Users.search_chosen_contact() # поиск избранных номеров

Users.search_name_surname_contact('Egor') #     поиск контакта по имени и фамилии

Users.delete_contacts('+71234567809') # удаление контакта по номеру телефона
print("\n Контакт удален \n")



