from setuptools import setup
import sys

try:
    from setuptools_rust import RustExtension, Binding
except ImportError:
    import subprocess

    errno = subprocess.call([sys.executable, "-m", "pip", "install", "setuptools-rust"])
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)
    else:
        from setuptools_rust import RustExtension, Binding

setup(
    name="rust-python-ctypes",
    description='Example project to extend python with rust and ctypes',
    install_requires=['setuptools-rust'],
    version="0.1.0",
    rust_extensions=[RustExtension("rust_python_ctypes.librust_python_ctypes", binding=Binding.NoBinding)],
    packages=["rust_python_ctypes"],
    zip_safe=False,
)
