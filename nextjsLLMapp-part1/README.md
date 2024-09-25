# nextjsLLMapp

## Installation

Install the LangChain CLI if you haven't yet

```bash
pip install -U langchain-cli
```

## Adding packages

```bash
# adding packages from 
# https://github.com/langchain-ai/langchain/tree/master/templates
langchain app add $PROJECT_NAME

# adding custom GitHub repo packages
langchain app add --repo $OWNER/$REPO
# or with whole git string (supports other git providers):
# langchain app add git+https://github.com/hwchase17/chain-of-verification

# with a custom api mount point (defaults to `/{package_name}`)
langchain app add $PROJECT_NAME --api_path=/my/custom/path/rag
```

Note: you remove packages by their api path

```bash
langchain app remove my/custom/path/rag
```

## Setup LangSmith (Optional)
LangSmith will help us trace, monitor and debug LangChain applications. 
You can sign up for LangSmith [here](https://smith.langchain.com/). 
If you don't have access, you can skip this section


```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

## Launch LangServe

```bash
langchain serve
```

## Running in Docker

This project folder includes a Dockerfile that allows you to easily build and host your LangServe app.

### Building the Image

To build the image, you simply:

```shell
docker build . -t my-langserve-app
```

If you tag your image with something other than `my-langserve-app`,
note it for use in the next step.

### Running the Image Locally

To run the image, you'll need to include any environment variables
necessary for your application.

In the below example, we inject the `OPENAI_API_KEY` environment
variable with the value set in my local environment
(`$OPENAI_API_KEY`)

We also expose port 8080 with the `-p 8080:8080` option.

```shell
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8080:8080 my-langserve-app
```




# Oscar
after having pipx(install scoop first on https://scoop.sh) and peotry, launch `$langchain app new`. Do not use peotry, otherwise, there will be duplicate files created.

Output:
$ langchain app new
What folder would you like to create?: nextjsLLMapp
What package would you like to add? (leave blank to skip):


Success! Created a new LangChain app under "./nextjsLLMapp"!


Next, enter your new app directory by running:

    cd ./nextjsLLMapp

Then add templates with commands like:

    langchain app add extraction-openai-functions
    langchain app add git+ssh://git@github.com/efriis/simple-pirate.git


add a folder called 'tests' and under it a __init__.py file


Running script in a virtual environment
poetry add "package" to install required packages
poetry install
poetry run python filename.py to run the file from poetry virtual environment


## Start FastAPI
In terminal:
* `uvicorn app.server:app --reload`

## Check the app in the LangServe Playground
See this in your browser:
* [http://127.0.0.1:8000/rag/playground/](http://127.0.0.1:8000/rag/playground/)

Use CTRL-C in the terminal to stop it.


## Go to LangSmith to track the operations
* smith.langchain.com



Very important: 
1. It's  always helpful to run the pip install on the requirements.txt brfore updaing the poetry install. Poetry will use the updates from pip
2. everytime you install a package from pip install in your virtual environment, you also need to do poetry add the same package to update from what is in the venv