
import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_cv(filename):
    try:
        # Load the data from the text file
        df = pd.read_csv(filename, sep='\t', skiprows=1, names=["Ewe_V", "I_mA", "time_s"])

        # Plot Current vs Voltage
        plt.figure(figsize=(10, 6))
        plt.plot(df["Ewe_V"], df["I_mA"], color='blue')
        plt.xlabel("Potential vs Ag/AgCl (V)")
        plt.ylabel("Current (mA)")
        plt.title("Cyclic Voltammetry Curve")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python plot_cv.py <path_to_cv_data.txt>")
    else:
        plot_cv(sys.argv[1])
