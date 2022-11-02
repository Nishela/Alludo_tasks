"""
A string of the form AAABBBEDDQQ is passed to the function input; the function must compress the string without losing
information and the expected output string is A3B3ED2Q2

Additionally write a decompression function
"""


def compressor(data: str) -> str:
    result = [data[0]]
    count = 1
    for x in range(1, len(data)):
        if data[x] == result[-1]:
            count += 1
            continue
        result.append(str(count) if count > 1 else '')
        result.append(data[x])
        count = 1
    else:
        result.append(str(count) if count > 1 else '')
    return ''.join(result)


def decompressor(data: str) -> str:
    result = []
    word = data[0]
    for x in range(1, len(data)):
        if data[x].isdigit():
            result.append(word * int(data[x]))
            word = ''
        elif data[x] != data[-1] and data[x + 1].isdigit():
            word = data[x]
        else:
            result.append(data[x])
    return ''.join(result)


if __name__ == '__main__':
    input_data = 'AAABBBEDDQQ'
    output_data = 'A3B3ED2Q2'
    assert compressor(input_data) == output_data
    assert decompressor(output_data) == input_data
