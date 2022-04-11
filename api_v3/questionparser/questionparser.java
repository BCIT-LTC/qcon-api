import org.antlr.v4.runtime.*;

import org.antlr.v4.runtime.tree.*;

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

public class questionparser {

   public static DocumentBuilderFactory documentFactory;
   public static DocumentBuilder documentBuilder;
   public static Document document;
   public static Element root;

   public static class questionparserVisitor extends
         questionparserBaseVisitor<Void> {
      public Void visitquestionparser(questionparserParser.questionparserContext ctx) {

         int numberofquestions = ctx.questions().size();

         // CHECK IF FIRST QUESTION WAS FOUND
         try {
            Element question = document.createElement("question");
            question.setAttribute("id", Integer.toString(0));

            Element content = document.createElement("content");
            content.appendChild(document.createTextNode(ctx.first_question().getText()));
            question.appendChild(content);
            root.appendChild(question);

         } catch (Exception e) {
         }

         for (int i = 0; i < numberofquestions; i++) {
            Element question = document.createElement("question");
            question.setAttribute("id", Integer.toString(i + 1));

            // CHECK IF QUESTION HEADER EXISTS
            try {
               Element questionheader = document.createElement("question_header");
               questionheader.appendChild(document.createTextNode(ctx.questions().get(i).question_header().getText()));
               question.appendChild(questionheader);

            } catch (Exception e) {
            }

            // GET QUESTION NUMBER

            try {
               Element question_start = document.createElement("question_start");
               question_start
                     .appendChild(document.createTextNode(ctx.questions().get(i).START_OF_QUESTION().getText()));
               question.appendChild(question_start);

            } catch (Exception e) {
            }

            // GET QUESTION CONTENT

            try {
               Element content = document.createElement("content");
               content
                     .appendChild(document.createTextNode(ctx.questions().get(i).content().getText()));
               question.appendChild(content);

            } catch (Exception e) {
            }

            root.appendChild(question);
         }

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

      String Content = null;

      if (args.length == 0) {
         Content = readinput();
      } else {
         try {
            Path fileName = Paths.get(args[0]);
            Content = Files.readString(fileName);
         } catch (IOException e) {
            System.out.println("questionparser error reading file:" + args[0]);
            e.printStackTrace();
         }
      }

      questionparserLexer questionparserLexer = new questionparserLexer(CharStreams.fromString(Content));
      CommonTokenStream tokens = new CommonTokenStream(questionparserLexer);
      questionparserParser parser = new questionparserParser(tokens);

      ParseTree tree = parser.questionparser();

      try {
         documentFactory = DocumentBuilderFactory.newInstance();
         documentBuilder = documentFactory.newDocumentBuilder();
         document = documentBuilder.newDocument();
         root = document.createElement("root");
         document.appendChild(root);
      } catch (ParserConfigurationException pce) {
         pce.printStackTrace();
      }

      questionparserVisitor loader = new questionparserVisitor();
      loader.visit(tree);

      printDocument(document);

   }
}