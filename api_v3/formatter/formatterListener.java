// Generated from formatter.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link formatterParser}.
 */
public interface formatterListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link formatterParser#formatter}.
	 * @param ctx the parse tree
	 */
	void enterFormatter(formatterParser.FormatterContext ctx);
	/**
	 * Exit a parse tree produced by {@link formatterParser#formatter}.
	 * @param ctx the parse tree
	 */
	void exitFormatter(formatterParser.FormatterContext ctx);
	/**
	 * Enter a parse tree produced by {@link formatterParser#rootheading}.
	 * @param ctx the parse tree
	 */
	void enterRootheading(formatterParser.RootheadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link formatterParser#rootheading}.
	 * @param ctx the parse tree
	 */
	void exitRootheading(formatterParser.RootheadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link formatterParser#rootbody}.
	 * @param ctx the parse tree
	 */
	void enterRootbody(formatterParser.RootbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link formatterParser#rootbody}.
	 * @param ctx the parse tree
	 */
	void exitRootbody(formatterParser.RootbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link formatterParser#section}.
	 * @param ctx the parse tree
	 */
	void enterSection(formatterParser.SectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link formatterParser#section}.
	 * @param ctx the parse tree
	 */
	void exitSection(formatterParser.SectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link formatterParser#end_answers_block}.
	 * @param ctx the parse tree
	 */
	void enterEnd_answers_block(formatterParser.End_answers_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link formatterParser#end_answers_block}.
	 * @param ctx the parse tree
	 */
	void exitEnd_answers_block(formatterParser.End_answers_blockContext ctx);
}