grammar Nyar;
// $antlr-format columnLimit 128;
// $antlr-format useTab false ;reflowComments false;
// $antlr-format alignColons hanging;
program: statement* EOF;
statement
    : emptyStatement
    | importStatement eos?
    | typeStatement eos?
    | assignStatment eos?
    | branchStatement eos?
    | loopStatement eos?
    | tryStatement eos?
    | traitStatement eos?
    | classStatement eos?
    | expression eos?
    | trinocular eos?
    | data eos?;
/*====================================================================================================================*/
// $antlr-format alignColons trailing;
emptyStatement : eos | Separate;
eos            : Semicolon;
Separate       : ';;';
Semicolon      : ';' | '\uFF1B'; //U+FF1B ；
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
importStatement
    : Using module = moduleName                         # ModuleInclude
    | Using module = moduleName As alias = identifier   # ModuleAlias
    | Using source = moduleName With? name = identifier # ModuleSymbol
    | Using source = moduleName With? idTuples          # ModuleSymbols
    | Using source = moduleName Dot idTuples            # ModuleSymbols
    | Using dict                                        # ModuleResolve;
moduleName
    : string
    | symbol
    | symbol (Dot symbol)
    | moduleLanguage moduleScope?
    | moduleScope?;
moduleLanguage: Suffix symbol;
moduleScope: Prefix symbol;
// $antlr-format alignColons trailing;
idTuples : '{' identifier (Comma identifier)* '}';
As       : 'as';
With     : 'with';
Using    : 'using';
Instance : 'instance';
Times    : '*';
Power    : '^';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
blockStatement: '{' statement* '}' | Colon expression | Colon statement* End;
blockNonEnd: '{' statement* '}' | statement*;
// $antlr-format alignColons trailing;
End   : 'end';
Colon : ':' | '\uFF1A'; //U+FF1A ：
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
expressionStatement: expression (Comma expression)*;
expression
    : functionCall                                                      # FunctionApply
    | left = expression Dot right = symbol                              # GetterApply
    | left = expression Dot right = functionCall                        # MethodApply
    | left = expression right = index                                   # IndexApply
    | assignStatment                                                    # AssignApply
    | left = identifier right = string                                  # SpecialString
    | left = expression As right = typeExpression                       # TypeConversion
    | op = pre_ops right = expression                                   # PrefixExpression
    | left = expression op = pst_ops                                    # PostfixExpression
    | left = expression op = bit_ops right = expression                 # BinaryLike
    | left = expression op = lgk_ops right = expression                 # LogicLike
    | left = expression op = cpr_ops right = expression                 # CompareLike
    | <assoc = right> left = expression op = pow_ops right = expression # PowerLike
    | left = expression op = mul_ops right = expression                 # MultiplyLike
    | left = expression op = add_ops right = expression                 # PlusLike
    | left = expression op = list_ops right = expression                # ListLike
    | atom = data                                                       # DataLiteral
    | '(' expression ')'                                                # PriorityExpression
    | controlFlow                                                       # ControlExpression
    | expression BitAnd                                                 # SlotCatch;
/* | left = number right = expression                                  # SpaceExpression*/
/*====================================================================================================================*/
trinocular
    : l = trinocularNest Nullable m = trinocularNest Colon r = trinocularNest # ConditionTrinocular
    | l = trinocularNest If m = trinocularNest Else r = trinocularNest        # IfElseTrinocular;
/*  | l = sym_or_num Power m = sym_or_num Mod r = sym_or_num         # PowerModTrinocular */
controlFlow
    : state = (Pass | Break) ('(' ')')?
    | state = (Throw | Yield | Await) expression
    | state = Return expressionStatement
    | state = Return '(' expressionStatement Comma? ')';
// $antlr-format alignColons trailing;
trinocularNest : expression | '(' trinocular ')';
functionCall   : symbols '(' (arguments (Comma arguments)*)? ')';
flowController : Pass | Break | Throw | Yield | Await;
Pass           : 'pass';
Return         : 'return';
Yield          : 'yield';
Await          : 'await';
Break          : 'break';
Throw          : 'throw';
Comma          : ',' | '\uFF0C'; //U+FF0C ，
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
arguments: expression | functionCall | data;
typeStatement
    : Type symbol Colon typeExpression End?
    | Type symbol '{' typeExpression '}'?;
