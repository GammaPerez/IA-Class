#PRACTICA 01
#ALUMNO: Gamaliel Jabneel Perez Esquivel 19180927
#MATERIA: Inteligencia artificial
#DOCENTE: Stephanie Cordero Martínez
import numpy as np

class perceptron(object):
    #"""
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        #"" Fit training data.
        self.w_=np.zeros(1+X.shape[1])
        self.errors_=[]

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                update = self.eta * (target -self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self


    def net_input (self,X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict (self, X):
        return np.where(self.net_input(X) >=0.0,1,-1)
    
import pandas as pd

df = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None)
df.tail()


# <hr>
# 
# ### Nota:
# 
# 
# Puedes encontrar una copia del conjunto de datos Iris (y del resto de conjuntos de datos que se utilizan en este libro) en los paquetes de código de este libro, que puedes utilizar si trabajas offline o si el servidor UCI ubicado en https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data está fuera de servicio temporalmente. Por ejemplo, para cargar el conjunto de datos Iris desde un directorio local, puedes sustituir la línea  
# 
#     df = pd.read_csv('https://archive.ics.uci.edu/ml/'
#         'machine-learning-databases/iris/iris.data', header=None)
#  
# po
#  
#     df = pd.read_csv('tu/ruta/local/a/iris.data', header=None)
# 

# In[10]:


df = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None)
df.tail()


# <hr>


# ### Representar el conjunto Iris

# In[11]:


import matplotlib.pyplot as plt
import numpy as np

#  seleccionar setosa y versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# extraer longitud de sépalo y longitud de pétalo
X = df.iloc[0:100, [0, 2]].values

# representar los datos
plt.scatter(X[:50, 0], X[:50, 1],
            color='#00BFBF', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='#8A2BE2', marker='x', label='versicolor')

plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')

# plt.savefig('images/02_06.png', dpi=300)
plt.show()

    

