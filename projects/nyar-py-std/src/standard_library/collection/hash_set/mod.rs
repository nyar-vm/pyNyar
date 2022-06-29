pub(crate) use _hash_map::make_module;
use std::collections::HashMap;
use rustpython_vm::PyObjectRef;

#[pymodule]
mod _hash_map {
    use super::*;

    #[pyattr]
    #[pyclass(name = "HashSet")]
    #[derive(Debug, Default, PyPayload)]
    struct VkHashSet {
        inner: HashMap<PyObjectRef, PyObjectRef>,
    }
}
