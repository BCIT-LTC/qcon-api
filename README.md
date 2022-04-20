# Qcon-api

[![pipeline status](https://issues.ltc.bcit.ca/web-apps/qcon/qcon-api/badges/master/pipeline.svg)](https://issues.ltc.bcit.ca/web-apps/qcon/qcon-api/-/commits/master)
[![Gitter](https://badges.gitter.im/BCIT-LTC/qcon.svg)](https://gitter.im/BCIT-LTC/qcon?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
<!--[![Docker Pulls]()-->

Qcon-api is a question conversion processor that enables accurate text conversion from Word into an LMS import package.

## Latest Release

* Latest - v2.0.3-alpha - `bcitltc/qcon-api:latest` - Read the full [release notes]().
* Stable - v2.0.0 - `bcitltc/qcon-api:stable` - Read the full [release notes]().

## Quick Start

```bash
docker run -p 8000:8000 bcitltc/qcon-api
```

Open your browser to **<https://localhost:8000>**

## Using Qcon-api

See the Qcon-api [usage and examples](docs/usage-examples.md) page for basic information about how to format documents and retrieve packaged files. For full documentation about the Qcon service, including what to do after the conversion to get your questions into your LMS, see the [Qcon User Guide](https://issues.ltc.bcit.ca/web-apps/qcon/qcon-user-guide).

## Developer Guide

See [getting started](docs/getting-started.md).

## Installation

Qcon-api can be deployed as a single docker container or as a scalable Kubernetes cluster workload. Please refer to the following guides for each setup:

* [docker container](docs/docker.md) - ideal for development
* [Kubernetes workload](docs/kubernetes.md) - scalable production deployment

## Support, Discussion, and Community

If you need any help with Qcon-api, please join us on the [BCITLTC/Qcon](https://gitter.im/BCIT-LTC/qcon) Gitter channel or fill-out our [contact form](https://issues.ltc.bcit.ca/web-apps/qcon/qcon-user-guide).

Please submit any **Qcon-api** bugs, issues, and feature requests to [bcit-ltc/qcon](https://issues.ltc.bcit.ca/web-apps/qcon/qcon-user-guide).

## License

Copyright (c) 2008-2020 [BCIT LTC](https://bcit.ca/ltc)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at <https://mozilla.org/MPL/2.0/>.
