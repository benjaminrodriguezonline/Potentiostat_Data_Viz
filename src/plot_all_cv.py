import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FOLDER = "data"
FILE_EXTENSION = ".txt"

def plot_all_cv():
    plt.figure(figsize=(10, 6))

    # Loop through all .txt files in the data folder
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(FILE_EXTENSION):
            filepath = os.path.join(DATA_FOLDER, filename)
            try:
                df = pd.read_csv(filepath, sep='\t', skiprows=1, names=["Ewe_V", "I_mA", "time_s"])
                plt.plot(df["Ewe_V"], df["I_mA"], label=filename)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    plt.xlabel("Potential vs Ag/AgCl (V)")
    plt.ylabel("Current (mA)")
    plt.title("Cyclic Voltammetry Curves")
    plt.legend(fontsize="small", loc="best")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_all_cv()