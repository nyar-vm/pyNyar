grammar Nyar;
// $antlr-format columnLimit 128;
// $antlr-format useTab false ;reflowComments false;
// $antlr-format alignColons hanging;
program: statement* EOF;
statement
    : emptyStatement
    | (importStatement | exportStatment) eos?
    | (letStatment | assignStatment) eos?
    | (switchStatment | ifStatment | matchStatment | forStatement | whileStatment) eos?
    | (typeStatement | traitStatement | classStatement) eos?
    | (interfaceStatement | structureStatement | enumerateStatement) eos?
    | tryStatement eos?
    | expression eos?
    | data eos?;
/*====================================================================================================================*/
// $antlr-format alignColons trailing;
emptyStatement : eos | Separate;
// $antlr-format alignColons trailing;
eos       : Semicolon;
Separate  : ';;';
Semicolon : ';' | '\uFF1B'; //U+FF1B ；
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
importStatement
    : Using name = moduleName mod = (Star | Power)?  # ModuleModify
    | Using name = moduleName As symbol              # ModuleAlias
    | Using name = moduleName With? symbol           # ModuleSymbol
    | Using name = moduleName (With | Dot)? idTuples # ModuleSymbols
    | Using dict                                     # ModuleResolve;
moduleName: string | symbol | moduleLanguage? moduleScope? symbols;
moduleLanguage: Suffix symbol Slash;
moduleScope: Prefix symbol Slash;
exportStatment: Expose symbol;
// $antlr-format alignColons trailing;
idTuples : '{' symbol (Comma symbol)* '}';
As       : 'as';
Using    : 'using';
Expose   : 'expose';
Divide   : Slash | '\u00F7'; //U+00F7 ÷
Multiply : Star | '\u00D7'; //U+00D7 ×
Star     : '*';
Slash    : '/';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
blockStatement: '{' statement* '}' | Colon statement* End | Colon expression;
blockNonEnd: '{' statement* '}' | Colon? statement+;
// $antlr-format alignColons trailing;
Colon : ':' | '\uFF1A'; //U+FF1A ：
End   : 'end' | '\u00AD'; // U+00AD
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
expressionStatement: expression (Comma expression)*;
expression
    : functionCall                                                      # FunctionApply
    | left = expression Dot right = symbol                              # GetterApply
    | left = expression Dot right = functionCall                        # MethodApply
    | left = expression right = index                                   # IndexApply
    | assignStatment                                                    # AssignApply
    | left = symbol right = string                                      # SpecialString
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
/*  | left = number right = expression                                  # SpaceExpression*/
/*====================================================================================================================*/
controlFlow
    : state = (Pass | Break) ('(' ')')?
    | state = (Throw | Yield | Await) expression
    | state = Return expressionStatement
    | state = Return '(' expressionStatement Comma? ')';
// $antlr-format alignColons trailing;
functionCall   : symbols '(' (arguments (Comma arguments)* Comma?)? ')';
arguments      : expression | functionCall | data;
flowController : Pass | Break | Throw | Yield | Await;
// $antlr-format alignColons trailing;
Pass   : 'pass';
Return : 'return';
Yield  : 'yield';
Await  : 'await';
Break  : 'break';
Throw  : 'throw';
Comma  : ',' | '\uFF0C'; //U+FF0C ，
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
typeStatement
    : Type symbol Colon typeExpression End?
    | Type symbol '{' typeExpression '}'?;
typeExpression
    : symbol '(' (typeExpression (Comma typeExpression)*)? ')'
    | symbol '<' (typeExpression (Comma typeExpression)*)? '>'
    | typeExpression (BitOr | BitAnd) typeExpression
    | typeExpression '[' ']'
    | symbol (Nullable | Star)?
    | integer;
typeSuffix: (Tilde | Act) typeExpression;
// $antlr-format alignColons trailing;
Type      : 'type';
BitOr     : '|';
BitAnd    : '&';
Nullable  : '?';
Keyword   : '**';
BaseInput : '^^';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
assignStatment
    : Val assignLHS blockStatement            # AssignValue
    | Var assignLHS blockStatement            # AssignVariable
    | Def assignLHS blockStatement            # AssignDefer
    | Def functionPattern blockStatement      # AssignFunction
    | functionPattern (Set | Delay) assignRHS # AssignFunction
    | assignLHS mod_assign Set assignRHS      # AssignModify
    | assignLHS Set assignRHS                 # AssignValue
    | assignLHS Flexible assignRHS            # AssignVariable
    | assignLHS Delay assignRHS               # AssignDefer;
assignLHS
    : symbol typeSuffix?               # LHSSingle
    | maybeSymbol (Comma maybeSymbol)* # LHSTuple
    | symbols                          # LHSMaybeSetter
    | symbols index                    # LHSMaybeIndex;
