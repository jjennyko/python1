import pandas as pd
datataipei = pd.read_csv("A_lvr_land_A.csv")
datataichung = pd.read_csv("B_lvr_land_A.csv")
datakaohsiung = pd.read_csv('E_lvr_land_A.csv')
datanewtaipei = pd.read_csv('F_lvr_land_A.csv')
print(datataipei.head())
datataipei = datataipei.drop(0)
datataichung = datataichung.drop(0)
datakaohsiung = datakaohsiung.drop(0)
datanewtaipei = datanewtaipei.drop(0)

datataipei['地區'] = '台北'
datataichung['地區'] = '台中'
datakaohsiung['地區'] = '高雄'
datanewtaipei['地區'] = '新北'

data = pd.concat([datataipei, datataichung, datakaohsiung, datanewtaipei], axis=0, join='inner').reset_index(drop=True)
print(data.head())
print(data.info())


columns_mapping = {'鄉鎮市區':'towns',
'交易標的':'transaction_sign',
'土地區段位置建物區段門牌':'house_number',
'土地移轉總面積平方公尺':'land_area_square_meter', 
'都市土地使用分區':'use_zoning', 
'非都市土地使用分區':'land_use_district',
'非都市土地使用編定':'land_use',
'交易年月日':'tx_dt', 
 '交易筆棟數':'transaction_pen_number', 
 '移轉層次':'shifting_level', 
 '總樓層數':'total_floor_number', 
 '建物型態':'building_state', 
 '主要用途':'main_use', 
 '主要建材':'main_materials',
 '建築完成年月':'complete_date', 
 '建物移轉總面積平方公尺':'building_area_square_meter', 
 '建物現況格局-房':'room_number', 
 '建物現況格局-廳':'hall_number', 
 '建物現況格局-衛':'health_number', 
'建物現況格局-隔間':'compartmented_number', 
 '有無管理組織':'manages', 
 '總價元':'total_price', 
 '單價元平方公尺':'unit_price', 
 '車位類別':'berth_category', 
 '車位移轉總面積(平方公尺)':'berth_area_square_meter',
'車位總價元':'berth_price', 
 '備註':'note', 
 '編號':'serial_number', 
 '主建物面積':'main_building_area', 
 '附屬建物面積':'auxiliary_building_area', 
 '陽台面積':'balcony_area', 
 '電梯':'elevator',
 '地區':'city'
                  }
analysis_columns = ['city','towns','main_use','use_zoning','total_price','building_area_square_meter',
                                     'main_building_area',
                                     'tx_dt','unit_price','room_number','hall_number','health_number']
columns_type = {'total_price': 'int','unit_price':'float','building_area_square_meter':'float',
                                      'main_building_area': 'float',
                                      'room_number': 'int','hall_number': 'int','health_number': 'int'}
new_data = data.rename(columns=columns_mapping)
new_data = new_data.loc[(new_data['main_use']=='住家用')&(new_data['use_zoning']=='住'),analysis_columns].dropna()
print(new_data.info())
new_data = new_data.astype(columns_type)
print(new_data.info())
print(new_data.head())

new_data['tx_dt_year'] = new_data['tx_dt'].apply(lambda x : int(x[:3]))
new_data = new_data.loc[(new_data['tx_dt_year']==109)&
                        (new_data['room_number']>=1)&
                        (new_data['room_number']<=5)&
                        (new_data['hall_number']>=1)&
                        (new_data['hall_number']<=2)].reset_index(drop=True)
print(new_data)


new_data['buildin_area_square_feet'] = new_data['building_area_square_meter']*0.3025
new_data['main_buildin_area_square_feet'] = new_data['main_building_area']*0.3025
new_data['unit_price_square_feet'] = new_data['unit_price']/0.3025
print(new_data.describe()) # 發現最小值有0[tatal_price,building_area_square_meter]
new_data = new_data.loc[(new_data['total_price']!=0)&(new_data['main_building_area']!=0)]
print(new_data.describe())


new_data1 = new_data.loc[new_data['city']=='台北'].corr()[['total_price', 'unit_price_square_feet']]
print(new_data1)

import matplotlib.pyplot as plt
new_data.boxplot(column=['unit_price_square_feet'], by='city', figsize=(16,6))
plt.xticks([1,2,3,4],['Taipei','Taichung','Kaohsiung','newTaipei'])
plt.show()

new_data.loc[new_data['city']=='台北'].boxplot(column=['total_price'], by='room_number', figsize=(16,6))
plt.show()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder().fit(new_data['towns'].values)
new_data['new_towns'] = le.transform(new_data['towns'].values)
print(new_data['new_towns'].head())
new_data.loc[new_data['city']=='台北'].boxplot(column=['unit_price_square_feet'], by='new_towns', figsize=(16,6))
plt.show()


print(le.inverse_transform([26]))


new_data2 = new_data.loc[new_data['city']=='台中'].corr()[['total_price','unit_price_square_feet']]
print(new_data2)
new_data.loc[new_data['city']=='台中'].boxplot(column='total_price', by='room_number', figsize=(16,6))
plt.show()
new_data.loc[new_data['city']=='台中'].boxplot(column='unit_price_square_feet', by='new_towns', figsize=(16,6))
plt.show()

print(le.inverse_transform([76]))