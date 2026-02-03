"""
Comparative Analysis of Sorting Algorithms
A console-based multi-algorithm benchmarking tool
"""

import sys
import time
import random
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, is_sorted


class SortingBenchmark:
    """
    Main application class for benchmarking and comparing sorting algorithms.
    Provides a professional CLI interface for sorting analysis.
    """
    
    def __init__(self):
        """Initialize the benchmarking application."""
        self.algorithms = {
            '1': {'name': 'Bubble Sort', 'func': bubble_sort, 'complexity': 'O(n²)'},
            '2': {'name': 'Insertion Sort', 'func': insertion_sort, 'complexity': 'O(n²)'},
            '3': {'name': 'Merge Sort', 'func': merge_sort, 'complexity': 'O(n log n)'},
        }
        self.data = None
        self.dataset_size = 0
    
    def clear_screen(self):
        """Clear the console screen in a cross-platform way."""
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()
    
    def print_header(self, title):
        """
        Print a formatted header for the application.
        
        Args:
            title: The header title text
        """
        width = 70
        print("\n" + "=" * width)
        print(f" {title.center(width - 2)}")
        print("=" * width + "\n")
    
    def print_separator(self):
        """Print a visual separator line."""
        print("-" * 70)
    
    def print_menu(self):
        """Display the main algorithm selection menu."""
        self.print_header("Sorting Algorithm Benchmarking Tool")
        print("Select an algorithm to benchmark:")
        print("\n  [1] Bubble Sort      (O(n²) - Exchange Sort)")
        print("  [2] Insertion Sort   (O(n²) - Comparison Sort)")
        print("  [3] Merge Sort       (O(n log n) - Divide and Conquer)")
        print("  [4] Run All Algorithms (Side-by-side Comparison)")
        print("  [5] Exit Program")
        print()
    
    def get_algorithm_choice(self):
        """
        Get user's algorithm selection.
        
        Returns:
            The user's choice as a string
        """
        while True:
            choice = input("Enter your choice [1-5]: ").strip()
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            print("Invalid input. Please enter a number between 1 and 5.\n")
    
    def get_dataset_size(self):
        """
        Get the desired dataset size from the user.
        
        Returns:
            The dataset size as an integer
        """
        while True:
            try:
                size = int(input("\nEnter the dataset size (e.g., 1000, 10000, 50000): "))
                if size <= 0:
                    print("Please enter a positive number.")
                    continue
                if size > 100000:
                    confirm = input(f"Warning: {size:,} elements may take a long time. Continue? (y/n): ").lower()
                    if confirm == 'y':
                        return size
                else:
                    return size
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
    def generate_random_data(self, size):
        """
        Generate random data for sorting (not timed).
        
        Args:
            size: Number of elements to generate
        
        Returns:
            List of random integers
        """
        return [random.randint(1, 100000) for _ in range(size)]
    
    def run_algorithm(self, algorithm_key):
        """
        Run a single algorithm with timing.
        
        Args:
            algorithm_key: The key for the algorithm to run
        
        Returns:
            Dictionary with timing and verification results
        """
        algo_info = self.algorithms[algorithm_key]
        name = algo_info['name']
        func = algo_info['func']
        
        # Create a copy for sorting (don't time data generation)
        test_data = self.data.copy()
        
        # Time only the sorting process
        start_time = time.perf_counter()
        sorted_data = func(test_data)
        end_time = time.perf_counter()
        
        elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
        is_valid = is_sorted(sorted_data)
        
        return {
            'name': name,
            'complexity': algo_info['complexity'],
            'time': elapsed_time,
            'valid': is_valid
        }
    
    def display_results(self, result):
        """
        Display results for a single algorithm run.
        
        Args:
            result: Dictionary containing the algorithm results
        """
        print(f"\nAlgorithm: {result['name']}")
        print(f"Time Complexity: {result['complexity']}")
        self.print_separator()
        print(f"Dataset Size:    {self.dataset_size:,} elements")
        print(f"Execution Time:  {result['time']:.4f} milliseconds")
        print(f"Verification:    {'✓ PASSED - Array is sorted' if result['valid'] else '✗ FAILED - Array is NOT sorted'}")
    
    def display_comparison_results(self, results):
        """
        Display side-by-side comparison of all algorithms.
        
        Args:
            results: List of result dictionaries from all algorithms
        """
        self.print_header("Side-by-Side Algorithm Comparison")
        print(f"Dataset Size: {self.dataset_size:,} elements\n")
        
        # Display results in table format
        print(f"{'Algorithm':<20} {'Complexity':<15} {'Time (ms)':<15} {'Status':<12}")
        self.print_separator()
        
        for result in results:
            status = "✓ PASSED" if result['valid'] else "✗ FAILED"
            print(f"{result['name']:<20} {result['complexity']:<15} {result['time']:>10.4f}      {status:<12}")
        
        # Find and display the fastest algorithm
        fastest = min(results, key=lambda x: x['time'])
        slowest = max(results, key=lambda x: x['time'])
        
        print()
        self.print_separator()
        print(f"\n⚡ Fastest:  {fastest['name']} ({fastest['time']:.4f} ms)")
        print(f"🐢 Slowest:  {slowest['name']} ({slowest['time']:.4f} ms)")
        
        # Calculate performance ratio
        if slowest['time'] > 0:
            ratio = slowest['time'] / fastest['time']
            print(f"📊 Performance Ratio: {ratio:.2f}x faster (fastest vs slowest)")
        
        print()
    
    def analysis_insights(self, results):
        """
        Provide algorithmic insights based on results.
        
        Args:
            results: List of result dictionaries from all algorithms
        """
        self.print_header("Algorithmic Analysis & Insights")
        
        print("About the Algorithms Tested:\n")
        
        print("• BUBBLE SORT (O(n²))")
        print("  An exchange sort that repeatedly steps through the list and swaps")
        print("  adjacent elements if they're in the wrong order. Very inefficient for")
        print("  large datasets but easy to understand.\n")
        
        print("• INSERTION SORT (O(n²))")
        print("  A comparison sort that builds the final sorted array one item at a time.")
        print("  Slightly more efficient than bubble sort in practice, especially for")
        print("  small or partially sorted datasets.\n")
        
        print("• MERGE SORT (O(n log n))")
        print("  A divide-and-conquer algorithm that divides the array into halves,")
        print("  recursively sorts them, and merges the results. Much faster for large")
        print("  datasets despite the overhead of creating new arrays.\n")
        
        # Show performance characteristics
        o_n_squared = [r for r in results if 'O(n²)' in r['complexity']]
        o_n_log_n = [r for r in results if 'O(n log n)' in r['complexity']]
        
        if o_n_squared and o_n_log_n:
            avg_quadratic = sum(r['time'] for r in o_n_squared) / len(o_n_squared)
            avg_loglinear = sum(r['time'] for r in o_n_log_n) / len(o_n_log_n)
            
            if avg_loglinear > 0:
                performance_gap = avg_quadratic / avg_loglinear
                print(f"At {self.dataset_size:,} elements:")
                print(f"  → O(n²) algorithms averaged {avg_quadratic:.4f} ms")
                print(f"  → O(n log n) algorithms averaged {avg_loglinear:.4f} ms")
                print(f"  → Performance gap: {performance_gap:.2f}x difference\n")
                
                if performance_gap > 10:
                    print("💡 The divide-and-conquer approach is SIGNIFICANTLY faster!")
                    print("   This gap grows exponentially as dataset size increases.")
    
    def run_single_algorithm(self):
        """Run and display results for a single algorithm."""
        self.print_header("Single Algorithm Benchmark")
        
        self.dataset_size = self.get_dataset_size()
        self.data = self.generate_random_data(self.dataset_size)
        
        print("\nGenerating random dataset...")
        print(f"Dataset: {self.dataset_size:,} random integers ready\n")
        
        print("Running algorithm...")
        choice = self.get_algorithm_choice()
        
        if choice in self.algorithms:
            result = self.run_algorithm(choice)
            self.clear_screen()
            self.display_results(result)
    
    def run_all_algorithms(self):
        """Run all algorithms and display comparison."""
        self.print_header("All Algorithms Comparison")
        
        self.dataset_size = self.get_dataset_size()
        self.data = self.generate_random_data(self.dataset_size)
        
        print("\nGenerating random dataset...")
        print(f"Dataset: {self.dataset_size:,} random integers ready\n")
        
        print("Running all algorithms...\n")
        results = []
        
        for key in ['1', '2', '3']:
            algo_name = self.algorithms[key]['name']
            print(f"  Running {algo_name}...", end='', flush=True)
            result = self.run_algorithm(key)
            results.append(result)
            print(" ✓")
        
        self.clear_screen()
        self.display_comparison_results(results)
        self.analysis_insights(results)
    
    def run(self):
        """Main application loop."""
        while True:
            self.print_menu()
            choice = self.get_algorithm_choice()
            
            if choice == '1' or choice == '2' or choice == '3':
                self.clear_screen()
                self.run_single_algorithm()
            elif choice == '4':
                self.clear_screen()
                self.run_all_algorithms()
            elif choice == '5':
                self.clear_screen()
                print("\nThank you for using the Sorting Algorithm Benchmarking Tool!")
                print("Goodbye!\n")
                sys.exit(0)
            
            input("\nPress Enter to return to the main menu...")
            self.clear_screen()


def main():
    """Entry point for the application."""
    try:
        app = SortingBenchmark()
        app.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
