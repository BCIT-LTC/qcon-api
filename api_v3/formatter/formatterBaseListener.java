// Generated from formatter.g4 by ANTLR 4.8

import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.TerminalNode;


import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

/**
 * This class provides an empty implementation of {@link formatterListener},
 * which can be extended to create a listener which only needs to handle a subset
 * of the available methods.
 */
public class formatterBaseListener implements formatterListener {

	DocumentBuilderFactory documentFactory;      
	DocumentBuilder documentBuilder;      
	Document document;
	Element root;

	public formatterBaseListener() {
		try{
			documentFactory = DocumentBuilderFactory.newInstance();      
			documentBuilder = documentFactory.newDocumentBuilder();      
			document = documentBuilder.newDocument();		
			// root element
			root = document.createElement("root");
			document.appendChild(root);
		}catch (ParserConfigurationException pce) {
         System.out.println("An error occurred.");
         pce.printStackTrace();
		}
	}

	public Document get_result() {
		// String newvalue;
    	return document;
  	}

	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterFormatter(formatterParser.FormatterContext ctx) {
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitFormatter(formatterParser.FormatterContext ctx) { 
	}
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterRootheading(formatterParser.RootheadingContext ctx) {
		
	 }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitRootheading(formatterParser.RootheadingContext ctx) { 
		System.out.println("rootheading found " + ctx.getText());
		Element rootheading = document.createElement("rootheading");
		rootheading.appendChild(document.createTextNode(ctx.getText()));
		root.appendChild(rootheading);
	}
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterRootbody(formatterParser.RootbodyContext ctx) { }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitRootbody(formatterParser.RootbodyContext ctx) { }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterSection(formatterParser.SectionContext ctx) { 
	}
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitSection(formatterParser.SectionContext ctx) { 
		Element section = document.createElement("section");
		section.appendChild(document.createTextNode(ctx.getText()));
		root.appendChild(section);
	}
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterEnd_answers_block(formatterParser.End_answers_blockContext ctx) { }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitEnd_answers_block(formatterParser.End_answers_blockContext ctx) { 
		Element endanswer = document.createElement("endanswer");
		endanswer.appendChild(document.createTextNode(ctx.getText()));
		root.appendChild(endanswer);
	}

	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void enterEveryRule(ParserRuleContext ctx) { }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void exitEveryRule(ParserRuleContext ctx) { }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void visitTerminal(TerminalNode node) { }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation does nothing.</p>
	 */
	@Override public void visitErrorNode(ErrorNode node) { }
}