import numpy as np 
import math
import matplotlib.pyplot as plt
import pandas as pd

the_array = np.array([[8.12,5.53,2.31],
[5.41, 5.59, 2.43],
[2.71, 2.88, 3.05]])
eigenvalues, eigenvectors = np.linalg.eig(the_array)
#print(eigenvalues, eigenvectors)

all_data = pd.read_excel('/Users/v.w./Desktop/cambridge/IB/LAB/A2/A2.xlsx', header = None)

for i in range (0, 11):
    section = all_data.loc[(2+5*i):(4+5*i), 1:3]
    name = all_data.loc[1+5*i, 1]
    new_section = np.array(section, dtype=float)
    new_section = new_section[:3, :3]

    eigenvalues, eigenvectors = np.linalg.eig(new_section)
    eigenvalues = pd.DataFrame(eigenvalues)
    det = np.linalg.det(new_section)
    #writer = pd.ExcelWriter('/Users/v.w./Desktop/cambridge/IB/LAB/A2/A2.xlsx') 
    #eigenvalues.to_excel(writer, cols=4, startrow=(5*i+3))
    #writer.save()

    print(f"{name} eigenvalues are: {eigenvalues}")
    #print(f"eigenvectors are: {eigenvectors}")
    print(f"determinant: {det}")
    print("__________________________________________")