import csv


def read_csv_file(file_1, file_2):
  with open(file_1, 'r') as file:
    reader = csv.DictReader(file)
    with open(file_2,"w") as file_w:
        writer = csv.DictWriter(file_w, fieldnames = reader.fieldnames)
        writer.writeheader()
        for row in reader:
           writer.writerow(row)


read_csv_file("write_csv.csv", "write_csv_file.cvs")