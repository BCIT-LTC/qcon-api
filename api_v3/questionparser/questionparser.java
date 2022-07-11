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

      public Void visitQuestion_header_part(questionparserParser.Question_header_partContext ctx) {
         // Read Title if present
         try {
            ctx.TITLE().getText();
            Element title = document.createElement("title");
            title.appendChild(document.createTextNode(ctx.content().getText()));
            root.appendChild(title);
         } catch (Exception e) {
         }
         // Read Points if present
         try {
            ctx.POINTS().getText();
            Element points = document.createElement("points");
            points.appendChild(document.createTextNode(ctx.content().getText()));
            root.appendChild(points);
         } catch (Exception e) {
         }
         // Read Type if present
         try {
            ctx.TYPE().getText();
            Element type = document.createElement("type");
            type.appendChild(document.createTextNode(ctx.content().getText()));
            root.appendChild(type);
         } catch (Exception e) {
         }
         return null;
      }

      public Void visitQuestion_wrapper(questionparserParser.Question_wrapperContext ctx) {
         // Check QUESTION NUMBER for first question
         try {
            // System.out.println(ctx.NUMLIST_PREFIX_ONE().getText());
            ctx.NUMLIST_PREFIX_ONE().getText();
            Element question_number = document.createElement("question_number");
            question_number.appendChild(document.createTextNode(ctx.NUMLIST_PREFIX_ONE().getText()));
            root.appendChild(question_number);
         } catch (Exception e) {
         }

         // Check QUESTION NUMBER for NOT the first question
         try {
            // System.out.println(ctx.NUMLIST_PREFIX_NOT_ONE().getText());
            ctx.NUMLIST_PREFIX_NOT_ONE().getText();
            Element question_number = document.createElement("question_number");
            question_number.appendChild(document.createTextNode(ctx.NUMLIST_PREFIX_NOT_ONE().getText()));
            root.appendChild(question_number);
         } catch (Exception e) {
         }

         // Check QUESTION content including optional feedback
         try {
            // System.out.println(ctx.question().getText());
            ctx.question().getText();
            Element question = document.createElement("question");
            question.appendChild(document.createTextNode(ctx.question().question_part().getText()));
            root.appendChild(question);

            // grab all feedback if multiple were added in question content

            ctx.question().feedback().get(0).content().getText();
            String questionfeedback = "";
            for (int i = 0; i < ctx.question().feedback().size(); i++) {
               questionfeedback = ctx.question().feedback().get(i).content().getText();
            }
            Element question_feedback = document.createElement("question_feedback");
            question_feedback.appendChild(document.createTextNode(questionfeedback));
            root.appendChild(question_feedback);
         } catch (Exception e) {
         }

         // Check FIB content with optional feedback
         try {
            // System.out.println(ctx.question().getText());
            ctx.fib_question().getText();
            Element fib_question = document.createElement("fib_question");
            fib_question.appendChild(document.createTextNode(ctx.fib_question().getText()));
            root.appendChild(fib_question);

            ctx.fib_question().feedback().getText();
            Element fib_question_feedback = document.createElement("question_feedback");
            fib_question_feedback.appendChild(document.createTextNode(ctx.fib_question().feedback().getText()));
            root.appendChild(fib_question_feedback);
         } catch (Exception e) {
         }

         return null;
      }

      public Void visitAnswer_part(questionparserParser.Answer_partContext ctx) {
         try {
            Element index = document.createElement("index");
            index.appendChild(document.createTextNode(ctx.LETTERLIST_PREFIX().getText()));

            Element content = document.createElement("content");
            content.appendChild(document.createTextNode(ctx.content().getText()));

            Element answer = document.createElement("answer");
            answer.appendChild(index);
            answer.appendChild(content);
            answer.setAttribute("correct", "false");
            try {
               ctx.feedback().get(0).getText();
               String answerfeedback = "";
               for (int i = 0; i < ctx.feedback().size(); i++) {
                  answerfeedback = ctx.feedback().get(i).content().getText();
               }
               Element feedback = document.createElement("feedback");
               feedback.appendChild(document.createTextNode(answerfeedback));
               answer.appendChild(feedback);
            } catch (Exception e) {
            }
            root.appendChild(answer);
         } catch (Exception e) {
         }
         return null;
      }

      public Void visitCorrect_answer_part(questionparserParser.Correct_answer_partContext ctx) {
         try {
            Element index = document.createElement("index");
            index.appendChild(document.createTextNode(ctx.CORRECT_ANSWER().getText()));

            Element content = document.createElement("content");
            content.appendChild(document.createTextNode(ctx.content().getText()));

            Element answer = document.createElement("answer");
            answer.appendChild(index);
            answer.appendChild(content);
            answer.setAttribute("correct", "true");
            try {
               ctx.feedback().get(0).getText();
               String answerfeedback = "";
               for (int i = 0; i < ctx.feedback().size(); i++) {
                  answerfeedback = ctx.feedback().get(i).content().getText();
               }
               Element feedback = document.createElement("feedback");
               feedback.appendChild(document.createTextNode(answerfeedback));
               answer.appendChild(feedback);
            } catch (Exception e) {
            }
            root.appendChild(answer);
         } catch (Exception e) {
         }
         return null;
      }

      public Void visitWr_answer(questionparserParser.Wr_answerContext ctx) {
         try {
            Element content = document.createElement("content");
            String wr_answer_text = ctx.content().getText();            
            try {
               wr_answer_text += ctx.answers().getText();
            } catch (Exception e) {
            }
            content.appendChild(document.createTextNode(wr_answer_text));
            Element wr_answer = document.createElement("wr_answer");
            wr_answer.appendChild(content);
            root.appendChild(wr_answer);
         } catch (Exception e) {
         }
         return null;
      }

      public Void visitHint(questionparserParser.HintContext ctx) {
         try {
            Element hint = document.createElement("hint");
            hint.appendChild(document.createTextNode(ctx.content().getText()));
            root.appendChild(hint);
         } catch (Exception e) {
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