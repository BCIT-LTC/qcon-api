// Generated from /Users/viresh/Documents/qcon_sept_2021/qcon-api/api_v3/formatter/formatter.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link formatterParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface formatterVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link formatterParser#formatter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFormatter(formatterParser.FormatterContext ctx);
	/**
	 * Visit a parse tree produced by {@link formatterParser#rootheading}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRootheading(formatterParser.RootheadingContext ctx);
	/**
	 * Visit a parse tree produced by {@link formatterParser#rootbody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRootbody(formatterParser.RootbodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link formatterParser#section}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSection(formatterParser.SectionContext ctx);
	/**
	 * Visit a parse tree produced by {@link formatterParser#end_answers_block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnd_answers_block(formatterParser.End_answers_blockContext ctx);
}