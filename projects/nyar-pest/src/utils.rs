use crate::ToPython;
use nyar_valkyrie::AST;
use std::{
    fs::File,
    io::{Error, Write},
};
use textwrap::indent;

impl ToPython for AST {
    fn to_python(&self) -> String {
        return match self {
            AST::Program(stmt) => {
                let mut code = String::new();
                code.push_str("from nyar_runtime.prelude import *\n");
                for s in stmt {
                    code.push_str(s.to_python().as_str());
                    code.push_str("\n\n")
                }
                return code;
            }
            AST::EmptyStatement => String::new(),
            AST::ImportStatement { .. } => String::new(),
            AST::IfStatement { pairs, default, modifier } => {
                let mut head = true;
                let mut code = String::new();
                for (c, s) in pairs {
                    let i = if head {
                        head = false;
                        "if"
                    }
                    else {
                        "elif"
                    };
                    code.push_str(&format!("{}\n{} {}:\n", code, i, c.to_python()))
                }
                return code;
            }
            AST::UnaryOperators { base, prefix, postfix, modifier } => {
                let mut code = base.to_python();
                for op in postfix {
                    code = format!("__unary_post[\"{}\"]({})", op, code)
                }
                for op in prefix {
                    code = format!("__unary_pre[\"{}\"]({})", op, code)
                }
                return code;
            }
            AST::InfixOperators { operator, lhs, rhs, modifier } => {
                let l = lhs.to_python();
                let r = rhs.to_python();
                format!("__infix[\"{}\"]({},{})", operator, l, r)
            }
            AST::Symbol { name, scope } => {
                let mut code = String::new();
                for s in scope {
                    code.push_str(&format!("{}.", s))
                }
                code.push_str(name);
                return code;
            }
            AST::NumberLiteral { handler, data } => format!("__unary_num[\"{}\"](\"{}\")", handler, data),
            AST::StringLiteral { handler, data } => format!("__unary_str[\"{}\"]({:?})", handler, data),
            AST::String(s) => s.clone(),
            AST::Boolean(x) => match x {
                true => "True".to_string(),
                false => "False".to_string(),
            },
            AST::None => "None".to_string(),
            AST::CommentLiteral { .. } => String::new(),
            _ => unimplemented!(),
        };
    }

    fn save_python(&self, path: &str) -> Result<(), Error> {
        let s = self.to_python();
        let mut file = File::create(path)?;
        file.write_all(s.as_bytes())?;
        Ok(())
    }
}
