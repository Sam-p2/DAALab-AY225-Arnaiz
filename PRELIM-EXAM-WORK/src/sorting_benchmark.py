import csv
import time
import os
import sys

# --- CORE ALGORITHMS (Built from scratch) ---
class Sorters:
    @staticmethod
    def bubble_sort(data, key):
        n = len(data)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if getattr(data[j], key) > getattr(data[j + 1], key):
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped: break
        return data

    @staticmethod
    def insertion_sort(data, key):
        for i in range(1, len(data)):
            current = data[i]
            pos = i
            while pos > 0 and getattr(data[pos - 1], key) > getattr(current, key):
                data[pos] = data[pos - 1]
                pos -= 1
            data[pos] = current
        return data

    @staticmethod
    def merge_sort(data, key):
        if len(data) <= 1: return data
        mid = len(data) // 2
        left = Sorters.merge_sort(data[:mid], key)
        right = Sorters.merge_sort(data[mid:], key)
        return Sorters._merge(left, right, key)

    @staticmethod
    def _merge(left, right, key):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if getattr(left[i], key) <= getattr(right[j], key):
                res.append(left[i]); i += 1
            else:
                res.append(right[j]); j += 1
        res.extend(left[i:]); res.extend(right[j:])
        return res

# --- DATA STRUCTURE ---
class Record:
    def __init__(self, id_val, first_name, last_name):
        self.id = int(id_val)
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.id:<10} | {self.first_name:<15} | {self.last_name:<15}"

# --- UI/UX FUNCTIONS ---
def display_menu():
    """Display the main menu with options"""
    print("\n" + "="*60)
    print("SORTING ALGORITHM BENCHMARK TOOL")
    print("="*60)
    print("1. Run Custom Test (Choose parameters)")
    print("2. Run Full Benchmark (For README table)")
    print("3. Exit")
    print("="*60)

