import inspect
import os
import argparse
import importlib.util

TESTS_DIR = os.path.join(os.path.dirname(__file__), "tests")


def load_module(module_name: str, file_path: str):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def discover_tests():
    test_entries = []

    for file_name in sorted(os.listdir(TESTS_DIR)):
        if not file_name.endswith(".py") or not file_name.startswith("test_"):
            continue

        file_path = os.path.join(TESTS_DIR, file_name)
        module_name = f"tests.{os.path.splitext(file_name)[0]}"
        module = load_module(module_name, file_path)
        test_functions = [
            (name, func)
            for name, func in inspect.getmembers(module, inspect.isfunction)
            if name.startswith("test_") and func.__module__ == module.__name__
        ]

        if len(test_functions) != 1:
            raise ValueError(f"{file_name} must contain exactly one test function")

        test_entries.append(test_functions[0])

    return test_entries

def main(fptr: str):
    # get file name
    module_name = os.path.splitext(os.path.basename(fptr))[0]
    user_module = load_module(module_name, fptr)

    if hasattr(user_module, 'MaxHeap'):
        tests = discover_tests()
        total_tests = len(tests)

        for index, (test_name, test_func) in enumerate(tests, start=1):
            try:
                test_func(user_module.MaxHeap)
                result = "Pass"
            except Exception:
                result = "Fail"

            print(f"{index}/{total_tests} {result} - {test_name}")

    else:
        print(f"Error: Could not find 'MaxHeap' in {fptr}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Engine to test your max-heap")
    parser.add_argument("filename", help="path to your .py file")
    args = parser.parse_args()

    main(args.filename)
