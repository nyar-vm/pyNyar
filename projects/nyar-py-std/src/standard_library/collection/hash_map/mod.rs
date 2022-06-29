pub(crate) use _hash_map::make_module;
use std::collections::HashMap;
use rustpython_vm::PyObjectRef;

#[pymodule]
mod _hash_map;
