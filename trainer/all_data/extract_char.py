import csv

input_csv = 'test/labels.csv'
chars = []

with open(input_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 1:
            for c in row[1]:
                if str(c) not in chars:
                    chars.append(str(c))

input_csv = 'train/labels.csv'
# chars = []

with open(input_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 1:
            for c in row[1]:
                if str(c) not in chars:
                    chars.append(str(c))

input_csv = 'val/labels.csv'
# chars = []

with open(input_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 1:
            for c in row[1]:
                if str(c) not in chars:
                    chars.append(str(c))

print(' '.join(chars))