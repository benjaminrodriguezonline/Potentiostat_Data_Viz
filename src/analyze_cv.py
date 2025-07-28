import pandas as pd
import numpy as np
import os
from datetime import datetime

# Prompt user for file path
file_path = input("Enter the path to the CV data file: ").strip().strip('"')

data = pd.read_csv(file_path, sep='\t')
time = data['time/s']
current = data['<I>/mA']

current_ox = current.clip(lower=0)
current_red = current.clip(upper=0)

charge_ox = np.trapz(current_ox, time)
charge_red = np.trapz(current_red, time)

print(f'Oxidation Charge: {charge_ox:.4f} mC')
print(f'Reduction Charge: {charge_red:.4f} mC')

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
base_name = os.path.basename(file_path).replace('.txt', '')
script_name = os.path.splitext(os.path.basename(__file__))[0]
txt_output_filename = f'{script_name}_{base_name}_{timestamp}.txt'

os.makedirs('output/txt_files', exist_ok=True)
with open(f'output/txt_files/{txt_output_filename}', 'w') as f2:
    f2.write(f'Oxidation Charge: {charge_ox:.4f} mC\n')
    f2.write(f'Reduction Charge: {charge_red:.4f} mC\n')

# with open('output/txt_files/integrated_charges.txt', 'w') as f2:
#     f2.write(f'Oxidation Charge: {charge_ox:.4f} mC\n')
#     f2.write(f'Reduction Charge: {charge_red:.4f} mC\n')