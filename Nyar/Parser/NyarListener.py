# Generated from D:/Python/NyarPY\Nyar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NyarParser import NyarParser
else:
    from NyarParser import NyarParser

# This class defines a complete listener for a parse tree produced by NyarParser.
class NyarListener(ParseTreeListener):

    # Enter a parse tree produced by NyarParser#program.
    def enterProgram(self, ctx:NyarParser.ProgramContext):
        pass

    # Exit a parse tree produced by NyarParser#program.
    def exitProgram(self, ctx:NyarParser.ProgramContext):
        pass


    # Enter a parse tree produced by NyarParser#statement.
    def enterStatement(self, ctx:NyarParser.StatementContext):
        pass

    # Exit a parse tree produced by NyarParser#statement.
    def exitStatement(self, ctx:NyarParser.StatementContext):
        pass


    # Enter a parse tree produced by NyarParser#emptyStatement.
    def enterEmptyStatement(self, ctx:NyarParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#emptyStatement.
    def exitEmptyStatement(self, ctx:NyarParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#eos.
    def enterEos(self, ctx:NyarParser.EosContext):
        pass

    # Exit a parse tree produced by NyarParser#eos.
    def exitEos(self, ctx:NyarParser.EosContext):
        pass


    # Enter a parse tree produced by NyarParser#ModuleModify.
    def enterModuleModify(self, ctx:NyarParser.ModuleModifyContext):
        pass

    # Exit a parse tree produced by NyarParser#ModuleModify.
    def exitModuleModify(self, ctx:NyarParser.ModuleModifyContext):
        pass


    # Enter a parse tree produced by NyarParser#ModuleAlias.
    def enterModuleAlias(self, ctx:NyarParser.ModuleAliasContext):
        pass

    # Exit a parse tree produced by NyarParser#ModuleAlias.
    def exitModuleAlias(self, ctx:NyarParser.ModuleAliasContext):
        pass


    # Enter a parse tree produced by NyarParser#ModuleSymbol.
    def enterModuleSymbol(self, ctx:NyarParser.ModuleSymbolContext):
        pass

    # Exit a parse tree produced by NyarParser#ModuleSymbol.
    def exitModuleSymbol(self, ctx:NyarParser.ModuleSymbolContext):
        pass


    # Enter a parse tree produced by NyarParser#ModuleSymbols.
    def enterModuleSymbols(self, ctx:NyarParser.ModuleSymbolsContext):
        pass

    # Exit a parse tree produced by NyarParser#ModuleSymbols.
    def exitModuleSymbols(self, ctx:NyarParser.ModuleSymbolsContext):
        pass


    # Enter a parse tree produced by NyarParser#ModuleResolve.
    def enterModuleResolve(self, ctx:NyarParser.ModuleResolveContext):
        pass

    # Exit a parse tree produced by NyarParser#ModuleResolve.
    def exitModuleResolve(self, ctx:NyarParser.ModuleResolveContext):
        pass


    # Enter a parse tree produced by NyarParser#moduleName.
    def enterModuleName(self, ctx:NyarParser.ModuleNameContext):
        pass

    # Exit a parse tree produced by NyarParser#moduleName.
    def exitModuleName(self, ctx:NyarParser.ModuleNameContext):
        pass


    # Enter a parse tree produced by NyarParser#moduleLanguage.
    def enterModuleLanguage(self, ctx:NyarParser.ModuleLanguageContext):
        pass

    # Exit a parse tree produced by NyarParser#moduleLanguage.
    def exitModuleLanguage(self, ctx:NyarParser.ModuleLanguageContext):
        pass


    # Enter a parse tree produced by NyarParser#moduleScope.
    def enterModuleScope(self, ctx:NyarParser.ModuleScopeContext):
        pass

    # Exit a parse tree produced by NyarParser#moduleScope.
    def exitModuleScope(self, ctx:NyarParser.ModuleScopeContext):
        pass


    # Enter a parse tree produced by NyarParser#exportStatment.
    def enterExportStatment(self, ctx:NyarParser.ExportStatmentContext):
        pass

    # Exit a parse tree produced by NyarParser#exportStatment.
    def exitExportStatment(self, ctx:NyarParser.ExportStatmentContext):
        pass


    # Enter a parse tree produced by NyarParser#idTuples.
    def enterIdTuples(self, ctx:NyarParser.IdTuplesContext):
        pass

    # Exit a parse tree produced by NyarParser#idTuples.
    def exitIdTuples(self, ctx:NyarParser.IdTuplesContext):
        pass


    # Enter a parse tree produced by NyarParser#blockStatement.
    def enterBlockStatement(self, ctx:NyarParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#blockStatement.
    def exitBlockStatement(self, ctx:NyarParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#blockNonEnd.
    def enterBlockNonEnd(self, ctx:NyarParser.BlockNonEndContext):
        pass

    # Exit a parse tree produced by NyarParser#blockNonEnd.
    def exitBlockNonEnd(self, ctx:NyarParser.BlockNonEndContext):
        pass


    # Enter a parse tree produced by NyarParser#expressionStatement.
    def enterExpressionStatement(self, ctx:NyarParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#expressionStatement.
    def exitExpressionStatement(self, ctx:NyarParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#PriorityExpression.
    def enterPriorityExpression(self, ctx:NyarParser.PriorityExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#PriorityExpression.
    def exitPriorityExpression(self, ctx:NyarParser.PriorityExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#DataLiteral.
    def enterDataLiteral(self, ctx:NyarParser.DataLiteralContext):
        pass

    # Exit a parse tree produced by NyarParser#DataLiteral.
    def exitDataLiteral(self, ctx:NyarParser.DataLiteralContext):
        pass


    # Enter a parse tree produced by NyarParser#FunctionApply.
    def enterFunctionApply(self, ctx:NyarParser.FunctionApplyContext):
        pass

    # Exit a parse tree produced by NyarParser#FunctionApply.
    def exitFunctionApply(self, ctx:NyarParser.FunctionApplyContext):
        pass


    # Enter a parse tree produced by NyarParser#BinaryLike.
    def enterBinaryLike(self, ctx:NyarParser.BinaryLikeContext):
        pass

    # Exit a parse tree produced by NyarParser#BinaryLike.
    def exitBinaryLike(self, ctx:NyarParser.BinaryLikeContext):
        pass


    # Enter a parse tree produced by NyarParser#LogicLike.
    def enterLogicLike(self, ctx:NyarParser.LogicLikeContext):
        pass

    # Exit a parse tree produced by NyarParser#LogicLike.
    def exitLogicLike(self, ctx:NyarParser.LogicLikeContext):
        pass


    # Enter a parse tree produced by NyarParser#MethodApply.
    def enterMethodApply(self, ctx:NyarParser.MethodApplyContext):
        pass

    # Exit a parse tree produced by NyarParser#MethodApply.
    def exitMethodApply(self, ctx:NyarParser.MethodApplyContext):
        pass


    # Enter a parse tree produced by NyarParser#IndexApply.
    def enterIndexApply(self, ctx:NyarParser.IndexApplyContext):
        pass

    # Exit a parse tree produced by NyarParser#IndexApply.
    def exitIndexApply(self, ctx:NyarParser.IndexApplyContext):
        pass


    # Enter a parse tree produced by NyarParser#CompareLike.
    def enterCompareLike(self, ctx:NyarParser.CompareLikeContext):
        pass

    # Exit a parse tree produced by NyarParser#CompareLike.
    def exitCompareLike(self, ctx:NyarParser.CompareLikeContext):
        pass


    # Enter a parse tree produced by NyarParser#PlusLike.
    def enterPlusLike(self, ctx:NyarParser.PlusLikeContext):
        pass

    # Exit a parse tree produced by NyarParser#PlusLike.
    def exitPlusLike(self, ctx:NyarParser.PlusLikeContext):
        pass


    # Enter a parse tree produced by NyarParser#SlotCatch.
    def enterSlotCatch(self, ctx:NyarParser.SlotCatchContext):
        pass

    # Exit a parse tree produced by NyarParser#SlotCatch.
    def exitSlotCatch(self, ctx:NyarParser.SlotCatchContext):
        pass


    # Enter a parse tree produced by NyarParser#PowerLike.
    def enterPowerLike(self, ctx:NyarParser.PowerLikeContext):
        pass

    # Exit a parse tree produced by NyarParser#PowerLike.
    def exitPowerLike(self, ctx:NyarParser.PowerLikeContext):
        pass


    # Enter a parse tree produced by NyarParser#TypeConversion.
    def enterTypeConversion(self, ctx:NyarParser.TypeConversionContext):
        pass

    # Exit a parse tree produced by NyarParser#TypeConversion.
    def exitTypeConversion(self, ctx:NyarParser.TypeConversionContext):
        pass


    # Enter a parse tree produced by NyarParser#ControlExpression.
    def enterControlExpression(self, ctx:NyarParser.ControlExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#ControlExpression.
    def exitControlExpression(self, ctx:NyarParser.ControlExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#PrefixExpression.
    def enterPrefixExpression(self, ctx:NyarParser.PrefixExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#PrefixExpression.
    def exitPrefixExpression(self, ctx:NyarParser.PrefixExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#AssignApply.
    def enterAssignApply(self, ctx:NyarParser.AssignApplyContext):
        pass

    # Exit a parse tree produced by NyarParser#AssignApply.
    def exitAssignApply(self, ctx:NyarParser.AssignApplyContext):
        pass


    # Enter a parse tree produced by NyarParser#SpecialString.
    def enterSpecialString(self, ctx:NyarParser.SpecialStringContext):
        pass

    # Exit a parse tree produced by NyarParser#SpecialString.
    def exitSpecialString(self, ctx:NyarParser.SpecialStringContext):
        pass


    # Enter a parse tree produced by NyarParser#PostfixExpression.
    def enterPostfixExpression(self, ctx:NyarParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#PostfixExpression.
    def exitPostfixExpression(self, ctx:NyarParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#MultiplyLike.
    def enterMultiplyLike(self, ctx:NyarParser.MultiplyLikeContext):
        pass

    # Exit a parse tree produced by NyarParser#MultiplyLike.
    def exitMultiplyLike(self, ctx:NyarParser.MultiplyLikeContext):
        pass


    # Enter a parse tree produced by NyarParser#GetterApply.
    def enterGetterApply(self, ctx:NyarParser.GetterApplyContext):
        pass

    # Exit a parse tree produced by NyarParser#GetterApply.
    def exitGetterApply(self, ctx:NyarParser.GetterApplyContext):
        pass


    # Enter a parse tree produced by NyarParser#ListLike.
    def enterListLike(self, ctx:NyarParser.ListLikeContext):
        pass

    # Exit a parse tree produced by NyarParser#ListLike.
    def exitListLike(self, ctx:NyarParser.ListLikeContext):
        pass


    # Enter a parse tree produced by NyarParser#controlFlow.
    def enterControlFlow(self, ctx:NyarParser.ControlFlowContext):
        pass

    # Exit a parse tree produced by NyarParser#controlFlow.
    def exitControlFlow(self, ctx:NyarParser.ControlFlowContext):
        pass


    # Enter a parse tree produced by NyarParser#functionCall.
    def enterFunctionCall(self, ctx:NyarParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by NyarParser#functionCall.
    def exitFunctionCall(self, ctx:NyarParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by NyarParser#arguments.
    def enterArguments(self, ctx:NyarParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by NyarParser#arguments.
    def exitArguments(self, ctx:NyarParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by NyarParser#flowController.
    def enterFlowController(self, ctx:NyarParser.FlowControllerContext):
        pass

    # Exit a parse tree produced by NyarParser#flowController.
    def exitFlowController(self, ctx:NyarParser.FlowControllerContext):
        pass


    # Enter a parse tree produced by NyarParser#typeStatement.
    def enterTypeStatement(self, ctx:NyarParser.TypeStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#typeStatement.
    def exitTypeStatement(self, ctx:NyarParser.TypeStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#typeExpression.
    def enterTypeExpression(self, ctx:NyarParser.TypeExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#typeExpression.
    def exitTypeExpression(self, ctx:NyarParser.TypeExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#typeSuffix.
    def enterTypeSuffix(self, ctx:NyarParser.TypeSuffixContext):
        pass

    # Exit a parse tree produced by NyarParser#typeSuffix.
    def exitTypeSuffix(self, ctx:NyarParser.TypeSuffixContext):
        pass


    # Enter a parse tree produced by NyarParser#AssignValue.
    def enterAssignValue(self, ctx:NyarParser.AssignValueContext):
        pass

    # Exit a parse tree produced by NyarParser#AssignValue.
    def exitAssignValue(self, ctx:NyarParser.AssignValueContext):
        pass


    # Enter a parse tree produced by NyarParser#AssignVariable.
    def enterAssignVariable(self, ctx:NyarParser.AssignVariableContext):
        pass

    # Exit a parse tree produced by NyarParser#AssignVariable.
    def exitAssignVariable(self, ctx:NyarParser.AssignVariableContext):
        pass


    # Enter a parse tree produced by NyarParser#AssignDefer.
    def enterAssignDefer(self, ctx:NyarParser.AssignDeferContext):
        pass

    # Exit a parse tree produced by NyarParser#AssignDefer.
    def exitAssignDefer(self, ctx:NyarParser.AssignDeferContext):
        pass


    # Enter a parse tree produced by NyarParser#AssignFunction.
    def enterAssignFunction(self, ctx:NyarParser.AssignFunctionContext):
        pass

    # Exit a parse tree produced by NyarParser#AssignFunction.
    def exitAssignFunction(self, ctx:NyarParser.AssignFunctionContext):
        pass


    # Enter a parse tree produced by NyarParser#AssignModify.
    def enterAssignModify(self, ctx:NyarParser.AssignModifyContext):
        pass

    # Exit a parse tree produced by NyarParser#AssignModify.
    def exitAssignModify(self, ctx:NyarParser.AssignModifyContext):
        pass


    # Enter a parse tree produced by NyarParser#LHSSingle.
    def enterLHSSingle(self, ctx:NyarParser.LHSSingleContext):
        pass

    # Exit a parse tree produced by NyarParser#LHSSingle.
    def exitLHSSingle(self, ctx:NyarParser.LHSSingleContext):
        pass


    # Enter a parse tree produced by NyarParser#LHSTuple.
    def enterLHSTuple(self, ctx:NyarParser.LHSTupleContext):
        pass

    # Exit a parse tree produced by NyarParser#LHSTuple.
    def exitLHSTuple(self, ctx:NyarParser.LHSTupleContext):
        pass


    # Enter a parse tree produced by NyarParser#LHSMaybeSetter.
    def enterLHSMaybeSetter(self, ctx:NyarParser.LHSMaybeSetterContext):
        pass

    # Exit a parse tree produced by NyarParser#LHSMaybeSetter.
    def exitLHSMaybeSetter(self, ctx:NyarParser.LHSMaybeSetterContext):
        pass


    # Enter a parse tree produced by NyarParser#LHSMaybeIndex.
    def enterLHSMaybeIndex(self, ctx:NyarParser.LHSMaybeIndexContext):
        pass

    # Exit a parse tree produced by NyarParser#LHSMaybeIndex.
    def exitLHSMaybeIndex(self, ctx:NyarParser.LHSMaybeIndexContext):
        pass


    # Enter a parse tree produced by NyarParser#assignRHS.
    def enterAssignRHS(self, ctx:NyarParser.AssignRHSContext):
        pass

    # Exit a parse tree produced by NyarParser#assignRHS.
    def exitAssignRHS(self, ctx:NyarParser.AssignRHSContext):
        pass


    # Enter a parse tree produced by NyarParser#parameter.
    def enterParameter(self, ctx:NyarParser.ParameterContext):
        pass

    # Exit a parse tree produced by NyarParser#parameter.
    def exitParameter(self, ctx:NyarParser.ParameterContext):
        pass


    # Enter a parse tree produced by NyarParser#functionPattern.
    def enterFunctionPattern(self, ctx:NyarParser.FunctionPatternContext):
        pass

    # Exit a parse tree produced by NyarParser#functionPattern.
    def exitFunctionPattern(self, ctx:NyarParser.FunctionPatternContext):
        pass


    # Enter a parse tree produced by NyarParser#maybeSymbol.
    def enterMaybeSymbol(self, ctx:NyarParser.MaybeSymbolContext):
        pass

    # Exit a parse tree produced by NyarParser#maybeSymbol.
    def exitMaybeSymbol(self, ctx:NyarParser.MaybeSymbolContext):
        pass


    # Enter a parse tree produced by NyarParser#MaybeMethod.
    def enterMaybeMethod(self, ctx:NyarParser.MaybeMethodContext):
        pass

    # Exit a parse tree produced by NyarParser#MaybeMethod.
    def exitMaybeMethod(self, ctx:NyarParser.MaybeMethodContext):
        pass


    # Enter a parse tree produced by NyarParser#MustMethod.
    def enterMustMethod(self, ctx:NyarParser.MustMethodContext):
        pass

    # Exit a parse tree produced by NyarParser#MustMethod.
    def exitMustMethod(self, ctx:NyarParser.MustMethodContext):
        pass


    # Enter a parse tree produced by NyarParser#ifStatment.
    def enterIfStatment(self, ctx:NyarParser.IfStatmentContext):
        pass

    # Exit a parse tree produced by NyarParser#ifStatment.
    def exitIfStatment(self, ctx:NyarParser.IfStatmentContext):
        pass


    # Enter a parse tree produced by NyarParser#ifShort.
    def enterIfShort(self, ctx:NyarParser.IfShortContext):
        pass

    # Exit a parse tree produced by NyarParser#ifShort.
    def exitIfShort(self, ctx:NyarParser.IfShortContext):
        pass


    # Enter a parse tree produced by NyarParser#ifSingle.
    def enterIfSingle(self, ctx:NyarParser.IfSingleContext):
        pass

    # Exit a parse tree produced by NyarParser#ifSingle.
    def exitIfSingle(self, ctx:NyarParser.IfSingleContext):
        pass


    # Enter a parse tree produced by NyarParser#ifNested.
    def enterIfNested(self, ctx:NyarParser.IfNestedContext):
        pass

    # Exit a parse tree produced by NyarParser#ifNested.
    def exitIfNested(self, ctx:NyarParser.IfNestedContext):
        pass


    # Enter a parse tree produced by NyarParser#elif.
    def enterElif(self, ctx:NyarParser.ElifContext):
        pass

    # Exit a parse tree produced by NyarParser#elif.
    def exitElif(self, ctx:NyarParser.ElifContext):
        pass


    # Enter a parse tree produced by NyarParser#elseIf.
    def enterElseIf(self, ctx:NyarParser.ElseIfContext):
        pass

    # Exit a parse tree produced by NyarParser#elseIf.
    def exitElseIf(self, ctx:NyarParser.ElseIfContext):
        pass


    # Enter a parse tree produced by NyarParser#switchStatment.
    def enterSwitchStatment(self, ctx:NyarParser.SwitchStatmentContext):
        pass

    # Exit a parse tree produced by NyarParser#switchStatment.
    def exitSwitchStatment(self, ctx:NyarParser.SwitchStatmentContext):
        pass


    # Enter a parse tree produced by NyarParser#caseBody.
    def enterCaseBody(self, ctx:NyarParser.CaseBodyContext):
        pass

    # Exit a parse tree produced by NyarParser#caseBody.
    def exitCaseBody(self, ctx:NyarParser.CaseBodyContext):
        pass


    # Enter a parse tree produced by NyarParser#switchBody.
    def enterSwitchBody(self, ctx:NyarParser.SwitchBodyContext):
        pass

    # Exit a parse tree produced by NyarParser#switchBody.
    def exitSwitchBody(self, ctx:NyarParser.SwitchBodyContext):
        pass


    # Enter a parse tree produced by NyarParser#matchStatment.
    def enterMatchStatment(self, ctx:NyarParser.MatchStatmentContext):
        pass

    # Exit a parse tree produced by NyarParser#matchStatment.
    def exitMatchStatment(self, ctx:NyarParser.MatchStatmentContext):
        pass


    # Enter a parse tree produced by NyarParser#matchBody.
    def enterMatchBody(self, ctx:NyarParser.MatchBodyContext):
        pass

    # Exit a parse tree produced by NyarParser#matchBody.
    def exitMatchBody(self, ctx:NyarParser.MatchBodyContext):
        pass


    # Enter a parse tree produced by NyarParser#condition.
    def enterCondition(self, ctx:NyarParser.ConditionContext):
        pass

    # Exit a parse tree produced by NyarParser#condition.
    def exitCondition(self, ctx:NyarParser.ConditionContext):
        pass


    # Enter a parse tree produced by NyarParser#tryStatement.
    def enterTryStatement(self, ctx:NyarParser.TryStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#tryStatement.
    def exitTryStatement(self, ctx:NyarParser.TryStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#tryCatch.
    def enterTryCatch(self, ctx:NyarParser.TryCatchContext):
        pass

    # Exit a parse tree produced by NyarParser#tryCatch.
    def exitTryCatch(self, ctx:NyarParser.TryCatchContext):
        pass


    # Enter a parse tree produced by NyarParser#tryFinal.
    def enterTryFinal(self, ctx:NyarParser.TryFinalContext):
        pass

    # Exit a parse tree produced by NyarParser#tryFinal.
    def exitTryFinal(self, ctx:NyarParser.TryFinalContext):
        pass


    # Enter a parse tree produced by NyarParser#ForLoop.
    def enterForLoop(self, ctx:NyarParser.ForLoopContext):
        pass

    # Exit a parse tree produced by NyarParser#ForLoop.
    def exitForLoop(self, ctx:NyarParser.ForLoopContext):
        pass


    # Enter a parse tree produced by NyarParser#ForInLoop.
    def enterForInLoop(self, ctx:NyarParser.ForInLoopContext):
        pass

    # Exit a parse tree produced by NyarParser#ForInLoop.
    def exitForInLoop(self, ctx:NyarParser.ForInLoopContext):
        pass


    # Enter a parse tree produced by NyarParser#whileStatment.
    def enterWhileStatment(self, ctx:NyarParser.WhileStatmentContext):
        pass

    # Exit a parse tree produced by NyarParser#whileStatment.
    def exitWhileStatment(self, ctx:NyarParser.WhileStatmentContext):
        pass


    # Enter a parse tree produced by NyarParser#letStatment.
    def enterLetStatment(self, ctx:NyarParser.LetStatmentContext):
        pass

    # Exit a parse tree produced by NyarParser#letStatment.
    def exitLetStatment(self, ctx:NyarParser.LetStatmentContext):
        pass


    # Enter a parse tree produced by NyarParser#classExpression.
    def enterClassExpression(self, ctx:NyarParser.ClassExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#classExpression.
    def exitClassExpression(self, ctx:NyarParser.ClassExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#classStatement.
    def enterClassStatement(self, ctx:NyarParser.ClassStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#classStatement.
    def exitClassStatement(self, ctx:NyarParser.ClassStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#classExtend.
    def enterClassExtend(self, ctx:NyarParser.ClassExtendContext):
        pass

    # Exit a parse tree produced by NyarParser#classExtend.
    def exitClassExtend(self, ctx:NyarParser.ClassExtendContext):
        pass


    # Enter a parse tree produced by NyarParser#classTrait.
    def enterClassTrait(self, ctx:NyarParser.ClassTraitContext):
        pass

    # Exit a parse tree produced by NyarParser#classTrait.
    def exitClassTrait(self, ctx:NyarParser.ClassTraitContext):
        pass


    # Enter a parse tree produced by NyarParser#classController.
    def enterClassController(self, ctx:NyarParser.ClassControllerContext):
        pass

    # Exit a parse tree produced by NyarParser#classController.
    def exitClassController(self, ctx:NyarParser.ClassControllerContext):
        pass


    # Enter a parse tree produced by NyarParser#classEos.
    def enterClassEos(self, ctx:NyarParser.ClassEosContext):
        pass

    # Exit a parse tree produced by NyarParser#classEos.
    def exitClassEos(self, ctx:NyarParser.ClassEosContext):
        pass


    # Enter a parse tree produced by NyarParser#traitStatement.
    def enterTraitStatement(self, ctx:NyarParser.TraitStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#traitStatement.
    def exitTraitStatement(self, ctx:NyarParser.TraitStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#interfaceStatement.
    def enterInterfaceStatement(self, ctx:NyarParser.InterfaceStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#interfaceStatement.
    def exitInterfaceStatement(self, ctx:NyarParser.InterfaceStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#structureStatement.
    def enterStructureStatement(self, ctx:NyarParser.StructureStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#structureStatement.
    def exitStructureStatement(self, ctx:NyarParser.StructureStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#enumerateStatement.
    def enterEnumerateStatement(self, ctx:NyarParser.EnumerateStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#enumerateStatement.
    def exitEnumerateStatement(self, ctx:NyarParser.EnumerateStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#traitExpression.
    def enterTraitExpression(self, ctx:NyarParser.TraitExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#traitExpression.
    def exitTraitExpression(self, ctx:NyarParser.TraitExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#interfaceExpression.
    def enterInterfaceExpression(self, ctx:NyarParser.InterfaceExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#interfaceExpression.
    def exitInterfaceExpression(self, ctx:NyarParser.InterfaceExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#interfaceFunction.
    def enterInterfaceFunction(self, ctx:NyarParser.InterfaceFunctionContext):
        pass

    # Exit a parse tree produced by NyarParser#interfaceFunction.
    def exitInterfaceFunction(self, ctx:NyarParser.InterfaceFunctionContext):
        pass


    # Enter a parse tree produced by NyarParser#interfaceParameters.
    def enterInterfaceParameters(self, ctx:NyarParser.InterfaceParametersContext):
        pass

    # Exit a parse tree produced by NyarParser#interfaceParameters.
    def exitInterfaceParameters(self, ctx:NyarParser.InterfaceParametersContext):
        pass


    # Enter a parse tree produced by NyarParser#structureExpression.
    def enterStructureExpression(self, ctx:NyarParser.StructureExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#structureExpression.
    def exitStructureExpression(self, ctx:NyarParser.StructureExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#enumerateExpression.
    def enterEnumerateExpression(self, ctx:NyarParser.EnumerateExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#enumerateExpression.
    def exitEnumerateExpression(self, ctx:NyarParser.EnumerateExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#enumerateNumber.
    def enterEnumerateNumber(self, ctx:NyarParser.EnumerateNumberContext):
        pass

    # Exit a parse tree produced by NyarParser#enumerateNumber.
    def exitEnumerateNumber(self, ctx:NyarParser.EnumerateNumberContext):
        pass


    # Enter a parse tree produced by NyarParser#data.
    def enterData(self, ctx:NyarParser.DataContext):
        pass

    # Exit a parse tree produced by NyarParser#data.
    def exitData(self, ctx:NyarParser.DataContext):
        pass


    # Enter a parse tree produced by NyarParser#number.
    def enterNumber(self, ctx:NyarParser.NumberContext):
        pass

    # Exit a parse tree produced by NyarParser#number.
    def exitNumber(self, ctx:NyarParser.NumberContext):
        pass


    # Enter a parse tree produced by NyarParser#byteInput.
    def enterByteInput(self, ctx:NyarParser.ByteInputContext):
        pass

    # Exit a parse tree produced by NyarParser#byteInput.
    def exitByteInput(self, ctx:NyarParser.ByteInputContext):
        pass


    # Enter a parse tree produced by NyarParser#index.
    def enterIndex(self, ctx:NyarParser.IndexContext):
        pass

    # Exit a parse tree produced by NyarParser#index.
    def exitIndex(self, ctx:NyarParser.IndexContext):
        pass


    # Enter a parse tree produced by NyarParser#IndexTake.
    def enterIndexTake(self, ctx:NyarParser.IndexTakeContext):
        pass

    # Exit a parse tree produced by NyarParser#IndexTake.
    def exitIndexTake(self, ctx:NyarParser.IndexTakeContext):
        pass


    # Enter a parse tree produced by NyarParser#Index000.
    def enterIndex000(self, ctx:NyarParser.Index000Context):
        pass

    # Exit a parse tree produced by NyarParser#Index000.
    def exitIndex000(self, ctx:NyarParser.Index000Context):
        pass


    # Enter a parse tree produced by NyarParser#Index001.
    def enterIndex001(self, ctx:NyarParser.Index001Context):
        pass

    # Exit a parse tree produced by NyarParser#Index001.
    def exitIndex001(self, ctx:NyarParser.Index001Context):
        pass


    # Enter a parse tree produced by NyarParser#Index010.
    def enterIndex010(self, ctx:NyarParser.Index010Context):
        pass

    # Exit a parse tree produced by NyarParser#Index010.
    def exitIndex010(self, ctx:NyarParser.Index010Context):
        pass


    # Enter a parse tree produced by NyarParser#Index011.
    def enterIndex011(self, ctx:NyarParser.Index011Context):
        pass

    # Exit a parse tree produced by NyarParser#Index011.
    def exitIndex011(self, ctx:NyarParser.Index011Context):
        pass


    # Enter a parse tree produced by NyarParser#Index100.
    def enterIndex100(self, ctx:NyarParser.Index100Context):
        pass

    # Exit a parse tree produced by NyarParser#Index100.
    def exitIndex100(self, ctx:NyarParser.Index100Context):
        pass


    # Enter a parse tree produced by NyarParser#Index101.
    def enterIndex101(self, ctx:NyarParser.Index101Context):
        pass

    # Exit a parse tree produced by NyarParser#Index101.
    def exitIndex101(self, ctx:NyarParser.Index101Context):
        pass


    # Enter a parse tree produced by NyarParser#Index110.
    def enterIndex110(self, ctx:NyarParser.Index110Context):
        pass

    # Exit a parse tree produced by NyarParser#Index110.
    def exitIndex110(self, ctx:NyarParser.Index110Context):
        pass


    # Enter a parse tree produced by NyarParser#Index111.
    def enterIndex111(self, ctx:NyarParser.Index111Context):
        pass

    # Exit a parse tree produced by NyarParser#Index111.
    def exitIndex111(self, ctx:NyarParser.Index111Context):
        pass


    # Enter a parse tree produced by NyarParser#indexTerm.
    def enterIndexTerm(self, ctx:NyarParser.IndexTermContext):
        pass

    # Exit a parse tree produced by NyarParser#indexTerm.
    def exitIndexTerm(self, ctx:NyarParser.IndexTermContext):
        pass


    # Enter a parse tree produced by NyarParser#dict.
    def enterDict(self, ctx:NyarParser.DictContext):
        pass

    # Exit a parse tree produced by NyarParser#dict.
    def exitDict(self, ctx:NyarParser.DictContext):
        pass


    # Enter a parse tree produced by NyarParser#keyValue.
    def enterKeyValue(self, ctx:NyarParser.KeyValueContext):
        pass

    # Exit a parse tree produced by NyarParser#keyValue.
    def exitKeyValue(self, ctx:NyarParser.KeyValueContext):
        pass


    # Enter a parse tree produced by NyarParser#keyValid.
    def enterKeyValid(self, ctx:NyarParser.KeyValidContext):
        pass

    # Exit a parse tree produced by NyarParser#keyValid.
    def exitKeyValid(self, ctx:NyarParser.KeyValidContext):
        pass


    # Enter a parse tree produced by NyarParser#list.
    def enterList(self, ctx:NyarParser.ListContext):
        pass

    # Exit a parse tree produced by NyarParser#list.
    def exitList(self, ctx:NyarParser.ListContext):
        pass


    # Enter a parse tree produced by NyarParser#element.
    def enterElement(self, ctx:NyarParser.ElementContext):
        pass

    # Exit a parse tree produced by NyarParser#element.
    def exitElement(self, ctx:NyarParser.ElementContext):
        pass


    # Enter a parse tree produced by NyarParser#complex.
    def enterComplex(self, ctx:NyarParser.ComplexContext):
        pass

    # Exit a parse tree produced by NyarParser#complex.
    def exitComplex(self, ctx:NyarParser.ComplexContext):
        pass


    # Enter a parse tree produced by NyarParser#decimal.
    def enterDecimal(self, ctx:NyarParser.DecimalContext):
        pass

    # Exit a parse tree produced by NyarParser#decimal.
    def exitDecimal(self, ctx:NyarParser.DecimalContext):
        pass


    # Enter a parse tree produced by NyarParser#integer.
    def enterInteger(self, ctx:NyarParser.IntegerContext):
        pass

    # Exit a parse tree produced by NyarParser#integer.
    def exitInteger(self, ctx:NyarParser.IntegerContext):
        pass


    # Enter a parse tree produced by NyarParser#StringEmpty.
    def enterStringEmpty(self, ctx:NyarParser.StringEmptyContext):
        pass

    # Exit a parse tree produced by NyarParser#StringEmpty.
    def exitStringEmpty(self, ctx:NyarParser.StringEmptyContext):
        pass


    # Enter a parse tree produced by NyarParser#StringEscapeBlock.
    def enterStringEscapeBlock(self, ctx:NyarParser.StringEscapeBlockContext):
        pass

    # Exit a parse tree produced by NyarParser#StringEscapeBlock.
    def exitStringEscapeBlock(self, ctx:NyarParser.StringEscapeBlockContext):
        pass


    # Enter a parse tree produced by NyarParser#StringEscapeSingle.
    def enterStringEscapeSingle(self, ctx:NyarParser.StringEscapeSingleContext):
        pass

    # Exit a parse tree produced by NyarParser#StringEscapeSingle.
    def exitStringEscapeSingle(self, ctx:NyarParser.StringEscapeSingleContext):
        pass


    # Enter a parse tree produced by NyarParser#StringLiteralBlock.
    def enterStringLiteralBlock(self, ctx:NyarParser.StringLiteralBlockContext):
        pass

    # Exit a parse tree produced by NyarParser#StringLiteralBlock.
    def exitStringLiteralBlock(self, ctx:NyarParser.StringLiteralBlockContext):
        pass


    # Enter a parse tree produced by NyarParser#StringLiteralSingle.
    def enterStringLiteralSingle(self, ctx:NyarParser.StringLiteralSingleContext):
        pass

    # Exit a parse tree produced by NyarParser#StringLiteralSingle.
    def exitStringLiteralSingle(self, ctx:NyarParser.StringLiteralSingleContext):
        pass


    # Enter a parse tree produced by NyarParser#special.
    def enterSpecial(self, ctx:NyarParser.SpecialContext):
        pass

    # Exit a parse tree produced by NyarParser#special.
    def exitSpecial(self, ctx:NyarParser.SpecialContext):
        pass


    # Enter a parse tree produced by NyarParser#symbol.
    def enterSymbol(self, ctx:NyarParser.SymbolContext):
        pass

    # Exit a parse tree produced by NyarParser#symbol.
    def exitSymbol(self, ctx:NyarParser.SymbolContext):
        pass


    # Enter a parse tree produced by NyarParser#solt.
    def enterSolt(self, ctx:NyarParser.SoltContext):
        pass

    # Exit a parse tree produced by NyarParser#solt.
    def exitSolt(self, ctx:NyarParser.SoltContext):
        pass


    # Enter a parse tree produced by NyarParser#add_ops.
    def enterAdd_ops(self, ctx:NyarParser.Add_opsContext):
        pass

    # Exit a parse tree produced by NyarParser#add_ops.
    def exitAdd_ops(self, ctx:NyarParser.Add_opsContext):
        pass


    # Enter a parse tree produced by NyarParser#pre_ops.
    def enterPre_ops(self, ctx:NyarParser.Pre_opsContext):
        pass

    # Exit a parse tree produced by NyarParser#pre_ops.
    def exitPre_ops(self, ctx:NyarParser.Pre_opsContext):
        pass


    # Enter a parse tree produced by NyarParser#pst_ops.
    def enterPst_ops(self, ctx:NyarParser.Pst_opsContext):
        pass

    # Exit a parse tree produced by NyarParser#pst_ops.
    def exitPst_ops(self, ctx:NyarParser.Pst_opsContext):
        pass


    # Enter a parse tree produced by NyarParser#bit_ops.
    def enterBit_ops(self, ctx:NyarParser.Bit_opsContext):
        pass

    # Exit a parse tree produced by NyarParser#bit_ops.
    def exitBit_ops(self, ctx:NyarParser.Bit_opsContext):
        pass


    # Enter a parse tree produced by NyarParser#lgk_ops.
    def enterLgk_ops(self, ctx:NyarParser.Lgk_opsContext):
        pass

    # Exit a parse tree produced by NyarParser#lgk_ops.
    def exitLgk_ops(self, ctx:NyarParser.Lgk_opsContext):
        pass


    # Enter a parse tree produced by NyarParser#cpr_ops.
    def enterCpr_ops(self, ctx:NyarParser.Cpr_opsContext):
        pass

    # Exit a parse tree produced by NyarParser#cpr_ops.
    def exitCpr_ops(self, ctx:NyarParser.Cpr_opsContext):
        pass


    # Enter a parse tree produced by NyarParser#pow_ops.
    def enterPow_ops(self, ctx:NyarParser.Pow_opsContext):
        pass

    # Exit a parse tree produced by NyarParser#pow_ops.
    def exitPow_ops(self, ctx:NyarParser.Pow_opsContext):
        pass


    # Enter a parse tree produced by NyarParser#mul_ops.
    def enterMul_ops(self, ctx:NyarParser.Mul_opsContext):
        pass

    # Exit a parse tree produced by NyarParser#mul_ops.
    def exitMul_ops(self, ctx:NyarParser.Mul_opsContext):
        pass


    # Enter a parse tree produced by NyarParser#list_ops.
    def enterList_ops(self, ctx:NyarParser.List_opsContext):
        pass

    # Exit a parse tree produced by NyarParser#list_ops.
    def exitList_ops(self, ctx:NyarParser.List_opsContext):
        pass


    # Enter a parse tree produced by NyarParser#mod_assign.
    def enterMod_assign(self, ctx:NyarParser.Mod_assignContext):
        pass

    # Exit a parse tree produced by NyarParser#mod_assign.
    def exitMod_assign(self, ctx:NyarParser.Mod_assignContext):
        pass


