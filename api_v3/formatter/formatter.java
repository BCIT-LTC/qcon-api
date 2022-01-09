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

import java.io.File;  // Import the File class
import java.io.IOException;  // Import this class to handle errors

import java.nio.file.*;

public class formatter {

    public static class formatterVisitor extends
        formatterBaseVisitor<Void>
    {
        Map<String,String> props = new OrderedHashMap<String, String>();
        int count = 0;
      public Void visitRootheading(formatterParser.RootheadingContext ctx) {
            props.put("rootheading",ctx.getText());
            // props.put(id, value);
            return null; // Java says must return something even when Void
        }
      public Void visitSection(formatterParser.SectionContext ctx) {
            count += 1;
            // System.out.println(Integer.toString(count));
            props.put(Integer.toString(count),ctx.getText());
            // props.put(id, value);
            return null; // Java says must return something even when Void
        }
    }


   public static void main(String args[]) {
      // System.out.println("Number of Command Line Argument = "+args.length);
      // System.out.println(String.format("Command Line Argument %d is %s", i, args[i]));		
         // for(int i = 0; i< args.length; i++) {
         //    System.out.println(String.format("Command Line Argument %d is %s", i, args[i]));
         // }      

      if(args.length < 1) {
         System.out.println("filename not provided");
         System.exit(0);
      }	   

      // try{
      //    DocumentBuilderFactory documentFactory = DocumentBuilderFactory.newInstance();      
      //    DocumentBuilder documentBuilder = documentFactory.newDocumentBuilder();      
      //    Document document = documentBuilder.newDocument();
      //    // root element
      //    Element root = document.createElement("company");
      //    document.appendChild(root);
      //    // employee element
      //    Element employee = document.createElement("employee");
      //    root.appendChild(employee);
      //    // set an attribute to staff element
      //    Attr attr = document.createAttribute("id");
      //    attr.setValue("10");
      //    employee.setAttributeNode(attr);
      //    // firstname element
      //    Element firstName = document.createElement("firstname");
      //    firstName.appendChild(document.createTextNode("James"));
      //    employee.appendChild(firstName);
      //    // lastname element
      //    Element lastname = document.createElement("lastname");
      //    lastname.appendChild(document.createTextNode("Harley"));
      //    employee.appendChild(lastname);
      //    // email element
      //    Element email = document.createElement("email");
      //    email.appendChild(document.createTextNode("james@example.org"));
      //    employee.appendChild(email);
      //    // department elements
      //    Element department = document.createElement("department");
      //    department.appendChild(document.createTextNode("Human Resources"));
      //    employee.appendChild(department);
      //    // create the xml file
      //    //transform the DOM Object to an XML File
      //    TransformerFactory transformerFactory = TransformerFactory.newInstance();
      //    Transformer transformer = transformerFactory.newTransformer();
      //    DOMSource domSource = new DOMSource(document);
      //    StreamResult streamResult = new StreamResult(new File(args[0]));
      //    transformer.transform(domSource, streamResult);
      //    System.out.println("Done creating XML File");         
      // }catch (ParserConfigurationException pce) {
      //    System.out.println("An error occurred.");
      //    pce.printStackTrace();
      // }catch (TransformerException tfe) {
      //    tfe.printStackTrace();
      // }

      // ANTLR
      String javaClassContent = "";
      try {
            Path fileName = Paths.get(args[0]);
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

      formatterVisitor loader = new formatterVisitor();
      loader.visit(tree);
      System.out.println(loader.props);

      // try{
      //    // create the xml file
      //    //transform the DOM Object to an XML File
      //    TransformerFactory transformerFactory = TransformerFactory.newInstance();
      //    Transformer transformer = transformerFactory.newTransformer();
      //    DOMSource domSource = new DOMSource(result);
      //    StreamResult streamResult = new StreamResult(new File("./code/temp/test123"));
      //    transformer.transform(domSource, streamResult);
      //    System.out.println("Done creating XML File");
      // }catch (TransformerException tfe) {
      //    tfe.printStackTrace();
      // }
   }
}