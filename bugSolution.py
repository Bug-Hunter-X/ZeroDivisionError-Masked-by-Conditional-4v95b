def function_with_uncommon_error_solution(x):
    try:
        if x == 0:
            return float('inf')  # Handle division by zero by returning infinity
        else:
            return 1 / x
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

result = function_with_uncommon_error_solution(0) 
result2 = function_with_uncommon_error_solution(5)