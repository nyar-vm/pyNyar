use crate::ToPython;
use nyar_valkyrie::AST;
use std::fs::File;
use std::io::{Error, Write};

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
            AST::UnaryOperators { .. } => String::new(),
            AST::InfixOperators { .. } => String::new(),
            AST::NumberLiteral { handler, data } => {
                format!("__unary_num[\"{}\"](\"{}\")", handler, data)
            }
            AST::StringLiteral { handler, data } => {
                format!("__unary_str[\"{}\"]({:?})", handler, data)
            }
            AST::String(s) => s.clone(),
            AST::CommentLiteral { .. } => String::new(),
            AST::Boolean(x) => match x {
                true => "True".to_string(),
                false => "False".to_string(),
            },
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
