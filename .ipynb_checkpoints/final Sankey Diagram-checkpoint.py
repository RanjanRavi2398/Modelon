from pyfmi.common.io import ResultDymolaBinary
import pandas as pd
import sys
import numpy as np
from  plotly.offline import plot
from plotly.graph_objs import *
      # get the data from the values dictionary
mat=ResultDymolaBinary(TestValues.mat)
mat_name=mat.name
Node=[mat_name]
for y in Node:
    data_1=[data for data in y if ".k" not in data]
    data_2=[data for data in data_1 if ".y" not in data]
    Data1=[data for data in data_2 if "_" not in data]
    Data=[data for data in Data1 if "Time" not in data]
Str=[ ]
for DATA in Data:
    Str.append(DATA)
len_data=len(Data)
for i in Data:
    time=mat.get_variable_data(i).t

Value=[]
for i in Data:
    value=mat.get_variable_data(i).x
    Value.append(value)
def is_negated(self, name):
        """
        Returns True if the given name corresponds to a negated result vector.
        
        Parameters::
        
            name -- 
                Name of the variable/parameter/constant.
                
        Returns::
        
            True if the result should be negated
        """
        varInd  = self.get_variable_index(name)
        dataInd = self.raw['dataInfo'][1][varInd]
        if dataInd<0:
            return True
        else:
            return False
for i in Data:
    value=mat.is_negated(i)
SourceSupply = []
for i in range(0, len_data):
    item = str(input())
    SourceSupply.append(item)
len_source=len(SourceSupply)
Link_color=['#262C46','#ff3344','#ffbbcc','#776647','#446677','#336677','#448899','#556677']
len_color=len(Link_color)
Supply=[]
Colors_1=[]
for i in  range(0,len_data):
    for j in range(0,len_source):
        if (SourceSupply[i]==Data[j]):
            Supply.append(j)
            Colors_1.append(Link_color[j])

Transformation = []
for i in range(0, len_data):
    item = str(input())
    Transformation.append(item)
len_transformation=len(Transformation)
Trans=[]
Colors_2=[]
for i in  range(0,len_data):
    for j in range(0,len_transformation):
        if (Transformation[i]==Data[j]):
            Trans.append(j)
            Colors_2.append(Link_color[j])

Consumption = []
for i in range(0,len_data):
    item = str(input())
    Consumption.append(item)
len_consumption=len(Consumption)
consume=[]
Colors_3=[]
for i in  range(0,len_data):
    for j in range(0,len_consumption):
        if (Consumption[i]==Data[j]):
            consume.append(j)
            Colors_3.append(Link_color[j])
Source=np.concatenate((Supply,Trans))
Target=np.concatenate((Trans,consume))
Colors=np.concatenate((Colors_1,Colors_2,Colors_3))
from  plotly.offline import plot
from plotly.graph_objs import *


trace1 = {
  "link": {
    "color": Colors,
    "value": [6157,6157,387,387,2383,2383,1240,1240,1240,1240,-1418,345,4555,6455,4554,665,6545,657,543,656,7666,6563,3454], 
    "source": Source, 
    "target": Target
  }, 
  "node": {
    "pad": 10, 
    "line": {
      "color": "Black", 
      "width": 0.5
    }, 
    "color": ['#262C46','#ff3344','#ffbbcc','#776647','#446677','#336677','#448899','#556677'], 
    "label":Str,
    "thickness": 30
  }, 
  "type": "sankey", 
  "domain": {
    "x": [0, 1], 
    "y": [0, 1]
  }, 
  "orientation": "h", 
  "valueformat": ".0f"
}
data = Data([trace1])

fig = Figure(data=data)
plot(fig)

