phone_book = []


def get_phone_book():
	global phone_book
	return phone_book


def set_phone_book(new_phone_book):
	global phone_book
	phone_book = new_phone_book


def add_contact(contact: list):
	global phone_book
	phone_book.append(contact)


def remove_contact(id):
	global phone_book
	name = phone_book[id-1][0]
	confim = input(f'Вы действительно ходите удалить контакт {name}?(y/n)')
	if confim.lower() =='y':
		phone_book.pop(id-1)
		return True
	return False


def change_contact(id, contact):
	global phone_book
	for g in range(len(contact)):
		if contact[g] !='':
			phone_book[id][g] = contact[g]


def search_contact(serch):
	global phone_book
	my_list = []
	for i in phone_book:
		for g in i:
			if serch in g:
				my_list.append(i)
	return (my_list)




