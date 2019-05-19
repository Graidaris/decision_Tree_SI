
def isnumeric(s):
    return all(c in "0123456789.+-" for c in s) and any(c in "0123456789" for c in s)


def convert(line):
    return ','.join(str(float(x)) if isnumeric(x)
                    else "-" for x in line.strip().split(','))


with open("new_dataset.data", "w") as new_dataset:

    with open("processed.hungarian.data", "r") as dataset:
        for line in dataset:
            l = convert(line)
            if '-' not in l:
                new_dataset.write(l + '\n')

    with open("processed.switzerland.data", "r") as dataset:
        for line in dataset:
            l = convert(line)
            if '-' not in l:
                new_dataset.write(l + '\n')

    with open("processed.va.data", "r") as dataset:
        for line in dataset:
            l = convert(line)
            if '-' not in l:
                new_dataset.write(l + '\n')

    with open("processed.cleveland.data", "r") as dataset:
        for line in dataset:
            l = convert(line)
            if '-' not in l:
                new_dataset.write(l + '\n')
