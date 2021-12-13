import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.antlr.v4.runtime.*;

import java.io.File;  // Import the File class
import java.io.IOException;  // Import this class to handle errors

import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;

public class formatter {
   public static void main(String args[]) {

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