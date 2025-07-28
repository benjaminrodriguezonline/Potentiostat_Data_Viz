import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from datetime import datetime

def plot_ct(filename):
    try:
        # Load the data from the text file
        df = pd.read_csv(filename, sep='\t', skiprows=1, names=["Ewe_V", "I_mA", "time_s"])

        # Plot Current vs Time
        plt.figure(figsize=(10, 6))
        plt.plot(df["time_s"], df["I_mA"], color='blue')
        plt.xlabel("Time (s)")
        plt.ylabel("Current (mA)")
        plt.title("Current vs Time")
        plt.grid(True)
        plt.tight_layout()
        # Prepare output filename
        os.makedirs("output/plots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = os.path.splitext(os.path.basename(filename))[0]
        script_name = os.path.splitext(os.path.basename(__file__))[0]
        output_filename = f"output/plots/{script_name}_{base_filename}_{timestamp}.png"
        plt.savefig(output_filename)
        plt.show()

    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        filepath = input("Enter path to CV data file: ").strip()
    
    plot_ct(filepath)
