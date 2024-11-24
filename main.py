class Calculator:
    a: str
    b: str
    def StrToFloat(self, number_str: str):
        try:
            print(f'--->>> конвертація типу данних str в float, значення {number_str}')
            try:
                return float(number_str)
            except:
                raise TypeError(f'помилка конвертації')

        except TypeError as error:
            print(f'{error}')
            return 0
        except:
            print(">>>>>error")
            return 0
        finally:
            print(">>>>>конвертація завершено!")
    def division(self, a: float, b: float):
        try:
            print(f'--->>> початок ділення a / b')
            result = a / b
            print(f'{a} / {b} = {result}')
        except ZeroDivisionError as error:
            print(f'error info {error}')
        finally:
            print('>>>>>ділення завершено!')
    def multiplication(self, a: float, b: float):
        print(f'--->>> початок множення a * b')
        result = a * b
        print(f'{a} * {b} = {result}')
        print('>>>>>множення завершено!')
    def addition(self, a: float, b: float):
        print(f'--->>> початок додавання a + b')
        result = a + b
        print(f'{a} + {b} = {result}')
        print('>>>>>додавання завершено!')
    def subtraction(self, a: float, b: float):
        print(f'--->>> початок віднімання a - b')
        result = a - b
        print(f'{a} - {b} = {result}')
        print('>>>>>віднімання завершено!')


Calculator = Calculator()
a = input("введіть значення зміної a = ")
a = Calculator.StrToFloat(a)
b = input("введіть значення зміної b = ")
b = Calculator.StrToFloat(b)

while True:
    operation = input("введіть потрибну операцию (/,*,+,-): ")
    if operation == "/":
        Calculator.division(a, b)
    elif operation == "*":
        Calculator.multiplication(a, b)
    elif operation == "+":
        Calculator.addition(a, b)
    elif operation == "-":
        Calculator.subtraction(a, b)
    else:
        break