typeExpression
    : symbols '(' (typeExpression (Comma typeExpression)*)? ')'
    | symbols '<' (typeExpression (Comma typeExpression)*)? '>'
    | typeExpression (BitOr | BitAnd) typeExpression
    | typeExpression '[' ']'
    | symbols (Nullable | Times)?
    | integer;
typeSuffix: (Tilde | Meets) typeExpression;
parameter
    : typeExpression? symbol
    | typeExpression? symbol Times
    | typeExpression? symbol Keywords
    | typeExpression? symbol Nullable symbol;
// $antlr-format alignColons trailing;
Type      : 'type';
BitOr     : '|';
BitAnd    : '&';
Nullable  : '?';
Keywords  : '**';
BaseInput : '^^';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
assignStatment
    : Val assignLHS assignRHS                                               # AssignValue
    | Var assignLHS assignRHS                                               # AssignVariable
    | Def assignLHS assignRHS                                               # AssignDefer
    | Def symbol '(' parameter (Comma parameter)* ')' typeSuffix? assignRHS # AssignFunction
    | symbol '(' parameter (Comma parameter)* ')' typeSuffix? Set assignRHS # AssignFunction
    | assignLHS Set assignRHS                                               # AssignValue
    | assignLHS Flexible assignRHS                                          # AssignVariable
    | assignLHS Delay assignRHS                                             # AssignDefer;
assignLHS
    : symbol typeSuffix?               # LHSSingle
    | maybeSymbol (Comma maybeSymbol)* # LHSTuple
    | symbols                          # LHSMaybeSetter
    | symbols index                    # LHSMaybeIndex;
assignRHS
    : expression                  # RHSExpression
    | Colon expression            # RHSExpression
    | '{' statement* '}'          # RHSStatement
    | Colon statement* End        # RHSStatement
    | expressionStatement         # RHSTuple
    | '(' expressionStatement ')' # RHSTuple
    | statement                   # RHSStatement;
maybeSymbol: symbols typeSuffix? | head = Tilde;
symbols: (symbol | symbolName) (Dot symbol)*;
symbolName: symbol (Name symbol)*;
// $antlr-format alignColons trailing;
Val      : 'val';
Var      : 'var';
Let      : 'let';
Def      : 'def';
Set      : '=';
Flexible : '.=' | '\u2250'; //U+2250 ≐
Name     : '::' | '\u2237'; //U+2237 ∷
Delay    : ':=' | '\u2254'; //U+2254 ≔
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
data: number | string | special | symbols | list | dict | index | solt;
number: complex | decimal | integer | Binary | Octal | Hexadecimal;
index
    : '[' indexValid (Comma? indexValid)* ']'
    | '⟦' indexValid (Comma? indexValid)* '⟧';
// $antlr-format alignColons trailing;
dict       : '{' keyValue? (Comma keyValue)* Comma? '}';
keyValue   : key = keyValid Colon value = element;
keyValid   : integer | symbol | string;
list       : '[' element? (Comma element)* Comma? ']';
element    : data | expression | statement;
indexValid : (symbol | integer) Colon?;
Plus       : '+';
Minus      : '-';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
branchStatement
    : If condition (Then | Colon)? blockNonEnd else?         # IfSingle
    | If condition (Then | Colon)? blockNonEnd elseIf* else? # IfNested
    | Switch condition switchController? switchBody          # SwitchStatement
    | Match condition matchBody                              # MatchStatement;
// $antlr-format alignColons trailing;
else   : Else expression | Else blockStatement;
elseIf : Else If condition (Then | Colon)? blockNonEnd;
If     : 'if';
Else   : 'else';
Then   : 'then';
// $antlr-format alignColons hanging;
caseBody //if no expr, must default
    : Case expression Colon blockNonEnd
    | expression Rule blockNonEnd
    | Default Colon blockNonEnd
    | Case Times Colon blockNonEnd
    | Times Rule blockNonEnd;
// $antlr-format alignColons trailing;
switchBody       : '{' caseBody* '}' | Colon caseBody* End;
switchController : Pass | Return | Break;
Switch           : 'switch';
Case             : 'case';
Default          : 'default';
// $antlr-format alignColons trailing;
matchBody : expression | blockStatement;
condition : expression | '(' expression ')';
Match     : 'match';
Rule      : '=>' | '\u27F9'; //U+27F9 ⟹;
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
tryStatement
    : Try blockStatement finalProduction
    | Try blockStatement (catchProduction finalProduction?);
