if __name__ == "__main__":
    import pandas as pd
    data=pd.read_csv('.//data//CRDC2013_14.csv',encoding='Latin-1')
    jj = data['JJ'].value_counts()
    sch = data['SCH_STATUS_MAGNET'].value_counts()
    table_1 = pd.pivot_table(data,values=['TOT_ENR_M','TOT_ENR_F'],index='JJ', aggfunc='sum')
    table_2 = pd.pivot_table(data,values=['TOT_ENR_M','TOT_ENR_F'],index='SCH_STATUS_MAGNET', aggfunc='sum')
    print(table_1,table_2)