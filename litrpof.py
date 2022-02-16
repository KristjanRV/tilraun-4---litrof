import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

 
data = pd.read_csv('C:\\Users\\krist\\OneDrive\\Documents\\Hlutir\\HÍ\\Önn 6\\Verkleg stjarneðlisfræði\\3. hulduefni\\dataset_spectra_Arcturus_and_Sun.txt', engine = 'python', sep='\s+', header = None, skiprows = 37600, skipfooter = 17998 )

print(data)

angstrom = data[0]
print(angstrom)
arcturus = data[1]
sol = data[2]

plt.plot(angstrom, sol, label = 'Sun spectra')
plt.plot(angstrom, arcturus, label = 'Arcturus spectra')
plt.legend()
plt.xlabel('Wavelength (Å)')
plt.ylabel('Normalized spectra')
plt.show()