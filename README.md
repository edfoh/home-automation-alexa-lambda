# home-automation-alexa-lambda

alexa skill hosted in aws lambda that will send alexa intents relating to the television to [home-automation-api](https://github.com/edfoh/home-automation-api)

### Prerequisites

1. npm install -g serverless
2. pip install virtualenv

### VirtualEnv and install dependencies

    virtualenv myenv
    source myenv/bin/activate
    ./install.sh

### Adding new dependencies

- add package name to [requirements.txt](requirements.txt)
- run `./install.sh`
- run `pip freeze > requirements.txt`

### Setting up config

you need to copy the [config.template.yml](config.template.yml) to a local `config.yml`file, which contains the details required to run the application. This file is git-ignored and will not / should not be checked into source control.

- run `cp config.template.yml config.yml`

### Running locally

    sls invoke local --function execute --path ./test.json

### Deploying

`Ensure you have the appropriate AWS credentials set up!`

    sls deploy
