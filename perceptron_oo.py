import random
from matplotlib import pyplot as plt
import numpy as np

class perceptron:
    
    def  fit(self, x:list, y:list, epochs:int = 10):
        weight = self._create_weight(len(x[0]))
        
        for i in range(len(x)):
            x[i] = [1] + x[i]
      
        for k in range(epochs):
            for i in range(len(x)):
                
                net = self._net(x[i], weight) 
                yi = 1 if net >= 0 else 0
                print(f"Valor esperado: {y[i]}\nValor predito: {yi}")
                
                for j in range(len(weight)):
                    weight[j] = weight[j] + 0.1 * (y[i] - yi) * x[i][j]

            print("-----------------------------------------------")
            print(f"Fim {k}")
        
        
    def _net(self, x, w):
        net = 0
        for i in range(len(x)):
            #print(f"{x[i]} * {w[i]}")
            net += x[i] * w[i]
        return net
            
    def _create_weight(self, inputs):
        weight = [random.uniform(-1, 1) for _ in range(inputs+1)]
        print(f"Weight: {weight}")
        return weight
