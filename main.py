import argparse
from utils import load_algorithm, get_available_algorithms

# def display_help():
#     available_algorithms = get_available_algorithms()
#     print("\nAvailable Categories and Algorithms:\n")
#     for category, algorithms in available_algorithms.items():
#         print(f"{category.capitalize()}:")
#         for algo in algorithms:
#             print(f"  - {algo}")
#     print("\nExample usage:")
#     print("  python main.py --category searching --algorithm depth_first --params \"{1: [2, 3], 2: [4], 3: [4], 4: []}\" 1\n")

def display_help():
    """Display available categories and algorithms."""
    available_algorithms = get_available_algorithms()
    print("\nAvailable Categories and Algorithms:\n")
    for category, algorithms in available_algorithms.items():
        print(f"{category.capitalize()}:")
        for algo, (module, class_name) in algorithms.items():
            print(f"  - {algo} (module: {module}, class: {class_name})")
    print("\nExample usage:")
    print("  python main.py --category searching --algorithm depth_first --params \"{1: [2, 3], 2: [4], 3: [4], 4: []}\" 1\n")

def main():
    parser = argparse.ArgumentParser(description="Algorithm Runner")
    parser.add_argument("--category", help="Category of the algorithm (e.g., basic, searching).")
    parser.add_argument("--algorithm", help="Algorithm name (e.g., depth_first, binary).")
    parser.add_argument("--params", nargs="*", help="Parameters required by the algorithm.")
    
    args = parser.parse_args()

    if not args.category or not args.algorithm:
        print("\nNo category or algorithm provided. Showing help:\n")
        display_help()
        return
    
    try:
        algo_instance = load_algorithm(args.category, args.algorithm)
        if args.params:
            result = algo_instance.run(*args.params)
            print(f"\nAlgorithm Result:\n{result}")
        else:
            print("\nNo parameters provided. This algorithm may require additional inputs.\n")
    except ValueError as e:
        print(f"\nError: {e}\n")
        display_help()

if __name__== "__main__":
    main()