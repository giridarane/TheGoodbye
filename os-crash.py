import ctypes
import time

def crash_system():
    # This function will cause a system crash by attempting to access invalid memory
    ptr = ctypes.cast(ctypes.c_void_p(0), ctypes.POINTER(ctypes.c_char))
    ptr.contents.value = b'A'  # Ensure it's a byte string for compatibility

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Crashing in {i} seconds... Press Ctrl+C to abort.", end='\r')
        time.sleep(1)
    print("\n")

if __name__ == "__main__":
    while True:
        print("This tool will crash your system. Choose an option:")
        print("1. Proceed to crash the system")
        print("2. Restart the countdown")
        print("3. Abort operation")
        
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            countdown(10)
            crash_system()
        elif choice == "2":
            print("Restarting the countdown...")
            countdown(10)
        elif choice == "3":
            print("Operation aborted.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
