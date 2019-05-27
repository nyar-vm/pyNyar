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


    # Enter a parse tree produced by NyarParser#ModuleInclude.
    def enterModuleInclude(self, ctx:NyarParser.ModuleIncludeContext):
        pass

    # Exit a parse tree produced by NyarParser#ModuleInclude.
    def exitModuleInclude(self, ctx:NyarParser.ModuleIncludeContext):
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


    # Enter a parse tree produced by NyarParser#index.
    def enterIndex(self, ctx:NyarParser.IndexContext):
        pass

    # Exit a parse tree produced by NyarParser#index.
    def exitIndex(self, ctx:NyarParser.IndexContext):
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


    # Enter a parse tree produced by NyarParser#indexValid.
    def enterIndexValid(self, ctx:NyarParser.IndexValidContext):
        pass

    # Exit a parse tree produced by NyarParser#indexValid.
    def exitIndexValid(self, ctx:NyarParser.IndexValidContext):
        pass


    # Enter a parse tree produced by NyarParser#IfSingle.
    def enterIfSingle(self, ctx:NyarParser.IfSingleContext):
        pass

    # Exit a parse tree produced by NyarParser#IfSingle.
    def exitIfSingle(self, ctx:NyarParser.IfSingleContext):
        pass


    # Enter a parse tree produced by NyarParser#IfNested.
    def enterIfNested(self, ctx:NyarParser.IfNestedContext):
        pass

    # Exit a parse tree produced by NyarParser#IfNested.
    def exitIfNested(self, ctx:NyarParser.IfNestedContext):
        pass


    # Enter a parse tree produced by NyarParser#SwitchStatement.
    def enterSwitchStatement(self, ctx:NyarParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#SwitchStatement.
    def exitSwitchStatement(self, ctx:NyarParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#MatchStatement.
    def enterMatchStatement(self, ctx:NyarParser.MatchStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#MatchStatement.
    def exitMatchStatement(self, ctx:NyarParser.MatchStatementContext):
        pass


    # Enter a parse tree produced by NyarParser#else.
    def enterElse(self, ctx:NyarParser.ElseContext):
        pass

    # Exit a parse tree produced by NyarParser#else.
    def exitElse(self, ctx:NyarParser.ElseContext):
        pass


    # Enter a parse tree produced by NyarParser#elseIf.
    def enterElseIf(self, ctx:NyarParser.ElseIfContext):
        pass

    # Exit a parse tree produced by NyarParser#elseIf.
    def exitElseIf(self, ctx:NyarParser.ElseIfContext):
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


    # Enter a parse tree produced by NyarParser#catchProduction.
    def enterCatchProduction(self, ctx:NyarParser.CatchProductionContext):
        pass

    # Exit a parse tree produced by NyarParser#catchProduction.
    def exitCatchProduction(self, ctx:NyarParser.CatchProductionContext):
        pass


    # Enter a parse tree produced by NyarParser#finalProduction.
    def enterFinalProduction(self, ctx:NyarParser.FinalProductionContext):
        pass

    # Exit a parse tree produced by NyarParser#finalProduction.
    def exitFinalProduction(self, ctx:NyarParser.FinalProductionContext):
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


    # Enter a parse tree produced by NyarParser#WhileLoop.
    def enterWhileLoop(self, ctx:NyarParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by NyarParser#WhileLoop.
    def exitWhileLoop(self, ctx:NyarParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by NyarParser#DoLoop.
    def enterDoLoop(self, ctx:NyarParser.DoLoopContext):
        pass

    # Exit a parse tree produced by NyarParser#DoLoop.
    def exitDoLoop(self, ctx:NyarParser.DoLoopContext):
        pass


    # Enter a parse tree produced by NyarParser#letStatment.
    def enterLetStatment(self, ctx:NyarParser.LetStatmentContext):
        pass

    # Exit a parse tree produced by NyarParser#letStatment.
    def exitLetStatment(self, ctx:NyarParser.LetStatmentContext):
        pass


    # Enter a parse tree produced by NyarParser#classBody.
    def enterClassBody(self, ctx:NyarParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by NyarParser#classBody.
    def exitClassBody(self, ctx:NyarParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by NyarParser#classExpression.
    def enterClassExpression(self, ctx:NyarParser.ClassExpressionContext):
        pass

    # Exit a parse tree produced by NyarParser#classExpression.
    def exitClassExpression(self, ctx:NyarParser.ClassExpressionContext):
        pass


    # Enter a parse tree produced by NyarParser#traitStatement.
    def enterTraitStatement(self, ctx:NyarParser.TraitStatementContext):
        pass

    # Exit a parse tree produced by NyarParser#traitStatement.
    def exitTraitStatement(self, ctx:NyarParser.TraitStatementContext):
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


    # Enter a parse tree produced by NyarParser#StringLiteral.
    def enterStringLiteral(self, ctx:NyarParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by NyarParser#StringLiteral.
    def exitStringLiteral(self, ctx:NyarParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by NyarParser#StringEmpty.
    def enterStringEmpty(self, ctx:NyarParser.StringEmptyContext):
        pass

    # Exit a parse tree produced by NyarParser#StringEmpty.
    def exitStringEmpty(self, ctx:NyarParser.StringEmptyContext):
        pass


    # Enter a parse tree produced by NyarParser#controller.
    def enterController(self, ctx:NyarParser.ControllerContext):
        pass

    # Exit a parse tree produced by NyarParser#controller.
    def exitController(self, ctx:NyarParser.ControllerContext):
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


