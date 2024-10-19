---
title: Quickstart
description: Hello-world Action Demo
---

In this demo tutorial, we'll get our hands on a simple hello-world action.

## Initialization
Let's generate our action and name it something unique so that we can [publish it to the marketplace](tutorial.md#publishing-in-the-marketplace).

To begin with, once you've installed `pyaction`, generate a base template for the action.

```bash
pyaction init
```

And here would be the prompting for our action called "PyAction Hello World".

``` { .plaintext .no-copy }
🎤 Action name
   PyAction Hello World
🎤 Action's slug
   pyaction-hello-world
🎤 Short description
   This actions says Hello to you!
🎤 Author's name
   John Doe
🎤 Python version
   3.12
🎤 Include workflow testing pipeline
   Yes

Copying from template version None
 identical  .
    create  pyaction-hello-world
    create  pyaction-hello-world/requirements.txt
    create  pyaction-hello-world/.github
    create  pyaction-hello-world/.github/workflows
    create  pyaction-hello-world/.github/workflows/test.yml
    create  pyaction-hello-world/README.md
    create  pyaction-hello-world/action.yml
    create  pyaction-hello-world/Dockerfile
    create  pyaction-hello-world/.dockerignore
    create  pyaction-hello-world/.gitignore
    create  pyaction-hello-world/main.py

✨ Your action `pyaction-hello-world` has been created successfully!
🔗 Visit https://pyaction.imsadra.me/quickstart for a quick demonstration.
```

Change your current directory to `pyaction-hello-world` to begin the development.

```bash
cd pyaction-hello-world/
```

## Development
Once we get our action initialized, it's time to initialize a Git directory so that we can push it to a GitHub repository and track all the changes.

```bash
git init && git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:<username>/pyaction-hello-world.git #(1)
```

1.  Replace `<username>` with your GitHub username/organization.

### Action Configuration (`action.yml`)
This YAML file indicates the basic configurations of our action. We can define our action name, description, and branding there. More importantly, this is where we declare the inputs and outputs of our actions. So head over to the `inputs:..` line where you should define the inputs and outputs.

Since our action has only one `name` input, simply declare it as follows.

```yaml title="pyaction-hello-world/action.yml" hl_lines="14-17"
...

inputs:
  github_token:
    description: The GitHub token
    default: ${{ github.token }}
    required: true

  repository:
    description: The repository name in the form of "<owner>/<repo>"
    default: ${{ github.repository }}
    required: true

  name:
    required: false
    description: the person/thing you want to greet
    default: World
```

!!! Info "There are two inputs already declared.."
    `github_token` and `repository` inputs are already declared within your workflow environment. You can use them to interact with GitHub.

In addition, our action has an output parameter called `phrase` as well. Define it this way at the end of the `action.yml` file.

```yaml
...

outputs:
  phrase:
    description: output message
```

### Main Executing File (`main.py`)
This is the main Python file that gets executed when the workflow container gets triggered. In this file, we have access to all the input parameters that users have passed to us from the `my_action` parameters. All we need to do is to retrieve the `name` and return the `phrase` that contains the greeting message.

```python title="pyaction-hello-world/main.py" linenums="1"
from pyaction import PyAction

workflow = PyAction()


@workflow.action()
def my_action(name: str) -> None:
    workflow.write(
        {
            "phrase": f"Hi {name}!"
        }
    )
```

## Usage & Deployment
In order to use the action within the repository, update the `test.yml` file in the following way.

```yaml title="pyaction-hello-world/.github/workflows/test.yml" linenums="1"
name: Greeting Action

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    name: Running the action
    steps:

      - name: checkout
        uses: actions/checkout@v4

      - name: Greetings
        id: greetings
        uses: ./
        with:
          name: Jane

      - name: Output
        run: echo ${{ steps.greetings.outputs.phrase }}
```

This way, whenever a push event happens to the `main` branch, this pipeline gets triggered and tests the action with the value `Jane` as the `name` input parameter.

Stage and commit the changes that you've made.

```bash
git add . && git commit -m 'updated'
```

Tag your current state and push your changes to the repository.

```bash
git tag v0.1.0
git push origin main --tags
```

!!! Note "This demo is also live.."
    The `pyaction-hello-world` implementation in this tutorial is available [here](https://github.com/lnxpy/pyaction-hello-world). Feel free to look over it.

## Publish to Marketplace
For more information about how you can ship your actions to the GitHub Marketplace, refer to the [publishing tutorial](tutorial.md#publishing-in-the-marketplace) page section.
