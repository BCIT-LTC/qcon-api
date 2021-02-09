# Qcon
 [![pipeline status](https://issues.ltc.bcit.ca/prototypes/qcon/badges/master/pipeline.svg)](https://issues.ltc.bcit.ca/prototypes/qcon/-/commits/master) 
[![Gitter](https://badges.gitter.im/BCIT-LTC/qcon.svg)](https://gitter.im/BCIT-LTC/qcon?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
<!--[![Docker Pulls]()-->

Qcon is an open source project that converts assessment questions from Word into a format that can be uploaded into an LMS like Brightspace, Moodle, or Canvas. Qcon makes it easy to update and manage quizzes and assessment questions using a familiar MS Word interface.

## Latest Release

* Latest - v2.0.3-alpha - `bcitltc/qcon:latest` - Read the full release [notes]().
* Stable - v2.0.0 - `bcitltc/qcon:stable` - Read the full release [notes]().

## Quick Start

    docker run -d --restart=unless-stopped -p 80:80 -p 443:443 --privileged bcitltc/qcon

Open your browser to https://localhost:8000

## Development Env Requirements
* Skaffold
* Kubernetes-cli (kubectl, kustomize)
* Docker
* Kustomize

* Setup a sane default repo
`skaffold config set default-repo registry.dev.ltc.bcit.ca/web-apps/qcon`

* Configure your Kubernetes context. This script merges config files when adding new contexts:
`KUBECONFIG=file1:file2:file3 kubectl config view \
    --merge --flatten > out.txt`

## Installation

Qcon can be deployed as a single docker container or as a scalable Kubernetes cluster workload. Please refer to the following guides for each setup:
* [docker container](https://registry.dev.ltc.bcit.ca/prototypes/qcon:latest) - ideal for development
* [Kubernetes workload]() - scalable production deployment



## Using Qcon

See the [Qcon Documentation] for information about how to format documents, retrieve files, and steps to take post-conversion to get your questions into your LMS.

## Support, Discussion, and Community
If you need any help with Qcon, please join us on the [BCITLTC/Qcon](https://gitter.im/BCIT-LTC/qcon) Gitter channel or fill-out our [contact form]().

Please submit any **Qcon** bugs, issues, and feature requests to [bcit-ltc/qcon](//github.com/bcit-ltc/qcon/issues).

# License

Copyright (c) 2008-2020 [BCIT LTC](https://bcit.ca/ltc)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
