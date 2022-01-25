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

   public static class formatterVisitor extends
         formatterBaseVisitor<Void> {
      public Void visitRootheader(formatterParser.RootheaderContext ctx) {
         Element rootheader = document.createElement("rootheader");
         rootheader.appendChild(document.createTextNode(ctx.getText()));
         root.appendChild(rootheader);
         return null;
      }

      public Void visitBody(formatterParser.BodyContext ctx) {
         Element body = document.createElement("body");
         body.appendChild(document.createTextNode(ctx.getText()));
         root.appendChild(body);
         return null;
      }
   }

   public static void main(String args[]) {

      if (args.length < 1) {
         System.out.println("formatter: filename not provided");
         System.exit(0);
      } else {
         System.out.println(args[0]);
      }

      String pandocContent = "";
      String inputfile = args[0] + "pandoc_string";

      try {
         Path fileName = Paths.get(inputfile);
         pandocContent = Files.readString(fileName);
      } catch (IOException e) {
         System.out.println("formatter error reading file:" + inputfile);
         e.printStackTrace();
      }
      System.out.println("starting parsing");
      formatterLexer formatterLexer = new formatterLexer(CharStreams.fromString(pandocContent));
      CommonTokenStream tokens = new CommonTokenStream(formatterLexer);
      formatterParser parser = new formatterParser(tokens);

      ParseTree tree = parser.formatter();

      try {
         documentFactory = DocumentBuilderFactory.newInstance();
         documentBuilder = documentFactory.newDocumentBuilder();
         document = documentBuilder.newDocument();
         root = document.createElement("root");
         document.appendChild(root);
      } catch (ParserConfigurationException pce) {
         System.out.println("formatter error reading: " + inputfile);
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
      } catch (TransformerException tfe) {
         System.out.println("formatter error writing: " + args[0]);
         tfe.printStackTrace();
      }
   }
}