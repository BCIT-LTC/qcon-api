# Basic Usage and Examples

!!! tip "Prerequsites"
    * A formatted Word document [sample.docx](assets/sample.docx)
    * Docker


## Run the app

1. Start up Docker
2. Open up the command line and launch the app:
    ```shell
    docker run -p 8000:8000 bcitltc/qcon-api
    ```
3. Open a browser window and navigate to `localhost:8000`
4. Click the **Upload** banner
5. Click the **Upload** button and select the Word doc you want to convert


# Examples


## Simple multiple-choice questions

Example of the details of the conversion... before/after

Word doc => XML output?


## Written response, Multi-select

More complicated question types with optional parameters (Title, points)


## Fill-in-blank, Matching, Ordering

Complex question types with embedded images, links, and symbols