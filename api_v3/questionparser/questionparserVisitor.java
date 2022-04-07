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
}