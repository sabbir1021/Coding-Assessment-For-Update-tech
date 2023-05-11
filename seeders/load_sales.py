
from sales.models import Sales
import csv
print('----------- Ready for data seed')

def run():
    with open('seeders/xyz_sales_data.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            Sales.objects.create(
                order_id = row[1],
                order_date = row[2],
                ship_date = row[3],
                ship_mode = row[4],
                customer_id = row[5],
                customer_name = row[6],
                segment = row[7],
                country = row[8],
                city = row[9],
                state = row[10],
                postal_code = row[11],
                region = row[12],
                product_id = row[13],
                category = row[14],
                sub_category = row[15],
                product_name = row[16],
                sales = row[17]
                )
    print('----------- end ------')
    return