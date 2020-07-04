if __name__ == "__main__":
    import pandas as pd
    data=pd.read_csv('.//data//CRDC2013_14.csv',encoding='Latin-1')
    data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']
    all_enrollment = data['total_enrollment'].sum()
    enrol = data.loc[:, data.columns.str.contains(r'^SCH_ENR_[A-Z]{2}_[FM]$')]
    enrol_sum = enrol.sum()
    race_gender_ratio = enrol_sum/all_enrollment
    print(race_gender_ratio)
    
    