use nyar_valkyrie::get_ast;
use nyar_python::ToPython;

#[test]
fn debug_numbers() {
    let ast = get_ast(include_str!("debug_numbers.nyar"));
    ast.clone().save("./tests/debug_number/debug_numbers.json");
    ast.save_python("./tests/debug_number/debug_numbers.py");
}

#[test]
fn debug_bytes() {
    let ast = get_ast(include_str!("debug_bytes.nyar"));
    ast.clone().save("./tests/debug_number/debug_bytes.json");
    ast.save_python("./tests/debug_number/debug_bytes.ugt");
}
