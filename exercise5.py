def main() -> None:
    tax = tax_payable(6000, 3500, 0.1, 105)
    print("应缴税额:", tax)

def tax_payable(salary: float, tax_hreshold: float, tax_rate: float, quick_deduction: float) -> float:
    return (salary - tax_hreshold) * tax_rate - quick_deduction

if __name__ == "__main__":
    main()