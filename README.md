# qcon-api

`qcon-api` is a question conversion processor that enables accurate text conversion from Word into an LMS import package. It requires the frontend, `qcon-web` to work correctly.

## Quick Start

```bash
docker run -p 8000:8000 registry.dev.ltc.bcit.ca/web-apps/qcon/qcon-api
```

Open your browser to [http://localhost:8000](http://localhost:8000).

## Using `qcon-api`

See [Qcon usage and examples](https://qcon-user-guide.dev.ltc.bcit.ca) for basic information about how to format documents and retrieve packaged files. For full documentation about the Qcon service, including what to do after the conversion to get your questions into your LMS, see the [Qcon User Guide](https://qcon-user-guide.dev.ltc.bcit.ca).

## Developer Guide

```bash
docker compose up --build
```

## Installing `qcon-api`

`qcon-api` can be deployed as a single docker container or as a scalable Kubernetes cluster workload. See the [deployment package](https://issues.ltc.bcit.ca/deployments/) and the following guides for each setup:

* [docker container](https://issues.ltc.bcit.ca/deployments/) - ideal for development
* [Kubernetes workload](https://issues.ltc.bcit.ca/deployments/) - scalable production deployment

## Support, Discussion, and Community

If you need any help with `qcon-api`, please see the [qcon user guide](https://qcon-user-guide.dev.ltc.bcit.ca) or fill-out our [contact form](https://issues.ltc.bcit.ca/web-apps/qcon/qcon-user-guide).

Please submit any `qcon-api` bugs, issues, and feature requests to...[courseproduction@bcit.ca](mailto:courseproduction@bcit.ca) or [bcit-ltc/qcon](https://issues.ltc.bcit.ca/web-apps/qcon/qcon-user-guide).

## License

Copyright (c) 2008-2022 [BCIT LTC](https://bcit.ca/ltc)

This Source Code Form is subject to the terms of the Mozilla Public
License, v2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at <https://mozilla.org/MPL/2.0/>.
