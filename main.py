import pandas as pd

df = pd.read_excel('provinces-Sheet1.xlsx')

#Bài 1
print("Bài 1")
print("List of provinces and cities:", end=" ")
for province in df['Tên']:
    print(province, end=", ")

#Bài 2
print("Bài 2")
city_region_df = df[df["Cấp"] == "Thành phố Trung ương"][["Tên", "Vùng"]]
print(city_region_df)

#Bài 3
print("Bài 3")
num_geographical_areas = df['Vùng'].nunique()
print(f"Số vùng địa lý ở Việt Nam: {num_geographical_areas}")
province_count_per_area = df['Vùng'].value_counts()
print('Số tỉnh thành trong mỗi vùng địa lý:')
print(province_count_per_area)

#Bài 4
print('Bài 4')
max_population_province = df.loc[df["Dân số (nghìn người)"].idxmax()]
min_population_province = df.loc[df["Dân số (nghìn người)"].idxmin()]
print(f"Tỉnh thành có dân số đông nhất: {max_population_province}")
print(f"Tình thành có dân số ít nhất: {min_population_province}")

#Bài 5
print("Bài 5")
total_area = df["Diện tích (km2)"].sum()
area_ratio = df.groupby("Vùng")["Diện tích (km2)"].sum() / total_area
print("Tỉ lệ diện tích của vùng:")
print(area_ratio)