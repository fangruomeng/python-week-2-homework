from math import cos, sin

def main() -> None:
    result = which_is_bigger()
    print("最大的是:", result)

def which_is_bigger() -> str:
    return "COS(365)" if cos(365) >= sin(365)  else "SIN(365)"

if __name__ == "__main__":
    main()