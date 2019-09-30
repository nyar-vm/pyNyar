use nyar_valkyrie::get_ast;
use nyar_python::ToPython;

#[test]
fn debug_expr() {
    let ast = get_ast(include_str!("basic_expr.nyar"));
    ast.clone().save("./tests/debug_expr/basic_expr.json");
    ast.save_python("./tests/debug_expr/basic_expr.py");
}

const PARENTHESES: &str = r#"
(1 + 1)
a(1 + 1)
"#;

#[test]
fn debug_expr_parentheses() {
    let ast = get_ast(PARENTHESES);
    ast.save("tests/debug_expr_parentheses.json");
    assert_eq!(0, 1)
}

const BRACKETS: &str = r#"
[1 + 1]
a[1 + 1]
a[1 + 1] + 1
"#;

#[test]
fn debug_expr_brackets() {
    let ast = get_ast(BRACKETS);
    ast.save("tests/debug_expr_brackets.json");
    assert_eq!(0, 1)
}
