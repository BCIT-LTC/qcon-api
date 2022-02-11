import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.antlr.v4.misc.OrderedHashMap;
import org.antlr.v4.runtime.*;

import org.antlr.v4.runtime.tree.*;

import java.util.Map;
import java.util.*;

import java.io.OutputStream;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
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

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.lang.StringBuilder;

public class sectioner {

   public static DocumentBuilderFactory documentFactory;
   public static DocumentBuilder documentBuilder;
   public static Document document;
   public static Element root;

   public static class sectionerVisitor extends
         sectionerBaseVisitor<Void> {

      public Void visitSectioner(sectionerParser.SectionerContext ctx) {
         System.out.println("SECTION FOUND");
         // System.out.println(ctx);
         return null;
      }

      public Void visitSection(sectionerParser.SectionContext ctx) {
         System.out.println("visitSection");
         // System.out.println(ctx.getText());
         return null;
      }

      public Void visitTitle(sectionerParser.TitleContext ctx) {
         System.out.println("visitTitle");
         // System.out.println(ctx.getText());
         return null;
      }

      public Void visitContent(sectionerParser.ContentContext ctx) {
         System.out.println("visitContent");
         return null;
      }
   }

   public static void serializeDocument(Document document, OutputStream os) {
      try {
         TransformerFactory tFactory = TransformerFactory.newInstance();
         Transformer transformer = tFactory.newTransformer();
         transformer.setOutputProperty(OutputKeys.INDENT, "yes");

         DOMSource source = new DOMSource(document);
         StreamResult result = new StreamResult(os);
         transformer.transform(source, result);
      } catch (TransformerException e) {
         e.printStackTrace();
      }
   }

   public static void printDocument(Document document) {
      serializeDocument(document, System.out);
   }

   public static String readinput() {
      InputStreamReader reader = new InputStreamReader(System.in);
      char[] buffer = new char[1000];
      StringBuilder sb = new StringBuilder();
      String input = "";
      int count;
      try {
         while ((count = reader.read(buffer)) != -1) {
            sb.append(buffer, 0, count);
         }
         input = sb.toString();
      } catch (Exception e) {
         e.printStackTrace();
      }
      return input;
   }

   public static void main(String args[]) {

      // String Content = readinput();

      String Content = "";
      String inputfile = "file.md";

      try {
         Path fileName = Paths.get(inputfile);
         Content = Files.readString(fileName);
      } catch (IOException e) {
         System.out.println("formatter error reading file:" + inputfile);
         e.printStackTrace();
      }

      // System.out.println(Content);

      sectionerLexer sectionerLexer = new sectionerLexer(CharStreams.fromString(Content));
      CommonTokenStream tokens = new CommonTokenStream(sectionerLexer);
      sectionerParser parser = new sectionerParser(tokens);

      ParseTree tree = parser.sectioner();

      try {
         documentFactory = DocumentBuilderFactory.newInstance();
         documentBuilder = documentFactory.newDocumentBuilder();
         document = documentBuilder.newDocument();
         root = document.createElement("root");
         document.appendChild(root);
      } catch (ParserConfigurationException pce) {
         pce.printStackTrace();
      }

      sectionerVisitor loader = new sectionerVisitor();
      loader.visit(tree);

      // printDocument(document);

   }
}