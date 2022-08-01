命名屏蔽规则


## 类屏蔽规则

```vk
def field() {
    1
}

class Test {
    field: int = 0
}
extends class {
    def get field(self) {
        2
    }
    def test test_field(self) {
        print(class.field)
        print(namespace::field())
        print(self.field)
    }
}
```



