import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    results = [0] * 13
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        results[roll1 + roll2] += 1
    return results[2:]

def calculate_probabilities(results, num_rolls):
    probabilities = [count / num_rolls for count in results]
    return probabilities

def plot_probabilities(probabilities):
    plt.bar(range(2, 13), probabilities)
    plt.title('Розподіл ймовірностей кидків кубиків')
    plt.xlabel('Сума кидків')
    plt.ylabel('Вірогідність')
    plt.xticks(range(2, 13))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    num_rolls = 1000000
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
