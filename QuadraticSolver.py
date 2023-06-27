import cmath
import math

class QuadraticEquation():
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        self.delta: float = None
        self.typeOfRoots: str = None
        self.roots = []
        
    def show_equation(self) -> str:
        return f"{self.getA()}x^2 + {self.getB()}x + {self.getC()} = 0"
        
    def setDelta(self, delta: float) -> None:
        self.delta = delta
        
    def setRoot(self, root: float) -> None:
        self.roots.append(root)
        
    def setTypeOfRoots(self, delta: float) -> None:
        if delta < 0:
            self.typeOfRoots = "COMPLEX"
        elif delta > 0:
            self.typeOfRoots = "TWO_ROOTS"
        else:
            self.typeOfRoots = "DOUBLE_ROOTS"
        
    def getA(self) -> float:
        return self.a
    
    def getB(self) -> float:
        return self.b
    
    def getC(self) -> float:
        return self.c
    
    def getDelta(self) -> float:
        return self.delta
    
    def getRoots(self) -> list:
        return self.roots
    
    def getTypeOfRoots(self) -> str:
        return self.typeOfRoots
    

class QuadraticSolver():
    def __init__(self):
        print("Calculadora de equacoes quadraticas!")
        self.equation: type[QuadraticEquation] = None
        
    def __setEquation(self, a, b, c) -> None:
        self.equation = QuadraticEquation(a, b, c)
        return
        
    def __getEquation(self) -> type[QuadraticEquation]:
        return self.equation
    
    def inputEquation(self) -> type[QuadraticEquation]:
        print("Insira o valor dos coeficientes da equacao quadratica\n")
        a = 0
        while a == 0:
            a = int(input("Insira o valor de a: "))
            b = int(input("Insira o valor de b: "))
            c = int(input("Insira o valor de c: "))
            
            self.__checkInput(a, b, c)
            
    def __checkInput(self,a: int, b: int, c: int) -> None:
        if a != 0:
            self.__setEquation(a, b, c)
        else:
            Exception("Insira um valor de a válido!")
    
    def __complexRootsSolution(self) -> list:
        equationObj = solver.__getEquation()
        
        a = equationObj.getA()
        b = equationObj.getB()
        delta = equationObj.getDelta()
        
        root1 = (-b + cmath.sqrt(delta))/ (2 * a)
        root2 = (-b - cmath.sqrt(delta))/ (2 * a)
        
        equationObj.setRoot(root1)
        equationObj.setRoot(root2)
        
        return equationObj.getRoots()
    
    def __twoRootsSolution(self) -> list:
        equationObj = solver.__getEquation()
        
        a = equationObj.getA()
        b = equationObj.getB()
        delta = equationObj.getDelta()
    
        root1 = (-b + math.sqrt(delta))/ (2 * a)
        root2 = (-b - math.sqrt(delta))/ (2 * a)
        
        equationObj.setRoot(root1)
        equationObj.setRoot(root2)
        
        return equationObj.getRoots()
    
    def __doubleRootSolution(self) -> list:
        equationObj = solver.__getEquation()
        
        a = equationObj.getA()
        b = equationObj.getB()
        
        root = -b / (2 * a)
        
        equationObj.setRoot(root)
        
        return equationObj.getRoots()
    
    def delta(self) -> float:
        equationObj = solver.__getEquation()
        
        a = equationObj.getA()
        b = equationObj.getB()
        c = equationObj.getC()
        
        delta = (b ** 2) -4 * (a) * (c)
        equationObj.setDelta(delta)
        equationObj.setTypeOfRoots(delta)
        
        return self.__getEquation().getDelta()
    
    def roots(self) -> list:
        equationObj = solver.__getEquation()
        
        typeOfRoot = equationObj.getTypeOfRoots()
    
        if typeOfRoot == "COMPLEX":
            self.__complexRootsSolution()
        elif typeOfRoot == "TWO_ROOTS":
            self.__twoRootsSolution()
        else:
            self.__doubleRootSolution()
            
    def show_roots(self) -> None:
        equationObj = solver.__getEquation()
        
        roots = equationObj.getRoots()
        equation = equationObj.show_equation()
        
        print(f"\nA equacao {equation} tem como raizes:")
        for index, root in enumerate(roots):
            print(f"({index + 1}º) {root}")
            
solver = QuadraticSolver()
solver.inputEquation()
solver.delta()
solver.roots()
solver.show_roots()

            
