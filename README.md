# ECG Peak Labeller 📈💗

Welcome to the ECG Peak Labeller! This is a tool designed to help you identify and label the R-peaks in ECG data stored as a numpy array.

## Requirements 🧰
- pandas>=1.5.0
- numpy>=1.23.0
- streamlit>=1.22.0
- plotly>=5.9.0
- streamlit-plotly-events>=0.0.6
- wfdb>=4.0.0
  
## Installation 🔧

1. Clone the repository: `git clone https://github.com/<username>/<repository>.git`
2. Install the dependencies: `pip install -r requirements.txt`

## Usage 🚀

1. Run `streamlit run ecg_PL.py`
2. Select one of the unlabeled ECG signals on the drop down box.
3. Click on the peaks in the plot. Each click will mark a peak with a red circle and its index will be displayed on the bottom of the plot.
5. If you need more precission, you can select an area to zoom in.
6. Once all peaks have been identified, click on "Save Peaks". The list of peaks will be saved to a numpy array and exported to a the pickle file.
7. Once peaks are saved, the ECG is ticked as "Labeled", so it won't show in the dropdown.
8. Click on "Clear peaks" to clear the plot and start over.

## Example 🎉

## License 📜

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments 🙏

This project was inspired by my passion for physiological data analysis and my love for Python programming. Thank you to all the open-source contributors whose work made this possible.

## Future
- Load your ECG numpy array by clicking on "Open ECG Data"