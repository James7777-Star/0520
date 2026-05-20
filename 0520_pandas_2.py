import pandas as pd

# 原始資料
products = ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"]
prices = [30, 20, 25, 60, 45, 35]
sales = [100, 150, 80, 60, 90, 54]

# ----------------------------------------------------
# 1. 使用「字典 (Dictionary)」方式建立 DataFrame
# ----------------------------------------------------
data_dict = {"Product": products, "Price": prices, "Sales": sales}
df_from_dict = pd.DataFrame(data_dict)

# ----------------------------------------------------
# 2. 使用「列表 (子列表 List of Lists)」方式建立 DataFrame
# ----------------------------------------------------
data_list = []
for i in range(len(products)):
    data_list.append([products[i], prices[i], sales[i]])

df_from_list = pd.DataFrame(data_list, columns=["Product", "Price", "Sales"])


# ----------------------------------------------------
# 3. 依照輸出範例列印結果
# ----------------------------------------------------

# (1) 觀察資料的前 5 筆與後 5 筆內容
# 註：因為總共只有 6 筆，前 5 筆會是 0~4，後 5 筆會是 1~5
print(df_from_dict.head(5))
print(df_from_dict.tail(5))

# (2) 回傳資料的列數與欄數 (shape)
print(df_from_dict.shape)

# (3) 欄位名稱 (columns)
print(df_from_dict.columns)

# (4) 資料型態 (dtypes)
print(df_from_dict.dtypes)

# (5) 非空值數量 (count)
print(df_from_dict.count())

# (6) 計算數值欄位的統計資訊並取小數後 2 位
# 使用 describe() 取得統計，並用 round(2) 限制小數位數
summary_stats = df_from_dict.describe().round(2)
print(summary_stats)

# ----------------------------------------------------
# 4. 將統計資訊儲存為 0520_stock2.csv
# ----------------------------------------------------
summary_stats.to_csv("0520_stock2.csv")