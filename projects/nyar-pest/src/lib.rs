pub mod utils;

use nyar_valkyrie::{get_ast,AST};

pub trait ToPython {
    fn to_python(self);
    fn save_python(self);
}

