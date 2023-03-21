def count_max_synbol(symbols_count):
    max_symbol_count = 0

    for symb in symbols_count:
        if symbols_count[symb] > max_symbol_count:
            max_symbol_count = symbols_count[symb]

    return max_symbol_count


def output_histogram(symbols_count):
    max_symbol_count = count_max_synbol(symbols_count)

    sorted_symbols = sorted(symbols_count.keys())

    for current_symbol_count in range(max_symbol_count, 0, -1):
        current_row = [0] * len(sorted_symbols)

        for i in range(len(sorted_symbols)):
            if symbols_count[sorted_symbols[i]] >= current_symbol_count:
                current_row[i] = "#"
            else:
                current_row[i] = " "

        print("".join(current_row))
    print("".join(sorted_symbols))


def count_symbols(lines):
    symbols_count = {}

    for line in lines:
        for word in line.split():
            for symb in word:
                if symb not in symbols_count:
                    symbols_count[symb] = 0
                symbols_count[symb] += 1

    return symbols_count


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    symbols_count = count_symbols(lines)
    output_histogram(symbols_count)
