use nyar_python::ToPython;
use nyar_valkyrie::get_ast;

#[test]
fn debug_expr() {
    let ast = get_ast(include_str!("if_basic.nyar"));
    ast.clone().save("./tests/debug_if/if_basic.json");
    ast.save_python("./tests/debug_if/if_basic.py");
}
