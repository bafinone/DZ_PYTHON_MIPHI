import csv
with open("products.csv","r",encoding="utf-8") as input_file:
    reader=csv.reader(input_file)
    with open("expensive.csv","w",encoding="utf-8",newline="") as output_file:
        writer=csv.writer(output_file)
        header=next(reader)
        writer.writerow(header)
        for row in reader:
            price=float(row[2])
            if price>100:
                writer.writerow(row)
