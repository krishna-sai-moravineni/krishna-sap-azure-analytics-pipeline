import pandas as pd
import faker
import random

fake = faker.Faker()

sample_customers = [{"customer_id": f"CUST{i:04d}", "customer_name": fake.company(), "city": fake.city(), "country": fake.country()} for i in range(1000)]
df_customers =pd.DataFrame(sample_customers)
#print(df_customers)


sample_vendors = [{"vendor_id": f"VEND{i:04d}", "vendor_name": fake.company(), "city":fake.city(), "country": fake.country()} for i in range(1000)]
df_vendors = pd.DataFrame(sample_vendors)
#print(df_vendors)

random_cust_ids = df_customers["customer_id"].to_list()
random_order_status = ["Open", "In Progress", "Completed", "Cancel In Progress", "Cancelled"]
#print(random_cust_ids)

sales_order_header = [{"order_id": f"SO{i:05d}", "customer_id": random.choice(random_cust_ids), "order_date": fake.date_this_year(), "order_status": random.choice(random_order_status)} for i in range(1000)]
df_sales_header = pd.DataFrame(sales_order_header)
print(df_sales_header)