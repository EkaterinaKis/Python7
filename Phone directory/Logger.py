
def add_new(contact):
    with open('Directory.txt', 'a', encoding='utf-8')as directory:
        directory.write(f'{contact}\n')


def get_contact():
    with open('Directory.txt', 'r', encoding='utf-8') as directory:
        return directory.read()