catchProduction: Catch symbol blockStatement | Catch '(' symbol ')' blockStatement;
finalProduction: Final blockStatement;
// $antlr-format alignColons trailing;
Try   : 'try';
Catch : 'catch';
Final : 'final';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
loopStatement
    : For '(' expressionStatement ')' loopController? blockStatement # ForLoop
    | For identifier In expression loopController? blockStatement    # ForInLoop
    | While condition loopController? blockStatement                 # WhileLoop
    | Do loopController? blockStatement                              # DoLoop;
loopController: Async | Lazy;
// $antlr-format alignColons trailing;
Async : 'async';
Lazy  : 'lazy';
In    : 'in';
For   : 'for';
While : 'while';
Do    : 'do';
/*====================================================================================================================*/
Macro : 'macro';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
traitStatement: Trait symbol classExtends? classMeets? classBody;
classStatement: Class symbol classExtends? classMeets? classBody;
classExtends: Extends symbol+ | '(' symbol (Comma symbol)* ')';
classMeets: Meets symbol+ | Tilde symbol | Tilde '(' symbol (Comma symbol)* ')';
classBody
    : '{' classExpression* '}'
    | Colon classExpression* End
    | Colon classExpression;
classExpression
    : emptyStatement
    | identifier* symbol typeSuffix?
    | identifier* symbol typeSuffix? blockStatement
    | identifier* symbol '(' parameter* ')' typeSuffix? (Colon 'pass')?
    | identifier* symbol '(' parameter* ')' typeSuffix? blockStatement;
// $antlr-format alignColons trailing;
Trait   : 'trait';
Class   : 'class';
Extends : 'extends';
Meets   : 'meets';
Tilde   : '~';
Suffix  : '$';
Prefix  : '@';
/*====================================================================================================================*/
complex        : (Decimal | Integer) identifier;
decimal        : Decimal | DecimalBad;
integer        : Integer;
Decimal        : Integer Dot Digit;
DecimalBad     : Integer Dot | Dot Digit+;
Binary         : Zero B Bin+;
Octal          : Zero O Oct+;
Hexadecimal    : Zero X Hex+;
Integer        : Zero+ | [1-9] Digit*;
Exponent       : '*^';
Base           : '/^';
fragment Bin   : Zero | [1];
fragment Oct   : Zero | [1-7];
fragment Digit : Zero | [1-9];
fragment Hex   : Zero | [1-9a-fA-F];
fragment Zero  : [0];
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
string
    : StringEscapeBlock  # StringEscapeBlock
    | StringEscapeSingle # StringEscapeSingle
    | StringLiteral      # StringLiteral
    | StringEmpty        # StringEmpty;
// $antlr-format alignColons trailing;
StringEscapeBlock   : S6 CharLevel1+? S6;
StringEscapeSingle  : S2 CharLevel2+? S2;
StringLiteral       : S4 ~[\uFF02]+? S4;
StringEmpty         : S6 S6 | S2 S2 | S4 S4;
Escape              : '\\';
fragment S6         : '"""';
fragment S4         : '\uFF02'; //U+FF02 ＂
fragment S2         : '"';
fragment CharLevel1 : Escape . | ~[\\];
fragment CharLevel2 : Escape . | ~["\\];
fragment NonEscape  : ~[\u0001]+?;
/*====================================================================================================================*/
controller : flowController | switchController | loopController;
special    : True | False | Null | Nothing;
identifier : controller | Identifier;
symbol     : controller | Symbol | Identifier;
solt       : Sharp n = Integer? | Sharp id = Identifier;
Identifier : Letter+;
Symbol     : NameStartCharacter NameCharacter*;
True       : 'true';
False      : 'false';
Null       : 'null';
Nothing    : 'nothing';
Sharp      : '#';
Dot        : '.';
Underline  : '_';
fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];
// $antlr-format alignColons hanging;
fragment Letter
    : (A | B | C | D | E | F | G)
    | (H | I | J | K | L | M | N)
    | (O | P | Q | R | S | T)
    | (U | V | W | X | Y | Z);