def get_user_choice():
    """Get and validate user menu choice"""
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice in ['1', '2', '3']:
                return int(choice)
            else:
                print("Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            sys.exit(0)

def get_sorting_parameters():
    """Get user input for sorting parameters"""
    print("\n" + "-"*60)
    print("SORTING PARAMETERS")
    print("-"*60)
    
    # Get algorithm choice
    print("\nChoose sorting algorithm:")
    print("1. Bubble Sort (O(n²))")
    print("2. Insertion Sort (O(n²))")
    print("3. Merge Sort (O(n log n))")
    
    algorithms = {
        1: ("Bubble Sort", Sorters.bubble_sort),
        2: ("Insertion Sort", Sorters.insertion_sort),
        3: ("Merge Sort", Sorters.merge_sort)
    }
    
    while True:
        try:
            algo_choice = input("\nEnter algorithm choice (1-3): ").strip()
            if algo_choice in ['1', '2', '3']:
                algo_choice = int(algo_choice)
                algo_name, algo_func = algorithms[algo_choice]
                break
            else:
                print("Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            return None, None, None, None, None
    
    # Get column choice
    print("\nChoose column to sort by:")
    print("1. ID (Integer)")
    print("2. First Name (String)")
    print("3. Last Name (String)")
    
    columns = {1: "id", 2: "first_name", 3: "last_name"}
    column_names = {1: "ID", 2: "First Name", 3: "Last Name"}
    
    while True:
        try:
            col_choice = input("\nEnter column choice (1-3): ").strip()
            if col_choice in ['1', '2', '3']:
                col_choice = int(col_choice)
                key = columns[col_choice]
                col_name = column_names[col_choice]
                break
            else:
                print("Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            return None, None, None, None, None
    
    # Get number of rows
    print("\n" + "-"*60)
    print("DATASIZE SELECTION")
    print("Maximum available: 100,000 records")
    print("-"*60)
    
    while True:
        try:
            n_input = input(f"\nEnter number of rows to sort (1-100000): ").strip()
            n = int(n_input)
            if 1 <= n <= 100000:
                break
            else:
                print("Please enter a number between 1 and 100,000.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            return None, None, None, None, None
    
    # Warn about O(n²) algorithms for large datasets
    if algo_name in ["Bubble Sort", "Insertion Sort"] and n > 10000:
        print("\n" + "!"*60)
        print(f"WARNING: {algo_name} is O(n²). Sorting {n:,} rows may take a long time!")
        print("Consider using Merge Sort (O(n log n)) for better performance.")
        print("!"*60)
        
        confirm = input("\nDo you want to continue? (y/n): ").lower()
        if confirm != 'y':
            print("Operation cancelled.")
            return None, None, None, None, None
    
    return algo_name, algo_func, key, col_name, n

def load_data(n=None):
    """Load data from CSV file"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to project root, then into data folder
    project_root = os.path.dirname(script_dir)
    csv_path = os.path.join(project_root, 'data', 'generated_data.csv')
    
    # Alternative: Look for file in multiple possible locations
    possible_paths = [
        csv_path,
        os.path.join('data', 'generated_data.csv'),
        os.path.join('..', 'data', 'generated_data.csv'),
        'generated_data.csv'
    ]
    
    actual_path = None
    for path in possible_paths:
        if os.path.exists(path):
            actual_path = path
            break
    
    if actual_path is None:
        # Try to find any CSV file in the data folder
        data_dir = os.path.join(project_root, 'data')
        if os.path.exists(data_dir):
            csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
            if csv_files:
                actual_path = os.path.join(data_dir, csv_files[0])
                print(f"Found CSV file: {csv_files[0]}")
    
    if actual_path is None:
        print(f"\nERROR: Could not find generated_data.csv")
        print(f"Please ensure your project structure is:")
        print("Project Folder/")
        print("  ├── data/")
        print("  │     └── generated_data.csv")
        print("  └── src/")
        print("        └── sorting_benchmark.py")
        print(f"\nCurrent working directory: {os.getcwd()}")
        print(f"Script location: {script_dir}")
        return None, 0
    
    print(f"\nLoading data from: {actual_path}")
    
    records = []
    try:
        start_load = time.perf_counter()
        with open(actual_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if n is not None and i >= n:
                    break
                records.append(Record(row['ID'], row['FirstName'], row['LastName']))
        load_time = time.perf_counter() - start_load
        
        print(f"✓ Successfully loaded {len(records):,} records")
        print(f"⏱️  File loading time: {load_time:.4f} seconds")
        
        return records, load_time
        
    except FileNotFoundError:
        print(f"✗ Error: File not found at {actual_path}")
        return None, 0
    except KeyError as e:
        print(f"✗ Error: Missing expected column in CSV: {e}")
        print("Expected columns: ID, FirstName, LastName")
        return None, 0
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return None, 0

def run_custom_test():
    """Run a single sorting test with user parameters"""
    # Get parameters from user
    result = get_sorting_parameters()
    if result[0] is None:  # User cancelled
        return
    
    algo_name, algo_func, key, col_name, n = result
    
    # Load data
    print(f"\n{'='*60}")
    print(f"LOADING DATA")
    print(f"{'='*60}")
    
    records, load_time = load_data(n)
    if records is None:
        return
    
    # Display warning for O(n²) algorithms
    if algo_name in ["Bubble Sort", "Insertion Sort"] and n > 10000:
        print(f"\n{'!'*60}")
        print(f"PERFORMANCE WARNING: {algo_name} is O(n²)")
        print(f"Sorting {n:,} rows may take significant time...")
        print("Press Ctrl+C to cancel if it takes too long.")
        print(f"{'!'*60}")
    
    # Perform sorting
    print(f"\n{'='*60}")
    print(f"SORTING EXECUTION")
    print(f"{'='*60}")
    print(f"Algorithm: {algo_name}")
    print(f"Sorting by: {col_name}")
    print(f"Dataset size: {n:,} records")
    print(f"{'='*60}")
    
    try:
        start_sort = time.perf_counter()
        
        if algo_name == "Merge Sort":
            # Merge sort returns a new list
            sorted_data = algo_func(records, key)
        else:
            # Bubble/Insertion sort in-place
            data_copy = records.copy()
            sorted_data = algo_func(data_copy, key)
        
        sort_time = time.perf_counter() - start_sort
        
        # Display results
        print(f"\n{'='*60}")
        print(f"RESULTS")
        print(f"{'='*60}")
        print(f"✅ Sorting completed successfully!")
        print(f"⏱️  Sorting execution time: {sort_time:.4f} seconds")
        print(f"⏱️  Total time (load + sort): {load_time + sort_time:.4f} seconds")
        
        # Display first 10 records
        print(f"\n{'='*60}")
        print(f"FIRST 10 SORTED RECORDS")
        print(f"{'='*60}")
        print(f"{'ID':<10} | {'First Name':<15} | {'Last Name':<15}")
        print(f"{'-'*45}")
        
        for i in range(min(10, len(sorted_data))):
            print(sorted_data[i])
        
        if len(sorted_data) > 10:
            print(f"... and {len(sorted_data) - 10:,} more records")
        
        print(f"\n{'='*60}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Sorting interrupted by user.")
        print("The operation was cancelled.")
    except Exception as e:
        print(f"\n❌ Error during sorting: {e}")

def run_full_benchmark():
    """Run the full benchmark for README table"""
    print("\n" + "="*60)
    print("RUNNING FULL BENCHMARK (For README)")
    print("="*60)
    print("This will test all algorithms on 1k, 10k, and 100k records.")
    print("Results will be displayed in a formatted table.")
    print("="*60)
    
    # Load all data first
    print("\nLoading full dataset...")
    all_records, load_time = load_data()
    if all_records is None:
        return
    
    # Scalability Test parameters
    test_scales = [1000, 10000, 100000]
    results = []
    
    print("\nBenchmark in progress...")
    print("(This may take several minutes for O(n²) algorithms)")
    print("Press Ctrl+C to cancel at any time.")
    
    for name, func in [("Bubble Sort", Sorters.bubble_sort), 
                       ("Insertion Sort", Sorters.insertion_sort), 
                       ("Merge Sort", Sorters.merge_sort)]:
        times = [name]
        
        for n in test_scales:
            subset = all_records[:n].copy()  # Copy to avoid modifying original
            
            # O(n^2) Warning: Skip 100k for Bubble/Insertion to prevent freezing
            if name != "Merge Sort" and n == 100000:
                times.append("Too Slow")
                print(f"  ⚠ Skipping {name} at N=100,000 (O(n²) would take too long)")
                continue
                
            print(f"  Running {name} on N={n:,}...", end="", flush=True)
            try:
                start = time.perf_counter()
                
                if name == "Merge Sort":
                    func(subset, "id")
                else:
                    func(subset, "id")
                    
                elapsed = time.perf_counter() - start
                times.append(f"{elapsed:.4f}s")
                print(f" completed in {elapsed:.2f} seconds")
                
            except KeyboardInterrupt:
                print(f"\n\n⚠️  Benchmark interrupted by user.")
                print("Partial results will be displayed.")
                times.append("Interrupted")
                break
            except Exception as e:
                print(f" error: {e}")
                times.append("Error")
        
        results.append(times)
    
    # Print results table for README 
    print("\n" + "="*80)
    print("BENCHMARK RESULTS TABLE (Sorting by ID)")
    print("="*80)
    print(f"{'Algorithm':<15} | {'N=1,000':<12} | {'N=10,000':<12} | {'N=100,000':<12}")
    print("-" * 80)
    for r in results:
        print(f"{r[0]:<15} | {r[1]:<12} | {r[2]:<12} | {r[3]:<12}")
    
    print("\n" + "="*80)
    print("ANALYSIS:")
    print("-" * 80)
    print("• Merge Sort (O(n log n)) scales efficiently with large datasets")
    print("• Bubble/Insertion Sort (O(n²)) become impractical beyond 10,000 records")
    print("• The 100x increase from 1k to 100k shows exponential time growth for O(n²)")
    print("="*80)
    
    # Ask if user wants to save to file
    try:
        save = input("\nSave results to benchmark_results.txt? (y/n): ").lower()
        if save == 'y':
            with open('benchmark_results.txt', 'w', encoding='utf-8') as f:
                f.write("SORTING ALGORITHM BENCHMARK RESULTS\n")
                f.write("="*60 + "\n\n")
                f.write(f"{'Algorithm':<15} | {'N=1,000':<12} | {'N=10,000':<12} | {'N=100,000':<12}\n")
                f.write("-"*60 + "\n")
                for r in results:
                    f.write(f"{r[0]:<15} | {r[1]:<12} | {r[2]:<12} | {r[3]:<12}\n")
            print("✓ Results saved to benchmark_results.txt")
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")

def main():
    """Main program loop"""
    print("Initializing Sorting Benchmark Tool...")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            run_custom_test()
        elif choice == 2:
            run_full_benchmark()
        elif choice == 3:
            print("\nThank you for using the Sorting Algorithm Benchmark Tool!")
            print("Goodbye!")
            break
        
        if choice != 3:
            try:
                input("\nPress Enter to continue...")
            except KeyboardInterrupt:
                print("\n\nReturning to main menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        print("Please check your setup and try again.")