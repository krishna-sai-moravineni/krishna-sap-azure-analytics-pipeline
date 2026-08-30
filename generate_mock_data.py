import pandas as pd
import faker
import random

fake = faker.Faker()

sample_customers = [{
                     "customer_id": f"CUST{i:04d}", 
                     "customer_name": fake.company(), 
                     "city": fake.city(), 
                     "country": fake.country()
                    } for i in range(1000)]

df_customers = pd.DataFrame(sample_customers)
#print(df_customers)


sample_vendors = [{
                    "vendor_id": f"VEND{i:04d}", 
                    "vendor_name": fake.company(), 
                    "city":fake.city(), 
                    "country": fake.country()
                  } for i in range(1000)]

df_vendors = pd.DataFrame(sample_vendors)
#print(df_vendors)


material_group = ["Raw Material", "Finished Good", "Packaging", "Spare Part"]
sample_materials = [{
                     "material_id": f"MAT{i:04d}", 
                     "material_name": fake.word().capitalize() + " " + fake.word().capitalize(), 
                     "material_group": random.choice(material_group),
                     "unit_price": round(random.uniform(1, 500), 2)
                    } for i in range(200)]

df_materials = pd.DataFrame(sample_materials)
#print(df_materials.head(10))

cust_ids = df_customers["customer_id"].to_list()
material_ids = df_materials["material_id"].to_list()
order_statuses = ["Open", "In Progress", "Completed", "Cancel In Progress", "Cancelled"]


sales_order_header = []
sales_order_item = []

for i in range(1000):

    #generate header row
    order_id = f"SO{i:05d}"

    header_row = {
                    "order_id": order_id, 
                    "customer_id": random.choice(cust_ids), 
                    "order_date": fake.date_this_year(), 
                    "order_status": random.choice(order_statuses)
                 }
    sales_order_header.append(header_row)

    #generate line items for the above header row
    for j in range(random.randint(1, 5)):

        curr_material_id = random.choice(material_ids)
        curr_quantity = random.randint(1, 1000)
        curr_material_unit_price = df_materials.loc[df_materials["material_id"] == curr_material_id, "unit_price"].values[0]

        item_row = {
                    "order_id": order_id,
                    "material_id": curr_material_id,
                    "item_number": (j + 1) * 10,
                    "quantity": curr_quantity,
                    "amount": round(curr_quantity * curr_material_unit_price, 2)
                   }

        sales_order_item.append(item_row)
        

df_sales_header = pd.DataFrame(sales_order_header)
df_sales_line_items = pd.DataFrame(sales_order_item)

print(df_sales_header.head(10))
print(df_sales_line_items.head(100))