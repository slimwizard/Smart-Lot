## This code assumes that the training data is in a folder called training data in this format:
training-data
     -occupied
     -unoccupied

## Similarly, we need the validation dataset in a similar format:

testing-data
     -occupied
     -unoccupied

1. In order to start the training: 

python train.py --train training-data/ --val testing-data/ --num_classes 2

2. Once your model is trained, it will save the model files in the current folder. 

## In order to predict using the trained model, we can run the predict.py code by passing it our test image. 

python predict.py testing-data/occupied/occupied_555.png

Result will be in format: [[confidence_of_occupied_spot confidence_of_unoccupied_spot]]
Confidence values are on a scale of 0 to 1, so the closer to one the prediction is, the more confident the model is in its prediction. Passing in an occupied spot to predict.py should result in something close to [[1 0]] and vice versa.
