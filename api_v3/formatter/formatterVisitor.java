// Generated from formatter.g4 by ANTLR 4.9.3
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
	 * Visit a parse tree produced by {@link formatterParser#unused_content}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnused_content(formatterParser.Unused_contentContext ctx);
	/**
	 * Visit a parse tree produced by {@link formatterParser#sectioninfo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSectioninfo(formatterParser.SectioninfoContext ctx);
	/**
	 * Visit a parse tree produced by {@link formatterParser#body}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBody(formatterParser.BodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link formatterParser#question_header_parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuestion_header_parameter(formatterParser.Question_header_parameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link formatterParser#end_answers}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnd_answers(formatterParser.End_answersContext ctx);
}