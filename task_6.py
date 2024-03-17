def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            total_cost += info['cost']
            total_calories += info['calories']
            selected_items.append(item)

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    keys_values = list(items.items())

    n = len(keys_values)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            value = keys_values[i - 1][1]

            if value['cost'] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j], 
                    dp[i - 1][j - value['cost']] + value['calories']
                )

    selected_items = []
    left_cost = budget
    for i in range(n, 0, -1):
        if dp[i][left_cost] != dp[i - 1][left_cost]:
            key = keys_values[i - 1][0]
            selected_items.append(key)
            left_cost -= items[key]['cost']

    total_cost = budget - left_cost

    return selected_items, total_cost, dp[n][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

def main():
    greedy_selected_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
    dynamic_selected_items, dynamic_total_cost, dynamic_total_calories = dynamic_programming(items, budget)
        
    print('\n')
    print(f"{'-'*108}")
    print(f"{'Aлгоритм':^35} | {'Обрані продукти':^40} | {'Загальні витрати':^16} | {'Калорії':^8}")
    print(f"{'-'*108}")
    print(f"{'Жадібний алгоритм':<35} | {str(greedy_selected_items):^40} | {greedy_total_cost:^16} | {greedy_total_calories:^8}")
    print(f"{'Алгоритм динамічного програмування':<35} | {str(dynamic_selected_items):^40} | {dynamic_total_cost:^16} | {dynamic_total_calories:^8}")
    print('\n')

if __name__ == "__main__":
    main()
