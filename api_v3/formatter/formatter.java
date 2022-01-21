import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.antlr.v4.misc.OrderedHashMap;
import org.antlr.v4.runtime.*;

import org.antlr.v4.runtime.tree.*;

import java.util.Map;

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

import java.io.File; // Import the File class
import java.io.IOException; // Import this class to handle errors

import java.nio.file.*;

public class formatter {

   public static DocumentBuilderFactory documentFactory;
   public static DocumentBuilder documentBuilder;
   public static Document document;
   public static Element root;

   // public formatter() {
   // String publictest = "haihfhf";
   // }
   public static class formatterVisitor extends
         formatterBaseVisitor<Void> {
      // Map<String, String> props = new OrderedHashMap<String, String>();

      int count = 0;

      public Void visitRootheader(formatterParser.RootheaderContext ctx) {
         // props.put("rootheading", ctx.getText());
         // props.put(id, value);
         System.out.println("THIS IS HEADER");
         Element rootheader = document.createElement("rootheader");
         rootheader.appendChild(document.createTextNode(ctx.getText()));
         root.appendChild(rootheader);
         return null; // Java says must return something even when Void
      }

      public Void visitSection(formatterParser.SectionContext ctx) {
         count += 1;
         // System.out.println(Integer.toString(count));
         // props.put(Integer.toString(count), ctx.getText());
         // props.put(id, value);
         System.out.println("SECTION FOUND");

         Element Section = document.createElement("section");
         Section.appendChild(document.createTextNode(ctx.getText()));
         Attr attr = document.createAttribute("id");
         attr.setValue(Integer.toString(count));
         Section.setAttributeNode(attr);

         root.appendChild(Section);

         return null; // Java says must return something even when Void
      }

      public Void visitEnd_answers_block(formatterParser.End_answers_blockContext ctx) {
         // System.out.println(Integer.toString(count));
         // props.put(Integer.toString(count), ctx.getText());
         // props.put(id, value);
         System.out.println("End_answers_block FOUND");

         Element End_answer = document.createElement("endanswer");
         End_answer.appendChild(document.createTextNode(ctx.getText()));
         root.appendChild(End_answer);

         return null; // Java says must return something even when Void
      }
   }

   public static void main(String args[]) {
      // System.out.println("Number of Command Line Argument = "+args.length);
      // System.out.println(String.format("Command Line Argument %d is %s", i,
      // args[i]));
      // for(int i = 0; i< args.length; i++) {
      // System.out.println(String.format("Command Line Argument %d is %s", i,
      // args[i]));
      // }

      if (args.length < 1) {
         System.out.println("filename not provided");
         System.exit(0);
      } else {
         System.out.println(args[0]);
      }

      String javaClassContent = "";
      String inputfile = args[0] + "pandoc_string";

      try {
         Path fileName = Paths.get(inputfile);
         javaClassContent = Files.readString(fileName);
      } catch (IOException e) {
         System.out.println("An error occurred.");
         e.printStackTrace();
      }
      // System.out.println(javaClassContent);
      System.out.println("starting parsing");
      formatterLexer formatterLexer = new formatterLexer(CharStreams.fromString(javaClassContent));
      CommonTokenStream tokens = new CommonTokenStream(formatterLexer);
      formatterParser parser = new formatterParser(tokens);
      // formatterParser.FormatterContext tree = parser.formatter();
      // ParseTreeWalker walker = new ParseTreeWalker();

      ParseTree tree = parser.formatter();

      try {
         documentFactory = DocumentBuilderFactory.newInstance();
         documentBuilder = documentFactory.newDocumentBuilder();
         document = documentBuilder.newDocument();
         root = document.createElement("root");
         document.appendChild(root);
      } catch (ParserConfigurationException pce) {
         System.out.println("An error occurred.");
         pce.printStackTrace();
      }

      formatterVisitor loader = new formatterVisitor();
      loader.visit(tree);

      try {
         // transform the DOM Object to an XML File
         String targetfile = args[0] + "formatter.xml";

         TransformerFactory transformerFactory = TransformerFactory.newInstance();
         Transformer transformer = transformerFactory.newTransformer();
         DOMSource domSource = new DOMSource(document);
         StreamResult streamResult = new StreamResult(new File(targetfile));
         transformer.transform(domSource, streamResult);
         System.out.println("Done creating XML File");
      } catch (TransformerException tfe) {
         tfe.printStackTrace();
      }
      // System.out.println(loader.props);
   }
}