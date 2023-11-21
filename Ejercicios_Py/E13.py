# Implementa la clase “Matriz” con los atributos int rows, int columns e int[rows][columns] matrix,
# que contenga los siguientes métodos: 
#- getNumberRows(): devuelve el número de filas de la matriz.
#- getNumberColumns(): devuelve el número de columnas de la matriz.
#- setElement(int x, int j, int element): cambia el valor de la matriz en [x][j] por el valor de [element].
#- addMatrix(int[][] matrix): suma todos los elementos de la matriz actual a los elementos de [matrix], 
#   y el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número de filas y
#   columnas que la matriz inicial, la operación no se puede realizar (notificalo).
#- multMatrix(int[][] matrix]: multiplica todos los elementos de la matriz actual a los elementos de [matrix],
# y el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número de filas y columnas que
# la matriz inicial, la operación no se puede realizar (notificalo).




class Matriz:
    def __init__ (self, rows, columns, initial_value=0):
        self.rows = rows
        self.columns = columns
        self.matrix = [[initial_value] * columns for _ in range(rows)]
    
    #metodos get
    def getNumberRows(self):
        return self.rows
    
    def getNumberColumns(Self):
        return Self.columns
    
    
    #metodos set

    def setRows (self, rows):
        self.rows = rows
    
    def setColumns(self, columns):
        self.columns = columns
    
    def setElement(self, x, j, element):
        if 0 <= x < self.rows and 0 <= j < self.columns:
            self.matrix[x][j] = element
        else:
            print("Índices fuera de los límites de la matriz.")
    
    def addMatrix(self,matrix):
        if len(matrix) != self.rows or len(matrix[0]) != self.columns:
            print("Las matrices no tienen las mismas dimensiones y no se pueden sumar")
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] += matrix[i][j]

    def mulMatrix(self, matrix) :
        if len(matrix) != self.rows or len(matrix[0]) != self.columns:
            print("Las matrices no tienen las mismas dimensiones y no se pueden multiplicar")
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] *= matrix[i][j]
    

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])



matriz1 = Matriz(2, 2, initial_value=1)
matriz2 = [[1, 5], [4, 6]]
print(matriz1)
matriz1.addMatrix(matriz2)
print("La suma de las matrices es : ", "\n" , matriz1)
matriz1.mulMatrix(matriz2)
print("La multiplicación de las matrices es : ", "\n" , matriz1)

matriz3 = [[1, 5, 8], [4, 6, 2]]
print(matriz1)
matriz1.addMatrix(matriz3)
matriz1.mulMatrix(matriz3)
