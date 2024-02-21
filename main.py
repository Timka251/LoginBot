import datetime
import pytz


def register():
    name = input("Введите ваше имя (без пробелов): ")
    while ' ' in name:
        name = input("Имя не должно содержать пробелов. Пожалуйста, введите ваше имя еще раз: ")
    login = input("Введите логин (без пробелов): ")
    while ' ' in login:
        login = input("Логин не должен содержать пробелов. Пожалуйста, введите логин еще раз: ")
    password = input("Введите пароль (без пробелов): ")
    while ' ' in password:
        password = input("Пароль не должен содержать пробелов. Пожалуйста, введите пароль еще раз: ")
    
    with open("users.txt", "r") as file:
        existing_logins = [line.strip().split()[1] for line in file]
        if login in existing_logins:
            print("Пользователь с таким логином уже существует.")
            return
    
    with open("users.txt", "a") as file:
        file.write(f"{name} {login} {password}\n")
    print("Регистрация успешна!")

def login():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    with open("users.txt", "r") as file:
        for line in file:
            user_data = line.strip().split()
            saved_login, saved_password = user_data[-2], user_data[-1]
            if login == saved_login and password == saved_password:
                print("Привет!")
                current_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
                print("Текущая дата и время в Москве:", current_time.strftime('%Y-%m-%d %H:%M:%S'))
                return True
    
    print("Ошибка")
    return False

def main():
    while True:
        choice = input("Выберите действие:\n1. Регистрация\n2. Вход\nВыбор: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                break
            else:
                retry = input("Попробовать снова? (Да/Нет): ")
                if retry.lower() != "да":
                    break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()
