# Data Manipulation with Pandas

This repository contains a Jupyter Notebook named `Datasets Task.ipynb` designed to demonstrate essential data manipulation techniques using pandas. The notebook guides users through various tasks involving data selection, filtering, and sorting within a dataset.

## Description

The `Datasets Task.ipynb` notebook is structured to provide hands-on experience with pandas dataframes, focusing on:
- Selecting specific columns and observations.
- Filtering data based on specific criteria.
- Sorting data by specific attributes.

### Tasks Included

1. **Column and Row Selection**:
   - Select specific columns from the first few observations in the dataset.
2. **Conditional Filtering**:
   - Filter and display observations based on the number of cards.
3. **Data Sorting**:
   - Sort the entire dataset by the 'Education' column in descending order to prioritize higher education values.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Jupyter Notebook or JupyterLab
- pandas library

You can install the necessary Python packages using pip:
```bash
pip install notebook pandas
```
or
```bash
pip3 install notebook pandas
```
### Installation
1. Clone this repository to your local machine using Git:
```bash
git clone https://github.com/dreamVaux/my_bootcamp_tasks.git
```
2. Navigate to the cloned directory.

### Running the Notebook
To open the notebook, run the following command in your terminal within the directory containing the notebook:
```bash
jupyter notebook Datasets Task.ipynb
```
or if you are using JupyterLab:
```bash
jupyter lab Datasets Task.ipynb
```
### Notebook Explanation
The notebook includes detailed comments and explanations for the following common pandas operations using iloc:
- df.iloc[:,: ]: Selects all rows and columns in the dataframe.
- df.iloc[5:,5:]: Selects rows starting from the 6th and columns starting from the 6th onward.
- df.iloc[:,0]: Selects all rows from the first column.
- df.iloc[9,:]: Selects all columns from the 10th row.

### Contributing
Contributions to enhance the content of this notebook or improve its explanations are welcome! Please fork the repository and submit a pull request with your changes.

### License
This project is licensed under the MIT License - see the LICENSE file for details.