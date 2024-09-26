from math import sqrt

def main() -> None:
    (result1, result2) = solving_equations(-8, -2, 1)
    print("计算结果: ", "\n")
    print("x1:", result1, "\n")
    print("x2:", result2, "\n")
    
def solving_equations(constant_term: float, linear_term: float, squared_term: float) -> tuple[float, float]:
    return (
        (-linear_term + sqrt(linear_term**2 - squared_term * constant_term * 4)) / (squared_term * 2), 
        (-linear_term - sqrt(linear_term**2 - squared_term * constant_term * 4)) / (squared_term * 2)
    )

if __name__ == "__main__":
    main()