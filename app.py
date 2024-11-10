from flask import Flask, jsonify
from functools import reduce

app = Flask(__name__)


@app.route('/A1G', methods=['GET'])
def A1G():
    def pure_function(x, y):
        return x + y

    total = 0

    def unpure_function(x, y):
        nonlocal total
        total += x + y
        return total

    result_pure = pure_function(3, 4)
    result_unpure = unpure_function(3, 4)

    return jsonify(
        pure_function_result=result_pure,
        unpure_function_result=result_unpure
    )


@app.route('/A1F', methods=['GET'])
def A1F():
    def immutable_example(x):
        x = x + 1
        return x

    original_value = 10
    new_value = immutable_example(original_value)

    mutable_list = [1, 2, 3]

    def mutable_example(lst):
        lst.append(4)
        return lst

    new_list = mutable_example(mutable_list)

    return jsonify(
        immutable_example={"original_value": original_value, "new_value": new_value},
        mutable_example={"original_list": [1, 2, 3], "new_list": new_list}
    )


@app.route('/A1E', methods=['GET'])
def A1E():
    def procedural_solution(x, y):
        return x + y

    class OOSolution:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def calculate(self):
            return self.x + self.y

    def functional_solution(x, y):
        return (lambda a, b: a + b)(x, y)

    result_procedural = procedural_solution(3, 4)
    oo_instance = OOSolution(3, 4)
    result_oo = oo_instance.calculate()
    result_functional = functional_solution(3, 4)

    return jsonify(
        procedural_result=result_procedural,
        oo_result=result_oo,
        functional_result=result_functional
    )

@app.route('/B1G', methods=['GET'])
def B1G():
    def sort(nums):
        for i in range(len(nums)):
            for y in range(len(nums) - 1):
                if nums[y] > nums[i]:
                    before = nums[y]
                    nums[y] = nums[i]
                    nums[i] = before


    numbers = [64, 34, 25, 12, 22, 11, 90]
    sort(numbers)
    return jsonify(
        input=[64, 34, 25, 12, 22, 11, 90],
        output=numbers
    )

@app.route('/B1F', methods=['GET'])
def B1F():
    def bubble_sort(numbers, n=None):
        if n is None:
            n = len(numbers)
        if n <= 1:
            return numbers
        else:
            numbers = bubble_pass(numbers)
            return bubble_sort(numbers, n - 1)

    def bubble_pass(lst):
        if len(lst) <= 1:
            return lst
        if lst[0] > lst[1]:
            return [lst[1]] + bubble_pass([lst[0]] + lst[2:])
        return [lst[0]] + bubble_pass(lst[1:])

    unsorted_list = [5, 2, 9, 1, 5, 6]
    sorted_list = bubble_sort(unsorted_list)

    return jsonify(
        input=unsorted_list,
        output=sorted_list
    )


@app.route('/B1E', methods=['GET'])
def B1E():
    def calculate_total_cost(items):
        prices = map(get_price, items)
        discounted_prices = map(apply_discount, prices)
        total_cost = sum(discounted_prices)
        return total_cost

    def get_price(item):
        return item['price']

    def apply_discount(price):
        return price * 0.9

    items = [
        {"name": "item1", "price": 100},
        {"name": "item2", "price": 200},
        {"name": "item3", "price": 300}
    ]

    result = calculate_total_cost(items)

    return jsonify(
        items=items,
        total_cost=result
    )

@app.route('/B2G', methods=['GET'])
def B2G():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def execute_operation(operation, x, y):
        return operation(x, y)

    operations = {
        "addition": add,
        "subtraction": subtract
    }

    result_add = execute_operation(operations["addition"], 5, 3)
    result_subtract = execute_operation(operations["subtraction"], 5, 3)

    return jsonify(
        result_addition=result_add,
        result_subtraction=result_subtract
    )

@app.route('/B2F', methods=['GET'])
def B2F():
    def multiply_by_two(x):
        return x * 2

    def add_three(x):
        return x + 3

    def apply_function(func, value):
        return func(value)

    result_multiply = apply_function(multiply_by_two, 5)
    result_add = apply_function(add_three, 5)

    return jsonify(
        result_multiply_by_two=result_multiply,
        result_add_three=result_add
    )

