import pandas as pd

df = pd.read_excel('fifa21_raw_data.xlsx')
def feet_inches_to_cm(height):
    feet, inches = height.split('\'')
    total_inches = int(feet) * 12 + int(inches.strip('"'))
    return total_inches * 2.54

def lbs_to_kg(weight):
    lbs = ''.join(filter(str.isdigit, weight))
    converted_weight = int(lbs) * float(0.45)
    return f"{converted_weight:.2f}kg"

def value_digits(value):
    if isinstance(value, str):
        value = value.replace('â‚¬', '').replace(',', '')
        if 'M' in value:
            return int(float(value.replace('M', '')) * 1000000)
        elif 'K' in value:
            return int(float(value.replace('K', '')) * 1000)
    else:
        return int(value)

df['Joined'] = pd.to_datetime(df['Joined'])
df['Month'] = df['Joined'].dt.month
df['Year'] = df['Joined'].dt.year
df = df.rename(columns={'â†“OVA':'OVA'})

df.drop(columns=['W/F','SM','IR','Joined','Loan Date End'], inplace=True)

df['Height (cm)'] = df['Height (cm)'].apply(feet_inches_to_cm)
df['Weight'] = df['Weight'].apply(lbs_to_kg)
df['Value'] = df['Value'].apply(value_digits)
df['Wage'] = df['Wage'].apply(value_digits)
df['Release Clause'] = df['Release Clause'].apply(value_digits)

print(df[['Height (cm)','Weight','Value','Wage','Month','Year', 'OVA']])

df.to_excel('Cleaned_Fifa21_Data.xlsx', index=False)