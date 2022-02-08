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

public class sectioner {

    public static DocumentBuilderFactory documentFactory;
    public static DocumentBuilder documentBuilder;
    public static Document document;
    public static Element root;

    public static class sectionerVisitor extends
            sectionerBaseVisitor<Void> {

    }

    public static void main(String args[]) {

        if (args.length < 1) {
            System.out.println("sectioner: filename not provided");
            System.exit(0);
        } else {
            System.out.println(args[0]);
        }

        String pandocContent = "";
        String inputfile = args[0] + "pandoc_output.md";

        try {
            Path fileName = Paths.get(inputfile);
            pandocContent = Files.readString(fileName);
        } catch (IOException e) {
            System.out.println("sectioner error reading file:" + inputfile);
            e.printStackTrace();
        }
        System.out.println("starting sectioner");
        sectionerLexer sectionerLexer = new sectionerLexer(CharStreams.fromString(pandocContent));
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
            System.out.println("sectioner error reading: " + inputfile);
            pce.printStackTrace();
        }

        sectionerVisitor loader = new sectionerVisitor();
        loader.visit(tree);

        try {
            // transform the DOM Object to an XML File
            String targetfile = args[0] + "sectioner.xml";

            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource domSource = new DOMSource(document);
            StreamResult streamResult = new StreamResult(new File(targetfile));
            transformer.transform(domSource, streamResult);
        } catch (TransformerException tfe) {
            System.out.println("sectioner error writing: " + args[0]);
            tfe.printStackTrace();
        }
    }
}