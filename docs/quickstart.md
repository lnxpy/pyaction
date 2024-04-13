---
title: Quickstart
description: Hello-world Action Demo
---

In this demo tutorial, we'll get our hands on a simple hello-world action.

## Initialization
Let's generate our action and name it something unique so that we can [publish it to the marketplace](tutorial.md#publishing).

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
🎤 Include workflow testing pipeline
   No

Copying from template version None
 identical  .
    create  pyaction-hello-world
    create  pyaction-hello-world/requirements.txt
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
This is the main Python file that gets executed when the workflow container gets triggered. In this file, we have access to all the input parameters that users have passed to us via `io.read()`. All we need to do is to retrieve the `name` and return the `phrase` that contains the greeting message.

```python title="pyaction-hello-world/main.py" linenums="1"
import sys
from typing import List

from pyaction import io


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    # reading the `name` input parameter
    name = io.read("name")
    message = f"Hello {name}!"

    # writing the `phrase` greeting message to output
    io.write({"phrase": message})

    # Now, people can $echo `phrase`


if __name__ == "__main__":
    main(sys.argv[1:])

```

## Dependencies
Follow this section if your action needs some additional packages installed in order to work.

??? Note "Using a virtual environment"
    This step is optional. If you want to, you can install the dependencies inside a virtualenv other than your global site-packages. Make sure that you've activated your environment.

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

```bash
pip install PACK1 PACK2==v1.2.3 PACK3
```

Finally, don't forget to update the `requirements.txt` file.

```bash
pip freeze >> requirements.txt
```

## Testing Locally
To test our action locally, we need to create a `.env` file in the root path of our action directory. We have to add the `INPUT_NAME` environment variable into it. To make sure that `message` has the exact content that we want, I simply add a temporary `print(message)` line at the end of the `main()` function and delete it after testing my action.

```bash
touch .env
```

```bash title="pyaction-hello-world/.env"
INPUT_NAME=Armita
```

```python title="pyaction-hello-world/main.py" hl_lines="3"
def main(args: List[str]) -> None:
    ...
    print(message)
```

To test the action, run the following command.

```bash
pyaction run
```

And here would be the result.

``` { .bash .no-copy }
Hello Armita!
```

## Deployment & Usage
Stage and commit the changes that you've made.

```bash
git add . && git commit -m 'updated'
```

Tag your current state and push your changes to the repository.

```bash
git tag v0.1.0
git push origin main --tags
```

If you want to self-test your action on each `git push` event, you simply need to answer `y` to the `Include workflow testing pipeline` prompt so it'll create a workflow for your action. Make sure to modify it and update its inputs in `.github/workflows/test.yml`.

!!! Note "This demo is also live.."
    The `pyaction-hello-world` implementation in this tutorial is available [here](https://github.com/lnxpy/pyaction-hello-world). Feel free to look over it.

## Publish to Marketplace
For more information about how you can ship your actions to the GitHub Marketplace, refer to the [publishing tutorial](tutorial.md#publishing) page section.
