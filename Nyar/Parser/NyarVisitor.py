# Generated from D:/Python/NyarPY\Nyar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NyarParser import NyarParser
else:
    from NyarParser import NyarParser

# This class defines a complete generic visitor for a parse tree produced by NyarParser.

class NyarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NyarParser#program.
    def visitProgram(self, ctx:NyarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#statement.
    def visitStatement(self, ctx:NyarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#emptyStatement.
    def visitEmptyStatement(self, ctx:NyarParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#eos.
    def visitEos(self, ctx:NyarParser.EosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ModuleInclude.
    def visitModuleInclude(self, ctx:NyarParser.ModuleIncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ModuleAlias.
    def visitModuleAlias(self, ctx:NyarParser.ModuleAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ModuleSymbol.
    def visitModuleSymbol(self, ctx:NyarParser.ModuleSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ModuleSymbols.
    def visitModuleSymbols(self, ctx:NyarParser.ModuleSymbolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ModuleResolve.
    def visitModuleResolve(self, ctx:NyarParser.ModuleResolveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#moduleName.
    def visitModuleName(self, ctx:NyarParser.ModuleNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#moduleLanguage.
    def visitModuleLanguage(self, ctx:NyarParser.ModuleLanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#moduleScope.
    def visitModuleScope(self, ctx:NyarParser.ModuleScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#idTuples.
    def visitIdTuples(self, ctx:NyarParser.IdTuplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#blockStatement.
    def visitBlockStatement(self, ctx:NyarParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#blockNonEnd.
    def visitBlockNonEnd(self, ctx:NyarParser.BlockNonEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#expressionStatement.
    def visitExpressionStatement(self, ctx:NyarParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#PriorityExpression.
    def visitPriorityExpression(self, ctx:NyarParser.PriorityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#DataLiteral.
    def visitDataLiteral(self, ctx:NyarParser.DataLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#FunctionApply.
    def visitFunctionApply(self, ctx:NyarParser.FunctionApplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#BinaryLike.
    def visitBinaryLike(self, ctx:NyarParser.BinaryLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#LogicLike.
    def visitLogicLike(self, ctx:NyarParser.LogicLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#MethodApply.
    def visitMethodApply(self, ctx:NyarParser.MethodApplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#IndexApply.
    def visitIndexApply(self, ctx:NyarParser.IndexApplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#CompareLike.
    def visitCompareLike(self, ctx:NyarParser.CompareLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#PlusLike.
    def visitPlusLike(self, ctx:NyarParser.PlusLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#SlotCatch.
    def visitSlotCatch(self, ctx:NyarParser.SlotCatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#PowerLike.
    def visitPowerLike(self, ctx:NyarParser.PowerLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#TypeConversion.
    def visitTypeConversion(self, ctx:NyarParser.TypeConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ControlExpression.
    def visitControlExpression(self, ctx:NyarParser.ControlExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#PrefixExpression.
    def visitPrefixExpression(self, ctx:NyarParser.PrefixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#AssignApply.
    def visitAssignApply(self, ctx:NyarParser.AssignApplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#SpecialString.
    def visitSpecialString(self, ctx:NyarParser.SpecialStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#PostfixExpression.
    def visitPostfixExpression(self, ctx:NyarParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#MultiplyLike.
    def visitMultiplyLike(self, ctx:NyarParser.MultiplyLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#GetterApply.
    def visitGetterApply(self, ctx:NyarParser.GetterApplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ListLike.
    def visitListLike(self, ctx:NyarParser.ListLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#controlFlow.
    def visitControlFlow(self, ctx:NyarParser.ControlFlowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#functionCall.
    def visitFunctionCall(self, ctx:NyarParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#arguments.
    def visitArguments(self, ctx:NyarParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#flowController.
    def visitFlowController(self, ctx:NyarParser.FlowControllerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#typeStatement.
    def visitTypeStatement(self, ctx:NyarParser.TypeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#typeExpression.
    def visitTypeExpression(self, ctx:NyarParser.TypeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#typeSuffix.
    def visitTypeSuffix(self, ctx:NyarParser.TypeSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#AssignValue.
    def visitAssignValue(self, ctx:NyarParser.AssignValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#AssignVariable.
    def visitAssignVariable(self, ctx:NyarParser.AssignVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#AssignDefer.
    def visitAssignDefer(self, ctx:NyarParser.AssignDeferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#AssignFunction.
    def visitAssignFunction(self, ctx:NyarParser.AssignFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#LHSSingle.
    def visitLHSSingle(self, ctx:NyarParser.LHSSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#LHSTuple.
    def visitLHSTuple(self, ctx:NyarParser.LHSTupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#LHSMaybeSetter.
    def visitLHSMaybeSetter(self, ctx:NyarParser.LHSMaybeSetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#LHSMaybeIndex.
    def visitLHSMaybeIndex(self, ctx:NyarParser.LHSMaybeIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#assignRHS.
    def visitAssignRHS(self, ctx:NyarParser.AssignRHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#parameter.
    def visitParameter(self, ctx:NyarParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#functionPattern.
    def visitFunctionPattern(self, ctx:NyarParser.FunctionPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#maybeSymbol.
    def visitMaybeSymbol(self, ctx:NyarParser.MaybeSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#MaybeMethod.
    def visitMaybeMethod(self, ctx:NyarParser.MaybeMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#MustMethod.
    def visitMustMethod(self, ctx:NyarParser.MustMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ifStatment.
    def visitIfStatment(self, ctx:NyarParser.IfStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ifShort.
    def visitIfShort(self, ctx:NyarParser.IfShortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ifSingle.
    def visitIfSingle(self, ctx:NyarParser.IfSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ifNested.
    def visitIfNested(self, ctx:NyarParser.IfNestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#else.
    def visitElse(self, ctx:NyarParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#elseIf.
    def visitElseIf(self, ctx:NyarParser.ElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#switchStatment.
    def visitSwitchStatment(self, ctx:NyarParser.SwitchStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#caseBody.
    def visitCaseBody(self, ctx:NyarParser.CaseBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#switchBody.
    def visitSwitchBody(self, ctx:NyarParser.SwitchBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#matchStatment.
    def visitMatchStatment(self, ctx:NyarParser.MatchStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#matchBody.
    def visitMatchBody(self, ctx:NyarParser.MatchBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#condition.
    def visitCondition(self, ctx:NyarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#tryStatement.
    def visitTryStatement(self, ctx:NyarParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#tryCatch.
    def visitTryCatch(self, ctx:NyarParser.TryCatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#tryFinal.
    def visitTryFinal(self, ctx:NyarParser.TryFinalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ForLoop.
    def visitForLoop(self, ctx:NyarParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#ForInLoop.
    def visitForInLoop(self, ctx:NyarParser.ForInLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#DoLoop.
    def visitDoLoop(self, ctx:NyarParser.DoLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#whileStatment.
    def visitWhileStatment(self, ctx:NyarParser.WhileStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#letStatment.
    def visitLetStatment(self, ctx:NyarParser.LetStatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#classBody.
    def visitClassBody(self, ctx:NyarParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#classExpression.
    def visitClassExpression(self, ctx:NyarParser.ClassExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#traitStatement.
    def visitTraitStatement(self, ctx:NyarParser.TraitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#classStatement.
    def visitClassStatement(self, ctx:NyarParser.ClassStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#classExtend.
    def visitClassExtend(self, ctx:NyarParser.ClassExtendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#classTrait.
    def visitClassTrait(self, ctx:NyarParser.ClassTraitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#classController.
    def visitClassController(self, ctx:NyarParser.ClassControllerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#data.
    def visitData(self, ctx:NyarParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#number.
    def visitNumber(self, ctx:NyarParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#index.
    def visitIndex(self, ctx:NyarParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#dict.
    def visitDict(self, ctx:NyarParser.DictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#keyValue.
    def visitKeyValue(self, ctx:NyarParser.KeyValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#keyValid.
    def visitKeyValid(self, ctx:NyarParser.KeyValidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#list.
    def visitList(self, ctx:NyarParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#element.
    def visitElement(self, ctx:NyarParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#indexValid.
    def visitIndexValid(self, ctx:NyarParser.IndexValidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#complex.
    def visitComplex(self, ctx:NyarParser.ComplexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#decimal.
    def visitDecimal(self, ctx:NyarParser.DecimalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#integer.
    def visitInteger(self, ctx:NyarParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#StringEscapeBlock.
    def visitStringEscapeBlock(self, ctx:NyarParser.StringEscapeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#StringEscapeSingle.
    def visitStringEscapeSingle(self, ctx:NyarParser.StringEscapeSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#StringLiteral.
    def visitStringLiteral(self, ctx:NyarParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#StringEmpty.
    def visitStringEmpty(self, ctx:NyarParser.StringEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#controller.
    def visitController(self, ctx:NyarParser.ControllerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#special.
    def visitSpecial(self, ctx:NyarParser.SpecialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#symbol.
    def visitSymbol(self, ctx:NyarParser.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#solt.
    def visitSolt(self, ctx:NyarParser.SoltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#add_ops.
    def visitAdd_ops(self, ctx:NyarParser.Add_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#pre_ops.
    def visitPre_ops(self, ctx:NyarParser.Pre_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#pst_ops.
    def visitPst_ops(self, ctx:NyarParser.Pst_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#bit_ops.
    def visitBit_ops(self, ctx:NyarParser.Bit_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#lgk_ops.
    def visitLgk_ops(self, ctx:NyarParser.Lgk_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#cpr_ops.
    def visitCpr_ops(self, ctx:NyarParser.Cpr_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#pow_ops.
    def visitPow_ops(self, ctx:NyarParser.Pow_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#mul_ops.
    def visitMul_ops(self, ctx:NyarParser.Mul_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NyarParser#list_ops.
    def visitList_ops(self, ctx:NyarParser.List_opsContext):
        return self.visitChildren(ctx)



del NyarParser