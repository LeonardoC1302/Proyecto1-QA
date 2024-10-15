import threading
import subprocess
import sys

def run_file(file_path):
    # Print the file being run
    print(f"Running file: {file_path}")
    # Use subprocess to run the file as a separate process
    subprocess.run([sys.executable, file_path])

def run_concurrent_files(num_threads, file_to_run):
    threads = []
    # Create the desired number of threads
    for i in range(num_threads):
        thread = threading.Thread(target=run_file, args=(file_to_run,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <num_threads> <file_to_run>")
        sys.exit(1)

    num_threads = int(sys.argv[1])
    file_to_run = sys.argv[2]

    print(f"Number of threads: {num_threads}")
    print(f"File to run: {file_to_run}")
    run_concurrent_files(num_threads, file_to_run)
