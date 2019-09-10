use crate::ToPython;
use nyar_valkyrie::AST;
use std::io::{Error, Write};
use std::fs::File;


impl ToPython for AST {
    fn to_python(&self) -> String {
        return match self {
            AST::None => { String::new() }
            AST::Program(stmt) => {
                let mut code = String::new();
                for s in stmt {
                    code.push_str(s.to_python().as_str());
                    code.push_str("\n\n")
                }
                return code;
            }
            AST::EmptyStatement => { String::new() }
            AST::ImportStatement { .. } => { String::new() }
            AST::UnaryOperators { .. } => { String::new() }
            AST::InfixOperators { .. } => { String::new() }
            AST::NumberLiteral { handler, data } => {
                format!("__unary_num['{}']('{}')", handler, data)
            }
            AST::StringLiteral { .. } => { String::new() }
            AST::String(s) => { s.clone() }
            AST::CommentLiteral { .. } => { String::new() }
            AST::Boolean(_) => { String::new() }
            _ => unimplemented!()
        };
    }

    fn save_python(&self, path: &str) -> Result<(), Error> {
        let s = self.to_python();
        let mut file = File::create(path)?;
        file.write_all(s.as_bytes())?;
        Ok(())
    }
}
