Data-Driven machine learning approaches for Lithium-ion Batteries RUL Prediction

Dataset: Battery Dataset from NASA prognostic centre of excellence

objectives:
1. predicting capacity degradation of battery using features like voltage charge,discharge,current charge,discharge and temperature

2. predicting remaining useful life of lithium ion batteries using machine learning models 

Dataset consists of 32 batteries which contains charge and discharge cycles, we need to convert the .mat files(32 .mat files) into pickle files

We get 32 pickle files saved in Dataset/data folder

we use specific features for each model

for 1st model we used

1.Cycle index
2.Temperature charge
3.Temperature discharge
4.voltage charge
5.voltage discharge
6.current charge
7.current discharge


for 2nd model we used

features->
1.capacity
2.charge time
3.discharge time
4.cycle index
5.max voltage discharge
6.min voltage charge
7.total time (charge time + discharge time)

target: RUL
