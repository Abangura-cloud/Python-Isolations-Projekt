import sys
import importlib.util

def check_interpreter():
    print("Current Python Interpreter Path:")
    print(sys.executable)

def check_requests_package():
    spec = importlib.util.find_spec("requests")
    if spec is not None:
        print("Package 'requests': INSTALLED")
    else:
        print("Package 'requests': NOT FOUND")

if __name__ == "__main__":
    print("=" * 50)
    check_interpreter()
    check_requests_package()
    print("=" * 50)
    
