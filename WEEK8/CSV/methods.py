import csv

def read_csv(file_1, file_2):
    with open(file_1, 'r') as file:
        reader = csv.reader(file)
        with open(file_2, "w", newline='') as file_w:
            writer = csv.writer(file_w)
            for row in reader:
                row = ",".join(row).replace(",","/")
                writer.writerow([row])


read_csv("read_csv_file.csv", "write_csv_file.csv")

