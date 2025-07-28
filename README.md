asd
# Potentiostat Data Visualization & Analysis

This project provides a suite of Python scripts to analyze and visualize data collected from cyclic voltammetry (CV) experiments using a three-electrode potentiostat setup. It is designed for both research and educational use, especially for introducing high school and undergraduate students to electrochemical data analysis.

## 📁 Project Structure

```
Potentiostat_Data_Viz/
├── data/                  # Raw CV data files (tab-delimited .txt)
├── output/
│   ├── plots/             # Auto-generated plots (PNG)
│   └── txt_files/         # Analysis summaries (text)
├── src/                   # Core Python scripts
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
```

## 📜 Available Scripts (in `src/`)

### `analyze_cv.py`
- Prompts user for a CV data file path.
- Separates oxidation and reduction currents.
- Numerically integrates each to estimate total charge transferred.
- Outputs results to console and saves a summary `.txt` file to `output/txt_files/`.

### `plot_cv.py`
- Prompts user for a file path.
- Plots **current vs. voltage** (Ewe vs <I>).
- Saves the figure to `output/plots/` with a timestamped name.

### `plot_ct.py`
- Same as `plot_cv.py`, but plots **current vs. time**.
- Also saves output to `output/plots/`.

## 🧪 Sample Output

- Numerical integration (oxidation/reduction charge)
- PNG plots of CV scans
- Output filenames include:
  - The script name
  - The input data filename
  - A timestamp

Example:
```
output/txt_files/analyze_cv_1M-ZnSO4-20mVs_C16_20250728_155102.txt
output/plots/plot_cv_1M-ZnSO4-20mVs_C16_20250728_154337.png
```

## ⚙️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/Potentiostat_Data_Viz.git
   cd Potentiostat_Data_Viz
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run a script:**
   ```bash
   python src/analyze_cv.py
   ```

## 🧠 Educational Use

This project is designed to:
- Reinforce electrochemical concepts like plating/stripping and coulombic efficiency.
- Provide students with hands-on data analysis experience.
- Bridge experimental chemistry and computational tools.

## 🧼 Notes

- The `.gitignore` has been configured to **allow tracking of data files** for reproducibility.
- If you encounter issues with `trapz` deprecation warnings, consider switching to `numpy.trapezoid()` or `scipy.integrate`.

## 📬 Contact

Feel free to reach out or open an issue if you’d like to contribute or need help setting up your own experiments for analysis.