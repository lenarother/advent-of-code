"""{{cookiecutter._title}}

{{cookiecutter._url}}

"""


def solve(data):
    return data


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
