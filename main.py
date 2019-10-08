import os


def reader(student: dict):
    file = os.path.abspath(os.path.join("student.txt"))
    rdr = open(file, 'r')
    if not rdr:
        raise FileNotFoundError
    for line in rdr:
        x = line.split(":")
        key = x[0]
        value = x[1].strip().split(',')
        student[key] = value


def print_map(student: dict):
    for key, value in student.items():
        print(key, value)


def serach_key(key: str, student: dict):
    if key not in student.keys():
        return False
    return True


def append_value_in_key(student: dict, key: str, item: str):
    if key not in student.keys():
        raise IndexError
    student[key].append(item)


def pop_value_in_key(student: dict, key: str):
    student[key].pop()


def insert_at(student: dict, key: str, iteam: str, index: int):
    if key not in student.keys():
        raise IndexError
    student[key].insert(index, iteam)


def add_a_new_key(student: dict, new):
    data = new.split(':')
    key = data[0]
    items = data[1].split(',')
    student[key] = items


def main():
    student = {}
    reader(student)
    print_map(student)
    """""
    key = input("Enter  a key to find")
    if serach_key(key, student):
        print("the", key, "is Found...!!!")
    else:
        print(key, "is not Found ...!!!")
    key = input('Enter a key')
    item = input('Enter a item to append')
    append_value_in_key(student, key, item)
    print_map(student)
    pop_value_in_key(student, key)
    """""
    new = input("enter a new key , and items")
    add_a_new_key(student, new)
    print_map(student)


if __name__ == "__main__":
    main()
