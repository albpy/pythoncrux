import numpy as np
from Data_view import Data
from nnfs.datasets import spiral_data

np.random.seed(0)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.05 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs, training):
        self.output = np.dot(inputs, self.weights)+self.biases
        self.inputs = inputs
    def backward(self, dvalues):
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)

        #Gradient on values
        self.dinputs =np.dot(dvalues, self.weights.T)

    def get_parameters(self):
        return self.weights, self.biases
    def set_parameters(self, weights, biases):
        self.weights = weights
        self.biases = biases

class Activation_ReLU:
    def forward(self, inputs, training):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)
    def backward(self, dvalues):
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0
class Activation_Softmax:
    def forward(self, inputs, training):
        exp_values = np.exp(inputs - np.max(inputs, axis = 1, keepdims = True)) #To prevent exploding neurons
        probabilities = exp_values / np.sum(exp_values, axis=1,keepdims=True)
        self.output = probabilities
    def backward(self, dvalues):
        self.dinputs = np.empty_like(dvalues)
        for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):
            #flatten
            single_output = single_output.reshape(-1,1)
            #Jacobian matrix of o/p
            jacobian_matrix = np.diagflat(single_output) - np.dot(single_output, single_output.T)
            #sample-wise gradient
            self.dinputs[index] = np.dot(jacobian_matrix, single_dvalues)

    def predictions(self, outputs):
        return np.argmax(outputs, axis=1)

class Loss:
    #Set or remember trainable layers
    def remember_trainable_layers(self, trainable_layers):
        self.trainable_layers = trainable_layers

    def calculate(self, output, y,*, include_regularization = False):
        sample_losses = self.forward(output, y) #calculate the sample losses ie. predicted loss
        #Calculate mean loss
        data_loss = np.mean(sample_losses)
        self.accumulated_sum += np.sum(sample_losses)
        self.accumulated_count+=len(sample_losses)
        #Need to include regularization
                 
        return data_loss
    #for batches as accumulated loss is necessary for class Loss and class Accuracy
    def calculate_accumulated(self, *, include_regularization = False):
        #Calculate mean loss
        data_loss = self.accumulated_sum/self.accumulated_count
        #Need to include regularization
        return data_loss

    #Reset values for accumulated for accumulated loss for next/new epoch
    def new_pass(self):
        self.accumulated_sum = 0
        self.accumulated_count = 0


class Loss_CategoricalCrossentropy(Loss):

    def forward(self, y_pred, y_true):
        #number of samples in a batch
        samples = len(y_pred)
        

        #clip data to prevent division by 0
        #Clip both sides to not drag mean towrds any value
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)
        
        # probablities
        #only for categorical labels
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]

        #Mask values - only for one hot encoded labels
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped * y_true, axis =1)

        # losses 
        negative_log_likekihoods = -np.log(correct_confidences)
        return negative_log_likekihoods
    def backward(self, dvalues, y_true):
        samples = len(dvalues)
        labels = len(dvalues[0])

        #one hot vec
        if len(y_true.shape) == 1:
            y_true = np.eye(labels)[y_true]
        #calculate gradient
        self.dinputs = -y_true/dvalues

        #Normalize gradient
        self.dinputs = self.dinputs/samples

class Optimizer_SGD:
    #Settings
    #Learning rate of 1 is default for this optimeser
    def __init__(self, learning_rate=1.,decay = 0.,momentum=0.):
        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iterations = 0
        self.momentum = momentum

    def pre_update_params(self):
        if self.decay:
            self.current_learning_rate = self.learning_rate * (1. / (1. + self.decay * self.iterations))
    #Update parameters
    def update_params(self, layer):
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases += -self.learning_rate * layer.dbiases
    #call once after any parameter updates
    def post_update_params(self):
        self.iterations += 1