assignRHS
    : expression
    | expressionStatement
    | statement
    | '{' statement* '}'
    | Colon statement* End;
parameter
    : typeExpression? symbol
    | typeExpression? symbol Star
    | typeExpression? symbol Keyword
    | typeExpression? symbol Nullable symbol;
// $antlr-format alignColons trailing;
functionPattern : symbol '(' parameter (Comma parameter)* Comma? ')' typeSuffix?;
maybeSymbol     : symbols typeSuffix? | Suffix;
symbols         : Symbols # MaybeMethod | TrueName Dot symbol # MustMethod;
// $antlr-format alignColons trailing;
Val      : 'val';
Var      : 'var';
Def      : 'def';
Set      : '=';
Flexible : '.=' | '\u2250'; //U+2250 ≐
Name     : '::' | '\u2237'; //U+2237 ∷
Delay    : ':=' | '\u2254'; //U+2254 ≔
/*====================================================================================================================*/
ifStatment : If ifShort | If ifSingle | If ifNested;
// $antlr-format alignColons hanging;
ifShort: condition expression | condition blockStatement;
ifSingle
    : condition blockNonEnd Else expression
    | condition blockNonEnd Else blockStatement;
ifNested
    : condition blockNonEnd elseIf+ Else expression
    | condition blockNonEnd elseIf+ Else blockStatement
    | condition blockNonEnd elseIf* elif ifShort;
// $antlr-format alignColons trailing;
elif   : ElseIf | Else If;
elseIf : elif condition blockNonEnd;
If     : 'if';
Else   : 'else';
ElseIf : 'elseif';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
switchStatment: Switch condition switchBody;
caseBody //if no expr, must default
    : Case expression Colon blockNonEnd
    | expression Rule blockNonEnd
    | Default Colon blockNonEnd
    | Case Star Colon blockNonEnd
    | Star Rule blockNonEnd;
// $antlr-format alignColons trailing;
switchBody : '{' caseBody* '}' | Colon caseBody* End;
Switch     : 'switch';
Case       : 'case';
Default    : 'default';
/*====================================================================================================================*/
matchStatment : Match condition matchBody;
matchBody     : expression | blockStatement;
condition     : expression | '(' expression ')';
Match         : 'match';
Rule          : '=>' | '\u27F9'; //U+27F9 ⟹;
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
tryStatement
    : Try blockNonEnd (Catch tryCatch)+ tryFinal
    | Try blockNonEnd Catch symbol blockNonEnd
    | Try blockNonEnd Catch '(' symbol ')' blockNonEnd;
tryCatch: symbol blockNonEnd | '(' symbol ')' blockNonEnd;
tryFinal: Final blockStatement;
// $antlr-format alignColons trailing;
Try   : 'try';
Catch : 'catch';
Final : 'final';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
forStatement
    : For '(' expressionStatement ')' blockStatement # ForLoop
    | For symbol In expression blockStatement        # ForInLoop;
whileStatment: While condition blockStatement;
// $antlr-format alignColons trailing;
In    : 'in';
For   : 'for';
While : 'while';
/*====================================================================================================================*/
letStatment : Let symbol* statement | Let symbol* blockStatement;
Macro       : 'macro';
With        : 'with';
Let         : 'let';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
classExpression
    : emptyStatement classEos?
    | classController* symbol typeSuffix? classEos?
    | classController* symbol typeSuffix? blockStatement classEos?
    | classController* symbol '(' parameter* ')' typeSuffix? blockStatement classEos?;
classStatement
    : Class symbol classExtend? classTrait? '{' classExpression* '}'
    | Class symbol classExtend? classTrait? Colon classExpression* End;
// $antlr-format alignColons trailing;
classExtend     : Extend symbol+ | '(' symbol (Comma symbol)* ')';
classTrait      : Act symbol+ | Tilde symbol | Tilde '(' symbol (Comma symbol)* ')';
classController : symbol | Val | Var | Def;
classEos        : Semicolon | Comma;
// $antlr-format alignColons trailing;
Class  : 'class';
Extend : 'extend';
Act    : 'act';
Tilde  : '~';
Suffix : '$';
Prefix : '@';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
traitStatement
    : Trait symbol classExtend? classTrait? '{' traitExpression* '}'
    | Trait symbol classExtend? classTrait? Colon traitExpression* End;
interfaceStatement
    : Interface symbol classExtend? classTrait? '{' interfaceExpression '}'
    | Interface symbol classExtend? classTrait? Colon interfaceExpression* End;
structureStatement
    : Structure symbol classExtend? classTrait? '{' structureExpression* '}'
    | Structure symbol classExtend? classTrait? Colon structureExpression* End;
