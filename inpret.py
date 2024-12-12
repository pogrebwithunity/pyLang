import sys

selected_string = ''

# Проверяем, передан ли аргумент
if len(sys.argv) > 1:
    # Получаем строку, переданную в качестве аргумента
    selected_string = sys.argv[1]
else:
    exit('Do not choosed the file')

class PyLangInterpreter:
    def __init__(self):
        self.variables = {}

    def eval(self, line):
        line = line.strip()
        
        # Игнорируем пустые строки и комментарии
        if not line or line.startswith('#'):
            return
        
        # Обработка присваивания
        if '=' in line:
            var_name, expression = line.split('=', 1)
            var_name = var_name.strip()
            expression = expression.strip()
            self.variables[var_name] = self.eval_expression(expression)
        elif line.startswith('print'):
            var_name = line[5:].strip()
            if var_name in self.variables:
                print(self.variables[var_name])
            else:
                print(f"Ошибка: переменная '{var_name}' не определена.")
        elif line.startswith('help'):
            print('commands: x = num print x, x = num print x + x dont working, x = num y = num z = x + y print z working')
        else:
            raise SyntaxError(f"Неизвестная команда: {line}")

    def eval_expression(self, expression):
        # Удаляем пробелы
        expression = expression.replace(' ', '')
        
        # Простой парсер для арифметических выражений
        try:
            return eval(expression, {}, self.variables)
        except Exception as e:
            raise ValueError(f"Ошибка при вычислении выражения '{expression}': {e}")

    def run(self, code):
        for line in code.splitlines():
            self.eval(line)

# Пример использования
if __name__ == "__main__":
    f = open(selected_string, 'r+')
    code = f.read()
    
    interpreter = PyLangInterpreter()
    interpreter.run(code)