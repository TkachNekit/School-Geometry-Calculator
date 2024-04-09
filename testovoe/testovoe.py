from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ProductCategoryAnalysis") \
    .getOrCreate()

# Предположим, что у вас есть два датафрейма: products и categories
# По ключу все объединяем
left_joined = products.join(categories, products.product_id == categories.product_id, "left_outer")
# Если нет категории, то берем
no_category_df = left_joined.filter(left_joined.category_id.isNull())
# Выбираем нужные столбцы для вывода
result_df = no_category_df.select("product_name")
result_df.show()
