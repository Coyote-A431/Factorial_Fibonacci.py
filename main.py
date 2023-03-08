print('First two numbers in Fibonacci (1, 1) are not allowed')

def validation():
    is_valid_input = False
    while not is_valid_input:
        try:
            num = input('Enter Fibonacci number/factorial number: ')
            num = int(num)
            if num > 0:
                is_valid_input = True
            else:
                print('Your number must be greater 0')
        except ValueError:
            print('You entered not number or left empty field')
    return num


def get_fact_num(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial


def get_fib_num(number_for_fib):
    fib1 = 1
    fib2 = 1
    fib_sum = 0
    i = 0
    while i < number_for_fib - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        print(f'{i} iteration: ', fib_sum)
    return fib_sum


# number = validation()
# fact = get_fact_num(number)
# number_for_fib = number + 2
# fib = get_fib_num(number_for_fib)
# print(fact)


#####


class Factorial_Fibonacci:

    def __init__(self):
        numbers_list = self.validation()
        self.num_for_fact = numbers_list[0]
        self.num_for_fib = numbers_list[1]

    def validation(self):
        is_valid_input = False
        while not is_valid_input:
            try:
                user_num = input('Enter Fibonacci number/factorial number: ')
                user_num = int(user_num)
                if user_num > 0:
                    result = [user_num, user_num + 2]
                    is_valid_input = True
                else:
                    print('Your number must be greater 0')
            except ValueError:
                print('You entered not number or left empty field')
        return result

    def get_fact_num(self):
        factorial = 1
        i = self.num_for_fact
        while i > 1:
            factorial *= i
            i -= 1
        print(f'{self.num_for_fact} iterations completed. Factorial {self.num_for_fact}! = ', factorial)
        return factorial

    def get_fib_num(self):
        fib1 = 1
        fib2 = 1
        fib_sum = 0
        i = 0
        while i < self.num_for_fib - 2:
            fib_sum = fib1 + fib2
            fib1 = fib2
            fib2 = fib_sum
            i += 1
            print(f'{i} iteration: ', fib_sum)
        return fib_sum

test = Factorial_Fibonacci()
test.get_fib_num()
test.get_fact_num()

