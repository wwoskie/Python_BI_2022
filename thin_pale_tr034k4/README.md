# Script to finally get thin pale tr034k4. 

Has function `sort_dataframes_by_mean(data, column)` that takes for input list pf dataframes and column name. Fir each df it calculates mean and max value in the column. Then it rearranges the given list according to mean values. If mean values for target column are equal it arranges df based on their max values in column. If max values are equal too only god knows what happens...

Uses `pandas`. All requirements are stored in `requirements.txt` file.
