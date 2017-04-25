# home-automation-alexa-lambda

alexa skill hosted in aws lambda that will send alexa intents relating to the television to [home-automation-api](https://github.com/edfoh/home-automation-api)

### Prerequisites

- npm install -g serverless
- Python 2.7 ([here](https://www.python.org/download/releases/2.7/) OR [via homebrew](https://brew.sh/))
- pip ([here](https://pip.pypa.io/en/stable/installing/) OR [via homebrew](https://brew.sh/))
- `pip install pip-tools` [pip-tools](https://github.com/nvie/pip-tools)
- `pip install virtualenv` [virtualenv](https://virtualenv.pypa.io/en/stable/)

### VirtualEnv and install dependencies

    virtualenv myenv
    source myenv/bin/activate
    pip install pip-tools
    ./install.sh

#### Add a python lib

1. Add it to the [requirements.in](requirements.in) file
1. Run `./install.sh`

#### Remove a python lib

1. Run `rm -rf lib`
1. Remove it from the [requirements.in](requirements.in) file
1. Run `./install.sh`

### Setting up config

you need to copy the [config.template.yml](config.template.yml) to a local `config.yml`file, which contains the details required to run the application. This file is git-ignored and will not / should not be checked into source control.

- run `cp config.template.yml config.yml`

### Running locally

    sls invoke local --function execute --path ./test.json

### Deploying

`Ensure you have the appropriate AWS credentials set up!`

    sls deploy
