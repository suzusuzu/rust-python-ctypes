# rust-python-ctypes
Example project to extend python with rust and ctypes

## install
```sh
pip install .
```

## Usage
```sh
python
>>> import rust_python_ctypes
>>> rust_python_ctypes.hello_rust()
hello rust
```

## Rust
`Cargo.toml`
```toml
[package]
name = "rust-python-ctypes"
version = "0.1.0"
authors = ["suzusuzu <s.suzugamine@gmail.com>"]
edition = "2018"

[lib]
crate-type = ["cdylib"]
```

`src/lib.rs`
```rust
#[no_mangle]
pub extern "C" fn hello_rust(){
    println!("hello rust");
}
```

## Python
`rust_python_ctypes/__init__.py`
```python
hello_rust_ = cdll.LoadLibrary(lib_path).hello_rust

def hello_rust():
    hello_rust_()
```
