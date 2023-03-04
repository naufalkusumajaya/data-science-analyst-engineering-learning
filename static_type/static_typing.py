from typing import List, Dict, Set, Optional, Any, Sequence, Tuple, Callable

x: list = []

y: List[List[int]] = [[1,2,3],[4,5,6]]

a: Dict[str, str] = {"a":"b"}

b: Set[str] = {"a","b"}


def sum3num(a:int, b:int, c:int) -> int:
    return a + b + c

def sum3num2(a:int, b:int, c:int) -> None:
    print(a + b + c)
    
## Custom Type

Vector = List[float]

def huu(v:Vector) -> Vector:
    return v

def typing_optional(x: Optional[bool] = False):
    pass

def typing_any(x: Any):
    pass

def typing_sequence(seq: Sequence[str]):
    # true untuk semua yang bisa diindex dengan angka
    pass

d: tuple = (1,2,'3') # aman

e: Tuple[int,int,str] = (1,2,'3')
# Khusus Tuple kita harus menentukan tipe data setiap elemen


def adding(x:int, y:int) -> str:
    return str(x + y)

def callable_type(func: Callable[[int,int],str], x:int, y:int) -> None:
    # Callable[[int,int],str] artinya 
    # [int,int] -> parameter
    # str -> output
    func(x,y)

callable_type(adding,1,2)