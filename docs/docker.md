---
title: Qcon-api as a Docker app
---
# Running Qcon-api as a Docker container app

If you're comfortable with the command line, qcon-api is a lightweight document converter that can be run locally as a Docker container.

1. Launch Docker
2. Run the app
    ```
    docker run -p 8000:8000 bcitltc/qcon-api
    ```
3. Open a browser to `localhost:8000`

See the [api routes](api-routes.md) and [usage and examples](usage-examples.md) pages for info about converting documents.