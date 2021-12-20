"""Day 20: Trench Map

https://adventofcode.com/2021/day/20

"""
MOVES = [
    (-1,-1), (0,-1), (1,-1),  # noqa
    (-1, 0), (0, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
]


def parse(data):
    enhancement_string, image = data.strip().split('\n\n')
    enhancement_string = enhancement_string.replace('\n', '')
    image = image.split('\n')
    return enhancement_string, image


def add_frame(image, sign='.'):
    empty_row = sign * (len(image[0]) + 4)
    new_image = [
        f'{sign}{sign}{row}{sign}{sign}'
        for row in image
    ]
    new_image = (
        [empty_row, empty_row] +
        new_image +
        [empty_row, empty_row]
    )
    x = len(empty_row)
    y = len(new_image)

    return new_image, x, y


def image_to_dict(image):
    return {
        (x, y): v
        for y, row in enumerate(image)
        for x, v in enumerate(row)
    }


def get_square(position, image_dict, sign):
    x, y = position
    for move in MOVES:
        dx, dy = move
        new_position = (x + dx, y + dy)
        yield image_dict.get(new_position, sign)


def find_enhancement(pos, image_dict, enhancement_string, sign='.'):
    square = list(get_square(pos, image_dict, sign))
    square = ''.join(square)
    square_binary = square.replace('.', '0').replace('#', '1')
    pos = int(square_binary, 2)
    return enhancement_string[pos]


def get_enhanced_image_dict(image_dict, enhancement_string, sign):
    new_image = {}
    for pos in image_dict:
        new_image[pos] = find_enhancement(
            pos,
            image_dict,
            enhancement_string,
            sign
        )
    return new_image


def dict_to_image(image_dict, len_x, len_y):
    image = []
    for y in range(len_y):
        row = ''.join(image_dict[(x, y)] for x in range(len_x))
        image.append(row)
    return image


def get_image_sum(image):
    return ''.join(image).count('#')


def get_sign(counter, enhancement_string):
    return '.' if counter % 2 == 1 else enhancement_string[0]


def solve(data, iterations=2):
    enhancement_string, image = parse(data)
    counter = 1
    while iterations:
        sign = get_sign(counter, enhancement_string)
        image, x, y = add_frame(image, sign=sign)
        image_dict = image_to_dict(image)
        new_image_dict = get_enhanced_image_dict(
            image_dict,
            enhancement_string,
            sign=sign
        )
        image = dict_to_image(new_image_dict, x, y)
        iterations -= 1
        counter += 1
    print(image_repr(image))
    return get_image_sum(image)


def image_repr(image):
    return '\n'.join([row for row in image])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, 50)
    print(f'Example2: {result}')
