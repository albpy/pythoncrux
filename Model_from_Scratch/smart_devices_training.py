from NNSD import Layer_Dense
from NNSD import Activation_ReLU, Activation_Softmax
from NNSD import Loss_CategoricalCrossentropy
from NNSD import Optimizer_SGD, np, Model
from NNSD import Accuracy_Categorical
from smart_devices import X_train, X_valid, y_train, y_valid, X_test, y_test,X,y, Data_, ord_enc, new_encoded_column, old_column_name
import pandas as pd
np.set_printoptions(threshold=np.inf)
model = Model()
model.add(Layer_Dense(31, 40))
model.add(Activation_ReLU())
model.add(Layer_Dense(40, 50))
model.add(Activation_ReLU())
model.add(Layer_Dense(50, 40))
model.add(Activation_ReLU())
model.add(Layer_Dense(40, 13))
model.add(Activation_Softmax())
model.set(loss = Loss_CategoricalCrossentropy(), optimizer = Optimizer_SGD(learning_rate=.009, decay = 0), accuracy= Accuracy_Categorical())
model.finalize()
model.train(X_train[:105039].to_numpy().astype(int), y_train[:105039].to_numpy().astype(int), batch_size = 100, epochs = 10, print_every = 100)
# loss = Loss_CategoricalCrossentropy()
# [:105039]
parameters = model.get_parameters()
model.predict(X_test[:5].to_numpy.astype(int))