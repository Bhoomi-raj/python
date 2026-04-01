import numpy as np
import pandas as pd
dict1 = {
    "name" : ["bhoomi","parth","poonam","payal","anish","vemula kaarthikeya"]
    ,"rollNo" : [1,2,3,4,5,6]
    ,"age" : [18,19,18,20,19,34]

}
df = pd.DataFrame(dict1)
print(df)
df.to_csv("pandasLIB.csv",index=False)
