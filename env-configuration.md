# ENV's and SECRETS

## DEV
### DEV .env (inside image)
# Default environment variables
API_HOST="api.local"
APP_PORT="8000"
APP_DESCRIPTION=""
APP_TAGLINE=""
#### --- (added by DEV pipeline)
VERSION=$VERSION_TAG
BUILD_HASH=$CI_COMMIT_SHA
BUILD_SHORT_SHA=$CI_COMMIT_SHORT_SHA
BUILD_TIMESTAMP=$BUILD_DATE
#### --- (injected by downward API)
CLUSTER_ENV=""
BUILD_ENV=""


### DEV .secrets (inside image)
# Default app credentials (insecure)
ADMIN_USERNAME="admin"
ADMIN_PASSWORD="admin"
API_KEY="2222222222222222222222222222222222222222"
DJANGO_SECRET_KEY="d8&z=vqy5b#lu0=an1xx9b_7n480af=-gdnqwqvtrs&d6el9=("


### DEV image labels (outside image)
#### --- (added by DEV pipeline; not added by local build engine)
org.opencontainers.image.version=$VERSION_TAG
org.opencontainers.image.revision=$CI_COMMIT_SHA
org.opencontainers.image.source=$CI_PROJECT_URL
version=$VERSION_TAG
build_hash=$CI_COMMIT_SHA
build_short_sha=$CI_COMMIT_SHORT_SHA
build_env=$BUILD_ENV
build_timestamp=$BUILD_DATE
pipeline_timestamp=$CI_PIPELINE_CREATED_AT
app_description=
app_tagline=


### DEV k8s deployment annotations (outside image)
#### --- (added by DEV pipeline)
VERSION: $VERSION_TAG
BUILD_ENV: $BUILD_ENV
PIPELINE_TIMESTAMP: $CI_PIPELINE_CREATED_AT
CLUSTER_ENV: $CLUSTER_ENV
app.gitlab.com/app: $CI_PROJECT_PATH_SLUG           # Enables GitLab dashboard
app.gitlab.com/env: $CI_ENVIRONMENT_SLUG
field.cattle.io/projectId: $CLUSTER_ID:$PROJECT_ID  # Adds namespace to default Rancher project

### OTHER DEV ENV VARS USED IN PIPELINE
NAMESPACE_NAME=$NAMESPACE_NAME  # Eg. "qcon" or "qcon-api"
TLS_SECRET_NAME=""              # Eg. "star-dev-ltc-bcit-ca"
CI_HOST: $CI_HOST               # Eg. "stable.dev.ltc.bcit.ca"


## STAGING
### STAGING .env
API_HOST="https://latest.dev.ltc.bcit.ca/qcon-api"




### STAGING .secrets


### STAGING image labels (outside image)


### STAGING k8s deployment annotations (outside image)



### PROD .env
API_HOST="https://stable.dev.ltc.bcit.ca/qcon"


## PROD
### PROD .env


### PROD image labels (outside image)


### PROD k8s deployment annotations (outside image)

