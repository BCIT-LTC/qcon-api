// Generated from questionparser.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link questionparserParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface questionparserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link questionparserParser#questionparser}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuestionparser(questionparserParser.QuestionparserContext ctx);
	/**
	 * Visit a parse tree produced by {@link questionparserParser#question_wrapper}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuestion_wrapper(questionparserParser.Question_wrapperContext ctx);
	/**
	 * Visit a parse tree produced by {@link questionparserParser#question}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuestion(questionparserParser.QuestionContext ctx);
	/**
	 * Visit a parse tree produced by {@link questionparserParser#fib_part}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFib_part(questionparserParser.Fib_partContext ctx);
	/**
	 * Visit a parse tree produced by {@link questionparserParser#answers}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnswers(questionparserParser.AnswersContext ctx);
	/**
	 * Visit a parse tree produced by {@link questionparserParser#answer_part}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnswer_part(questionparserParser.Answer_partContext ctx);
	/**
	 * Visit a parse tree produced by {@link questionparserParser#correct_answer_part}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCorrect_answer_part(questionparserParser.Correct_answer_partContext ctx);
	/**
	 * Visit a parse tree produced by {@link questionparserParser#trailing_content}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTrailing_content(questionparserParser.Trailing_contentContext ctx);
}