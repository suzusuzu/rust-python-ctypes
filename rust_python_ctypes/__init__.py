from ctypes import *
import os

def find_lib_path():
    current_path = os.path.dirname(os.path.abspath(os.path.expanduser(__file__)))
    lib_files= [f.name for f in os.scandir(current_path) if f.is_file() and 'rust_python_ctypes' in f.name ]
    if not lib_files:
        raise Exception('Cannot find shared library file')
    return os.path.join(current_path, lib_files[0])

lib_path = find_lib_path()
hello_rust_ = cdll.LoadLibrary(lib_path).hello_rust

def hello_rust():
    hello_rust_()