class Accuracy:
    #Calculate accuracy => Given predictions and ground truth values
    def calculate(self, predictions, y):
        #Get comparisons result
        comparisons = self.compare(predictions, y)
        accuracy = np.mean(comparisons)
        #add accumulated value of matching values and sample count
        self.accumulated_sum+= np.sum(comparisons)
        self.accumulated_count+= len(comparisons)
        return accuracy
    def calculate_accumulated(self):
        #calculate an accuracy
        accuracy = self.accumulated_sum/self.accumulated_count
        return accuracy
    def new_pass(self): #--> at the begining of each epoch
        self.accumulated_sum = 0
        self.accumulated_count = 0
#Accuracy for classification model 
class Accuracy_Categorical(Accuracy):
    def compare(self, predictions, y):
        if len(y.shape) == 2:
            y = np.argmax(y, axis=1)
        return predictions == y
    
#Primitive layer is the source of data to the first layer
class Layer_Input:
    #forward pass
    def forward(self, inputs, training):
        self.output = inputs 

class Model:
    def __init__(self):
        #Networkobject list
        self.layers = []
        #output of softmax classifiers
        self.softmax_classifier_output = None

    # Add object to the list
    def add(self, layer):
        self.layers.append(layer)

    #Set loss optimizer and accuracy
    def set(self, *, loss, optimizer, accuracy):
        if loss is not None:
            self.loss = loss
        if optimizer is not None:
            self.optimizer = optimizer
        if accuracy is not None:
            self.accuracy = accuracy
    def finalize(self):
        # Create and set input layer
        self.input_layer = Layer_Input()
        #Count all the objects
        layer_count = len(self.layers)
        #List for trainable layers
        self.trainable_layers = []
        #iterate all the objects for layers
        for i in range(layer_count):
            # if its first layer, previous object layer is input layer
            if i == 0:
                self.layers[i].prev = self.input_layer
                self.layers[i].next = self.layers[i+1]
            #All the layers except for first and last
            elif i < (layer_count - 1):
                self.layers[i].prev = self.layers[i-1]
                self.layers[i].next = self.layers[i+1]
            #The last object layer, which is loss -> Also lets save aside reference to last object whose output is model's output
            else:
                self.layers[i].prev = self.layers[i-1]
                self.layers[i].next = self.loss
                self.output_layer_activation = self.layers[i]
            #Add trainable layers to a variable
            if hasattr(self.layers[i], 'weights'):
                self.trainable_layers.append(self.layers[i])
            #Update trainble layers in loss object or add trainable layers if loss exists
            if self.loss is not None:
                self.loss.remember_trainable_layers(self.trainable_layers)

            

    def train(self, X, y, *, epochs=1, batch_size = None, print_every=1, validation_data=None):

        # defult step if batch size is not set
        train_steps =1
        # Set default batch size for training data as wel
        if validation_data is not None:
            validation_steps = 1

            X_val, y_val = validation_data

        #Calculation of number of steps
        if batch_size is not None:
            train_steps = len(X)//batch_size
            #add 1 more batch if there is any remaining data
            if train_steps * batch_size < len(X):
                train_steps += 1
            
            if validation_data is not None:
                validation_steps = len(X_val) // batch_size

                if validation_steps * batch_size < len(X_val):
                    validation_steps += 1 
        for epoch in range(epochs+1):
            print(f'epoch : {epoch}')

            #Reset accumulated values in loss and accuracy
            self.loss.new_pass()
            self.accuracy.new_pass()

            for step in range(train_steps):#-------------------->
                if batch_size is not None:
                    batch_X = X
                    batch_y = y
                
                else:
                    batch_X = X[step*batch_size : (step+1)*batch_size]
                    batch_y = y[step*batch_size : (step+1) * batch_size]
            
                output = self.forward(X, training = True)
                data_loss =   self.loss.calculate(output, y, include_regularization=False)
            
                loss = data_loss
                predictions = self.output_layer_activation.predictions(output)
                accuracy = self.accuracy.calculate(predictions, y)

                #backward pass
                self.backward(output, y)
            
                #Optimize (Update parameter)
                self.optimizer.pre_update_params()
                for layer in self.trainable_layers:
                    self.optimizer.update_params(layer)
                self.optimizer.post_update_params()

                if not step % print_every or step == train_steps-1:
                    print(f'step: {step}, ' + f'acc:{accuracy:.3f}, ' +f'loss:{loss:.3f}, '+ 
                      f'data_loss :{data_loss:.5f}, ' + f'lr : {self.optimizer.current_learning_rate} ')
            
            # Get and print each epoch and loss_accuracy
            epoch_data_loss = self.loss.calculate_accumulated()
            epoch_accuracy =self.accuracy.calculate_accumulated()
            
            print(f'training, ' + f'acc:{epoch_accuracy:.3f}, ' +f'loss:{epoch_data_loss:.3f}, '+ 
                      f'data_loss :{epoch_data_loss:.5f}, ' + f'lr : {self.optimizer.current_learning_rate} ')
                
            if validation_data is not None:
            
                self.loss.newpass()
                self.accuracy.newpass()

                for step in range(validation_steps):
                    if batch_size is not None:
                        batch_X = X_val
                        batch_y = y_val

                    #else slice batch for step
                    else:
                        batch_X = X_val[step * batch_size : (step+1)*batch_size]
                        batch_y = y_val[step * batch_size : (step+1)*batch_size]

                    output = self.forward(batch_X, training = False)
                
                    self.loss.calculate(output, batch_y, include_regularization=False)
                
                    
                    predictions = self.output_layer_activation.predictions(output)
                    accuracy = self.accuracy.calculate(predictions, batch_y)

                #

                    
                #Forward pass
                output = self.forward(X_val, training = False)
                # Calculate loss
                loss = self.loss.calculate(output, y_val)

                predictions = self.output_layer_activation.predictions(output)
                self.accuracy.calculate(predictions, batch_y)

            validation_loss = self.loss.calculate_accumulated()
            validation_accuracy = self.accuracy.calculate_accumulated()

            #print a summary
            print(f'validation, ' + f'acc: {validation_accuracy:3f}, ' + f'loss: {validation_loss:3f}')



    def forward(self, X, training):
        #forward method on input layer to set output property that first layer in "prev" object is expecting
        self.input_layer.forward(X, training)

        # call forward method for every object in chain
        # pass output of previous object as parameter
        for layer in self.layers:
            layer.forward(layer.prev.output, training)
        #layer is now last object from the list
        return layer.output 
    