enumerateStatement
    : Enumerate e = (Plus | Star)? symbol classExtend? classTrait? '{' enumerateExpression* '}'
    | Enumerate e = (Plus | Star)? symbol classExtend? classTrait? Colon enumerateExpression* End;
traitExpression: interfaceExpression | structureExpression;
interfaceExpression: interfaceFunction Colon typeExpression classEos?;
interfaceFunction: symbol '(' interfaceParameters? ')' e = Nullable?;
interfaceParameters: typeExpression symbol (Comma typeExpression symbol)*;
structureExpression: symbol e = Nullable Colon typeExpression classEos?;
enumerateExpression: symbol classEos? | symbol Colon enumerateNumber classEos?;
enumerateNumber: number | symbol BitOr symbol;
// $antlr-format alignColons trailing;
Enumerate : 'enumerate';
Structure : 'structure';
Interface : 'interface';
Trait     : 'trait';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
data: number | string | special | symbol | symbols | list | dict | index | solt;
number: complex | decimal | integer | byteInput;
byteInput: Binary | Octal | Hexadecimal;
index
    : '[' indexValid (Comma? indexValid)* ']'
    | '⟦' indexValid (Comma? indexValid)* '⟧';
indexValid
    : (indexTerm | list)                        # IndexTake
    | Colon                                     # Index000
    | Name indexTerm                            # Index001
    | Colon Colon indexTerm                     # Index001
    | Colon indexTerm Colon?                    # Index010
    | Colon indexTerm Colon indexTerm           # Index011
    | indexTerm Name                            # Index100
    | indexTerm Colon Colon?                    # Index100
    | indexTerm Name indexTerm                  # Index101
    | indexTerm Colon Colon indexTerm           # Index101
    | indexTerm Colon indexTerm Colon?          # Index110
    | indexTerm Colon indexTerm Colon indexTerm # Index111;
indexTerm: symbol | sign = (Plus | Minus)? integer;
// $antlr-format alignColons trailing;
dict     : '{' keyValue? (Comma keyValue)* Comma? '}';
keyValue : key = keyValid Colon value = element;
keyValid : integer | symbol | string;
list     : '[' element? (Comma element)* Comma? ']';
element  : data | expression | statement;
Plus     : '+';
Minus    : '-';
Power    : '^';
Surd     : '\u221A'; //U+221A √
/*====================================================================================================================*/
complex        : (Decimal | Integer) symbol;
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
    : StringEmpty         # StringEmpty
    | StringEscapeBlock   # StringEscapeBlock
    | StringEscapeSingle  # StringEscapeSingle
    | StringLiteralBlock  # StringLiteralBlock
    | StringLiteralSingle # StringLiteralSingle;
// $antlr-format alignColons trailing;
StringEscapeBlock   : S6 CharLevel1+? S6;
StringEscapeSingle  : S2 CharLevel2+? S2;
StringLiteralBlock  : S3 .+? S3;
StringLiteralSingle : S1 ~[\uFF02]+? S1;
StringEmpty         : S6 S6 | S3 S3 | S2 S2 | S1 S1;
Escape              : '\\';
fragment S6         : '"""';
fragment S3         : '\uFF02\uFF02\uFF02';
fragment S2         : '"';
fragment S1         : '\uFF02'; //U+FF02 ＂
fragment CharLevel1 : Escape ~[ ] | ~[\\];
fragment CharLevel2 : Escape ~[ ] | ~["\\];
/*====================================================================================================================*/
special : True | False | Null | Nothing;
True    : 'true';
False   : 'false';
Null    : 'null';
Nothing : 'nothing';
/*====================================================================================================================*/
symbol     : flowController | Symbol | TrueName;
solt       : Sharp n = Integer? | Sharp id = symbol;
Symbols    : Symbol (Dot Symbol)+;
TrueName   : Symbol (Name Symbol)*;
Symbol     : NameStartCharacter NameCharacter*;
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
Remark             : '///' -> channel(HIDDEN);
Comment            : '%%%';
LineComment        : (Shebang | Remark) ~[\r\n]+ -> channel(HIDDEN);
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
mul_ops: Divide | Modulo | Quotient | Multiply | Kronecker | TensorProduct;
list_ops: Concat | LeftShift | RightShift | Increase | Map;
mod_assign: Plus | Minus | Star | Divide;
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
LogicXor      : '\u2295'; //U+2295 ⊕
Decrease      : '--';
Kronecker     : '\u2297'; //U+2297 ⊗
TensorProduct : '\u2299'; //U+2299 ⊙
MapAll        : '//@';
Quotient      : '//';
Map           : '/@';
Output        : '%%';
Modulo        : '%';
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
