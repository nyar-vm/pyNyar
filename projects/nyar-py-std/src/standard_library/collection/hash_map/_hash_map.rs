use super::*;

#[pyattr]
#[pyclass(name = "HashMap")]
#[derive(Debug, Default, PyPayload)]
struct VkHashMap {
    inner: HashMap<PyObjectRef, PyObjectRef>,
}

impl VkHashMap {
    fn insert(&mut self) -> Option<PyObjectRef> {
        self.inner.insert()
    }
}
