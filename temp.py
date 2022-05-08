import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/Dev Goel/Desktop/deploy/trained_model.sav', 'rb'))

input_data = (1,0.874525,0,0,1,2,0,-0.616568,0.765941,2)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person does not have a stroke')
else:
  print('The person have a stroke')