# backward
    def backward(self, output, y):
        #Backward method on loss to set the dinput property
        self.loss.backward(output, y)

        for layer in reversed(self.layers):
            layer.backward(layer.next.dinputs)
    def get_parameters(self):
        #Create list of parameters
        parameters = []
        #Iterable trainable layers to  get their parameters
        for layer in self.trainable_layers:
            parameters.append(layer.get_parameters())

        #Return list
        return parameters
    def set_parameters(self, parameters):
        #iterate over parameters, layers and update each layer with each set of parameters
        for parameter_set, layer in zip(parameters, self.trainable_layers):
            layer.set_parameters(*parameter_set)

    def predict(self, X, *, batch_size = None):
        prediction_steps = 1
        
        if batch_size is not None:
            pass
        #To populate 
        output = []
        for step in range(prediction_steps):
            if batch_size is None:
                batch_X = X
            else: # Slice batch
                batch_X = X[step * batch_size : (step+1)*batch_size]
            
            batch_output = self.forward(batch_X, training=False)
            output.append(batch_output)
        return np.vstack(output)
        

# X = Data.drop("Group", axis = 1).to_numpy()
# y = Data["Group"].to_numpy()

# # X, y = spiral_data(samples=100,classes=3)
# print("X is ", X.shape)
# print("Y", y)

# dense1= Layer_Dense(2, 3)
# activation1 = Activation_ReLU()
# dense2 = Layer_Dense(3, 4)
# activation2 = Activation_Softmax()
# loss_function = Loss_CategoricalCrossentropy()

# #performing all forward pass of our training data
# dense1.forward(X)

# activation1.forward(dense1.output)

# dense2.forward(activation1.output)

# # print(dense2.output[:5])

# activation2.forward(dense2.output)

# print(len(activation2.output), (y.shape))

# loss = loss_function.calculate(activation2.output, y)
# print(loss)