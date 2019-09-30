use nyar_python::ToPython;
use nyar_valkyrie::get_ast;

#[test]
fn debug_numbers() {
    let ast = get_ast(include_str!("debug_numbers.nyar"));
    ast.clone().save("./tests/debug_literal/debug_numbers.json");
    ast.save_python("./tests/debug_literal/debug_numbers.py");
}

#[test]
fn debug_bytes() {
    let ast = get_ast(include_str!("debug_bytes.nyar"));
    ast.clone().save("./tests/debug_literal/debug_bytes.json");
    ast.save_python("./tests/debug_literal/debug_bytes.py");
}

#[test]
fn debug_strings() {
    let ast = get_ast(include_str!("debug_strings.nyar"));
    ast.clone().save("./tests/debug_literal/debug_strings.json");
    ast.save_python("./tests/debug_literal/debug_strings.py");
}
