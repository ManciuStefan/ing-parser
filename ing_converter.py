import sys
import csv

filename = sys.argv[1]
parsedFilename = sys.argv[2]

print(f'Parsing {filename} into {parsedFilename}')
exportFile = open(parsedFilename, mode='w')
export_writer = csv.writer(exportFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
export_writer.writerow(['Data', 'Tip tranzactie', 'Sursa/Destinatie', 'Suma'])

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if len(row[0]) > 0 and not row[0].startswith('Data'):
                if line_count > 1:
                    export_writer.writerow([date, type, sourceDest, sum])
                    print(f'\t{date} => {type} => {sourceDest} ||| {sum}.')
                date = row[0]
                type = row[3]
                sourceDest = '-'
                if len(row[5]) > 0:
                    sum = '-' + row[5]
                else:
                    sum = '+' + row[6]
            else:
                if row[3].startswith('Terminal') or row[3].startswith('Ordonator') or row[3].startswith('Beneficiar'):
                    aux, sourceDest = row[3].split(':')
            line_count += 1