@app.route('/B2E', methods=['GET'])
def B2E():
    def multiplier(factor):
        def multiply_by_factor(number):
            return number * factor
        return multiply_by_factor

    double = multiplier(2)
    triple = multiplier(3)

    result_double = double(5)
    result_triple = triple(5)

    return jsonify(
        result_double=result_double,
        result_triple=result_triple
    )
@app.route('/B3G', methods=['GET'])
def B3G():
    square = lambda x: x ** 2
    to_uppercase = lambda s: s.upper()

    result_square = square(5)
    result_uppercase = to_uppercase("hello")

    return jsonify(
        result_square=result_square,
        result_uppercase=result_uppercase
    )
@app.route('/B3F', methods=['GET'])
def B3F():
    add = lambda x, y: x + y
    multiply = lambda a, b: a * b

    result_add = add(2, 3)
    result_multiply = multiply(4, 5)

    return jsonify(
        result_add=result_add,
        result_multiply=result_multiply
    )

@app.route('/B3E', methods=['GET'])
def B3E():
    numbers = [5, 3, 8, 1, 4]
    sorted_numbers = sorted(numbers, key=lambda x: -x)

    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    sorted_people = sorted(people, key=lambda person: person["age"])

    return jsonify(
        sorted_numbers=sorted_numbers,
        sorted_people=sorted_people
    )
@app.route('/B4G', methods=['GET'])
def B4G():
    numbers = [1, 2, 3, 4, 5, 6]

    mapped = list(map(lambda x: x * 2, numbers))
    filtered = list(filter(lambda x: x % 2 == 0, numbers))
    reduced = reduce(lambda x, y: x + y, numbers)

    return jsonify(
        mapped=mapped,
        filtered=filtered,
        reduced=reduced
    )

@app.route('/B4F', methods=['GET'])
def B4F():
    numbers = [1, 2, 3, 4, 5, 6]

    result = reduce(lambda x, y: x + y, filter(lambda x: x > 5, map(lambda x: x * 2, numbers)))

    return jsonify(
        final_result=result
    )

@app.route('/B4E', methods=['GET'])
def B4E():
    data = [
        {"name": "Alice", "age": 30, "score": 88},
        {"name": "Bob", "age": 25, "score": 95},
        {"name": "Charlie", "age": 35, "score": 70},
        {"name": "Diana", "age": 40, "score": 85}
    ]

    scores_above_80 = filter(lambda x: x['score'] > 80, data)
    names_uppercase = map(lambda x: {"name": x["name"].upper(), "age": x["age"], "score": x["score"]}, scores_above_80)
    total_score = reduce(lambda acc, x: acc + x['score'], names_uppercase, 0)

    return jsonify(
        total_score=total_score
    )
@app.route('/C1G', methods=['GET'])
def C1G():
    def add_numbers(a, b, c):
        return a + b + c

    def add_numbers_refactored(*args):
        return sum(args)

    result_before = add_numbers(1, 2, 3)
    result_after = add_numbers_refactored(1, 2, 3, 4)

    return jsonify(
        result_before=result_before,
        result_after=result_after
    )

@app.route('/C1F', methods=['GET'])
def C1F():
    def calculate_area(radius):
        return 3.14159 * radius * radius

    PI = 3.14159
    def calculate_area_refactored(radius):
        return PI * radius * radius

    radius = 5
    result_before = calculate_area(radius)
    result_after = calculate_area_refactored(radius)

    return jsonify(
        result_before=result_before,
        result_after=result_after
    )

@app.route('/C1E', methods=['GET'])
def C1E():
    def calculate_total(price):
        discount = price * 0.1
        return price - discount

    def calculate_discount(price):
        return price * 0.1

    def calculate_total_refactored(price):
        return price - calculate_discount(price)

    price = 50
    result_before = calculate_total(price)
    result_after = calculate_total_refactored(price)

    return jsonify(
        result_before=result_before,
        result_after=result_after
    )


if __name__ == '__main__':
    app.run(debug=True)
