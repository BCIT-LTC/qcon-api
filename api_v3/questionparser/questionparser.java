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

      public Void visitQuestion(questionparserParser.QuestionContext ctx) {
         Element question = document.createElement("question");
         question.appendChild(document.createTextNode(ctx.getText()));
         root.appendChild(question);
         return null;
      }

      public Void visitFib_question(questionparserParser.Fib_questionContext ctx) {
         Element fib_question = document.createElement("fib_question");
         fib_question.appendChild(document.createTextNode(ctx.getText()));
         root.appendChild(fib_question);
         return null;
      }

      public Void visitAnswer_part(questionparserParser.Answer_partContext ctx) {

         Element answer = document.createElement("answer");
         answer.appendChild(document.createTextNode(ctx.content().getText()));
         root.appendChild(answer);
         return null;
      }

      public Void visitCorrect_answer_part(questionparserParser.Correct_answer_partContext ctx) {
         // System.out.println("Answersss");

         Element correct_answer = document.createElement("correct_answer");
         correct_answer.appendChild(document.createTextNode(ctx.content().getText()));
         root.appendChild(correct_answer);
         return null;
      }

      public Void visitWr_answer(questionparserParser.Wr_answerContext ctx) {
         
         Element wr_answer = document.createElement("wr_answer");
         wr_answer.appendChild(document.createTextNode(ctx.content().getText()));
         root.appendChild(wr_answer);
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