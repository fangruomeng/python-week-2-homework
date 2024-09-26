from enum import Enum

def main() -> None:
    amount_of_dollar = exchange(10000, ExchangeRate.Dollar)
    amount_of_gbp = exchange(10000, ExchangeRate.GBP)
    amount_of_eur = exchange(10000, ExchangeRate.EUR)
    amount_of_aud = exchange(10000, ExchangeRate.AUD)
    print("换算美元:", amount_of_dollar, "\n")
    print("换算英镑:", amount_of_gbp, "\n")
    print("换算欧元:", amount_of_eur, "\n")
    print("换算澳元:", amount_of_aud, "\n")
    
class ExchangeRate(Enum):
    Dollar = 7.00
    GBP = 8.55
    EUR = 7.78
    AUD = 4.24

def exchange(amount: float, foreign_exchange: ExchangeRate):
    return round(amount / foreign_exchange.value, 2)

if __name__ == "__main__":
    main()