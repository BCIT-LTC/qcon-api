import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.antlr.v4.runtime.*;

import javax.xml.*;

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

// import java.io.File;  // Import the File class
import java.io.IOException;  // Import this class to handle errors

import java.nio.file.*;
// import java.nio.file.Paths;
// import java.nio.file.Path;

public class formatter {
   public static void main(String args[]) {

      try{
         DocumentBuilderFactory documentFactory = DocumentBuilderFactory.newInstance();      
         DocumentBuilder documentBuilder = documentFactory.newDocumentBuilder();      
         Document document = documentBuilder.newDocument();
         
      }catch (ParserConfigurationException pce) {
         System.out.println("An error occurred.");
         pce.printStackTrace();
      }

      // System.out.print(myString);

      // ANTLR
      String javaClassContent = "";
      try {
            Path fileName = Paths.get("long.txt");
            javaClassContent = Files.readString(fileName);
      } catch (IOException e) {
         System.out.println("An error occurred.");
         e.printStackTrace();
      }
      System.out.println(javaClassContent);
      formatterLexer formatterLexer = new formatterLexer(CharStreams.fromString(javaClassContent));
      CommonTokenStream tokens = new CommonTokenStream(formatterLexer);
      formatterParser parser = new formatterParser(tokens);
      formatterParser.FormatterContext tree = parser.formatter();
      ParseTreeWalker walker = new ParseTreeWalker();
      formatterBaseListener listener= new formatterBaseListener();
      walker.walk(listener, tree);



      // walker.walk(printer, tree)
      // result = printer.get_results()
      // assertThat(listener.getErrors().size(), is(1));
      // assertThat(listener.getErrors().get(0),
      // is("Method DoSomething is uppercased!"));
   }

}