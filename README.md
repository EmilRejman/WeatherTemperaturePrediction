## Temperature prediction
In this project I have tried to predict mean daily temperature for next 3 days for vilage where my parents live in Poland - Tajęcina
(prediction from single datapoint). Data gathered from: https://power.larc.nasa.gov/data-access-viewer/ .
For now it have been done with linear regresion and simple Neural network, geting average prediciton error for 3 days with best models around ~2.16*C for LL and ~2.05*C for NN.

The project is sapareted into parts:
- Data Analize
- Linear_regression prediction
- NN prediction.

Data analize shall be run before prediction files to prepere the data.

Further description in jupyter-notebook files.

Currently workng on: RNN, get data from different points for api and predict temperature with better accuracy and longer period (5 days). 

made with python 3.7 

##### running the app:
* install jupyter-notebook on Venv or main python
* Run ``` pip install -r requirements.txt```


