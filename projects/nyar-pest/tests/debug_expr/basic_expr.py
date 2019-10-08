from nyar_runtime.prelude import *
__unary_post["!"](__unary_post["!"](__unary_num["int"]("1")))

__infix["+"](__unary_num["int"]("1"),__infix["*"](__unary_num["int"]("2"),__infix["^"](__unary_num["int"]("3"),__unary_pre["-"](__unary_post["!"](__unary_post["!"](__unary_num["int"]("4")))))))

__infix["+"](__unary_num["int"]("1"),__unary_pre["+"](__unary_pre["+"](__unary_num["int"]("2"))))

__infix["*"](__unary_num["int"]("1"),__infix["+"](__unary_num["int"]("2"),__unary_num["int"]("3")))

