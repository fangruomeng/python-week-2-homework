def main() -> None:
    score_list = score_list = [51, 71, 76, 81, 46, 67, 58]
    total_result = total(score_list)
    average_score_result = average_score(score_list)
    pass_rate_result = pass_rate(score_list)
    print("分数总和:", total_result, "\n")
    print("平均分:", average_score_result, "\n")
    print("及格率:", pass_rate_result, "\n")

def total(score_list: list[int]) -> int:
    return sum(score_list)

def average_score(score_list: list[int]) -> float:
    return round(float(total(score_list)) / len(score_list), 2)

def pass_rate(score_list: list[int]) -> float:
    count = sum(1 for score in score_list if score > 60)
    return round(float(count) / len(score_list), 2)

if __name__ == "__main__":
    main()