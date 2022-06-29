#![feature(proc_macro_hygiene)]

#[macro_use]
extern crate rustpython_derive;

mod standard_library;

use std::marker::PhantomData;
use rustpython_vm as vm;
use vm::compile::Mode;
use vm::Interpreter;

fn main() -> vm::PyResult<()> {
    let py = Interpreter::without_stdlib(Default::default());
    py.enter(|vm| {
        let scope = vm.new_scope_with_builtins();

        let code_obj = vm
            .compile(include_str!("test.py"), Mode::Exec, "<embedded>".to_owned())
            .map_err(|err| vm.new_syntax_error(&err))?;
        vm.run_code_obj(code_obj, scope)?;
        Ok(())
    })
}
