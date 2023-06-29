import math
import cmath
from abc import ABC, abstractmethod

class Quadratic_Equation_Elements():
    def __init__(self):
        self.a = int(input("Insira o valor do coeficiente a: "))
        self.b = int(input("Insira o valor do coeficiente b: "))
        self.c = int(input("Insira o valor do coeficiente c: "))
        self.delta: float = 0.0
        self.solution_type: int = 0
        self.roots: list = []
        self.vertice: tuple = ()

class Delta(ABC):
    @abstractmethod
    def delta (self, equation: type[Quadratic_Equation_Elements]) -> float:
        pass
    
class Roots(ABC):
    @abstractmethod
    def roots(self, equation: type[Quadratic_Equation_Elements]) -> float:
        pass
class Check_Roots_Type(ABC):
    @abstractmethod
    def check_roots_type (self, equation: type[Quadratic_Equation_Elements]) -> int:
        pass
class Vertice_Coordinates(ABC):
    @abstractmethod
    def x_vertice_coordinate (self, equation: type[Quadratic_Equation_Elements]) -> float:
        pass
    
    @abstractmethod
    def y_vertice_coordinante (self, equation: type[Quadratic_Equation_Elements]) -> float:
        pass
    
class Quadratic_Equation(Quadratic_Equation_Elements):
    def __init__(self):
        super().__init__()
        
    def get_A(self):
        return self.a
    
    def get_B(self):
        return self.b
    
    def get_C(self):
        return self.c
    
    def get_delta(self):
        return self.delta
    
    def get_roots(self):
        return self.roots
    
    def get_vertice(self):
        return self.vertice
    
    def get_solution_type(self):
        return self.solution_type
    
    def set_delta(self, delta) -> None:
        self.delta = delta
    
    def set_solution_type(self, solution_type: int) -> None:
        self.solution_type = solution_type
    
    def set_roots(self, roots: list) -> None:
        self.roots = roots
    
    def set_vertice(self, vertice: tuple) -> None:
        self.vertice = vertice

class Vertice(Vertice_Coordinates):
    def x_vertice_coordinate(self, equation: type[Quadratic_Equation]) -> float:
        a = equation.get_A()
        b = equation.get_B()
        
        return -b/(2 * a)
    
    def y_vertice_coordinante(self, equation: type[Quadratic_Equation]) -> float:
        delta = equation.get_delta()
        a = equation.get_A()
        
        return -delta/(4 * a)
    
    def vertice_coordinate(self, equation: type[Quadratic_Equation]) -> tuple:
        return(self.x_vertice_coordinate(equation), self.y_vertice_coordinante(equation))

class Check_Roots(Check_Roots_Type):
    def check_roots_type(self, equation: type[Quadratic_Equation]) -> int:
        delta = equation.get_delta()
        
        if delta > 0:
            return 2
        elif delta < 0:
            return 1
        else:
            return 0
            
class Eval_Roots(Roots):
    def roots(self, equation: type[Quadratic_Equation]) -> tuple:
        a = equation.get_A()
        b = equation.get_B()
        delta = equation.get_delta()
        solution_type = equation.get_solution_type()
        
        match(solution_type):
            case 2:
                return (
                    (-b + math.sqrt(delta))/(2 * a),
                    (-b - math.sqrt(delta))/(2 * a)
                        )
            case 1:
                return (
                    (-b + cmath.sqrt(delta)/(2 * a)),
                    (-b + cmath.sqrt(delta)/(2 * a))  
                )
            case 0:
                return (
                    -b / (2 * a)
                )
                
class Eval_Delta(Delta):
    def delta(self, equation: type[Quadratic_Equation]) -> float:
        a = equation.get_A()
        b = equation.get_B()
        c = equation.get_C()
        
        return (b ** 2) + (-4 * a * c)

class Display():
    def __init__(self, equation: type[Quadratic_Equation]):
        self.equation = equation
    
    def print_results(self):
        print(f"\nAs raízes são: {self.equation.get_roots()}")
        print(f"O valor do discriminante é: {self.equation.get_delta()}")
        print(f"O vértice da parábola é: {self.equation.get_vertice()}")

vertice_solver = Vertice()
delta_solver = Eval_Delta()
solution_checker = Check_Roots()
root_solver = Eval_Roots()
quadratic_equation = Quadratic_Equation()

quadratic_equation.set_delta(delta_solver.delta(quadratic_equation))
quadratic_equation.set_solution_type(solution_checker.check_roots_type(quadratic_equation))
quadratic_equation.set_roots(root_solver.roots(quadratic_equation))
quadratic_equation.set_vertice(vertice_solver.vertice_coordinate(quadratic_equation))

display = Display(quadratic_equation)
display.print_results()
