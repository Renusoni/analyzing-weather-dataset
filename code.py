# --------------
#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 
from pandas import DataFrame


#Code for categorical variable
def categorical(df):
   categorical_var=df.select_dtypes(include='object')
   return categorical_var
   
 
#Code for numerical variable
def numerical(df):
   numerical_var=df.select_dtypes(include='number')
   return numerical_var 
   
   
#code to check distribution of variable

def clear(df,col,val):
   series = df.apply(lambda x: True if x[col] == val else False , axis=1)
   numOfRows = len(series[series == True].index)
   return numOfRows

#Code to check instances based on the condition

def instances_based_condition(df,col1,val1,col2,val2):
    instance = df[(df[col1] > val1) & (df[col2]== val2)]
    return instance
   
# Code to calculate different aggreagted values according to month

def agg_values_ina_month(df,date_col,agg_col,agg):
   aggregated_value=pd.pivot_table(df,index=date_col,values=agg_col,aggfunc=agg)
   return aggregated_value

# Code to group values based on the feature
def group_values(df,col1):
    mean_weather=df.groupby(col1).agg(np.mean)
    return mean_weather
    
    
# function for conversion 
def convert(df,celsius):
    converted_temp=1.8*celsius + 32
    return converted_temp
    
    

weather=pd.read_csv(path)

categorical_var=categorical(weather)
print("categorical_var: ",categorical_var)

numerical_var=numerical(weather)
print("numerical_var: ",numerical_var)

value=clear(weather,'Weather','Cloudy')
print("Cloudy_value: ",value)

aggregated_value=agg_values_ina_month(weather,['Date/Time'],['Temp (C)'],'mean')
print("aggregated_value: ",aggregated_value)

mean_weather=group_values(weather,['Weather'])
print("aggregated_value: ",mean_weather)

converted_temp=convert(weather,weather['Temp (C)'])
print("converted_temp: ",converted_temp)

wind_speed_35_vis_25=instances_based_condition(weather,'Wind Spd (km/h)',35,'Visibility (km)',25)

print("wind_speed_35_vis_25: ",wind_speed_35_vis_25)






