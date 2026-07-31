import csv
import random


def generate_data(num_rows = 500, filename = 'Uptime of Laptops from Various Brands.csv'):
    headers = [
        'Laptops Serial Number', 
        'Belongs to a Computer Producers Brand',
        'Uninterrupted Operating Time (hours)'
    ]

    with open(filename, mode = 'w', newline = '', encoding = 'utf-8-sig') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(headers)
        for i in range(1, num_rows + 1):
            row = [
                i,
                random.randint(1000000, 2000000),
                random.randint(0, 1),
                random.randint(85, 285)           
            ]
            writer.writerow(row)
            
    print(f"Success ! {num_rows} records generated.")
    print(f"The file was successfully saved with the name: {filename}")

if __name__ == '__main__':
    generate_data(500)