"""
Develop branch
"""


def input_data() -> str:
    return input('Введите строку')


def print_data(data: str) -> None:
    print(data)


def exit_program() -> None:
    input('Нажмите Enter для выхода')


def main() -> None:
    data = input_data()
    print_data(data)
    exit_program()


if __name__ == '__main__':
    main()
   