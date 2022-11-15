import csv

with open('LOG_2022_2_0_2022_02_06.CSV') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Columns names are {", ".join( row)}')
            line_count += 1
        print(f'\t {row[0]} the temperature is {row[11]} degrees at {row[2]}.')

    print(f'Processed {line_count} lines.')