fragment NameStartCharacter
    : (Underline | Letter)
    | [\p{Latin}]
    | [\p{Han}]
    | [\p{Hiragana}]
    | [\p{Katakana}]
    | [\p{Greek}];
// $antlr-format alignColons trailing;
fragment EmojiCharacter : [\p{Emoji}];
fragment NameCharacter  : NameStartCharacter | Digit;
/*====================================================================================================================*/
// $antlr-format alignColons trailing;
Shebang            : '#!' -> channel(HIDDEN);
Comment            : '%%%';
LineComment        : Shebang ~[\r\n]+ -> channel(HIDDEN);
PartComment        : Comment .*? Comment -> channel(HIDDEN);
NewLine            : ('\r'? '\n' | '\r')+ -> skip;
WhiteSpace         : UnicodeWS+ -> skip;
fragment UnicodeWS : [\p{White_Space}];
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
add_ops: Plus | Minus;
pre_ops: Plus | Minus | BitNot | LogicNot | Reciprocal | Increase;
pst_ops: Increase | BitNot | DoubleBang | Decrease;
bit_ops: LeftShift | RightShift | Exponent | Base;
lgk_ops: LogicAnd | LogicNot | LogicOr | LogicXor;
cpr_ops
    : (Equal | NotEqual | Equivalent | NotEquivalent)
    | (Grater | GraterEqual | Less | LessEqual)
    | (LogicAnd | LogicOr);
pow_ops: Power | Surd;
mul_ops: Divide | Mod | Remainder | Times | Multiply | Kronecker | TensorProduct;
list_ops: Concat | LeftShift | RightShift | Increase | Map;
// $antlr-format alignColons trailing;
/* <> */
Import      : '<<<' | '\u22D8'; //U+22D8 ⋘
LeftShift   : '<<' | '\u226A'; //U+226A ≪
LessEqual   : '<=';
Less        : '<';
Export      : '>>>' | '\u22D9'; //U+22D9 ⋙
RightShift  : '>>' | '\u226B'; //U+226B ≫
GraterEqual : '>=';
Grater      : '>';
/* +-÷ */
Increase      : '++';
PlusTo        : '+=';
LogicXor      : '\u2295'; //U+2295 ⊕
Decrease      : '--';
MinusFrom     : '-=';
Multiply      : '\u00D7'; //U+00D7 ×
Kronecker     : '\u2297'; //U+2297 ⊗
TensorProduct : '\u2299'; //U+2299 ⊙
MapAll        : '//@';
Remainder     : '//';
Map           : '/@';
Divide        : '/';
Quotient      : '\u00F7'; //U+00F7 ÷
Output        : '%%';
Mod           : '%';
/* =~ */
Equivalent    : '===';
NotEquivalent : '=!=';
Equal         : '=='; //≡
Concat        : '~~';
Destruct      : '~=';
/* |&! */
LogicOr    : '||' | '\u2227'; //U+2227 ∧
LogicAnd   : '&&' | '\u2228'; //U+2228 ∨
DoubleBang : '!!';
NotEqual   : '!=' | '\u2260'; //U+2260 ≠
BitNot     : '!' | '\uFF01'; //U+FF01 ！
LogicNot   : DoubleBang | '\u00AC'; //U+00AC ¬
Elvis      : ':?';
/* $ @ */
Curry     : '@@@';
Apply     : '@@';
LetAssign : '@=';
/* upper lower*/
Quote     : '`';
Acute     : '\u00B4'; // U+00B4 ´
Quotation : '\'';
Ellipsis  : '...'; //…
DOT       : '\u22C5'; //U+22C5 ⋅
/* Prefix */
Surd       : '\u221A'; //U+221A √
Reciprocal : '\u215F'; //U+215F ⅟
/* Postfix */
Degree    : '\u00B0'; //U+00B0 °
Transpose : '\u1D40'; //U+1D40 ᵀ
Hermitian : '\u1D34'; //U+1D34 ᴴ
/* Other */
Section  : '\u00A7'; //U+00A7 §
Pilcrow  : '\u00B6'; //U+00B6 ¶
Currency : '\u00A4'; //U+00A4 ¤
Element  : '\u2208'; //U+2208 ∈
