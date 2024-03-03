---
title: Demo
description: Hello-world Action Tutorial
---

# Hello-world Demo Action
In this demo tutorial, we'll put our hands on a simple hello-world action in Python.

## Initialization
Let's generate our action and name it something unique so that we can publish it to the marketplace.

!!! warning "Before you start this tutorial.."
    Follow the [setup](index.md/#easy-to-setup) section to make `cookiecutter` available on your machine.


```bash
cookiecutter gh:lnxpy/pyaction
```

And here would be the prompting for my action called "PyAction Hello World".

``` { .plaintext .no-copy }
[1/7] action_name (My Awesome Action): PyAction Hello World
[2/7] action_slug (pyaction-hello-world):
[3/7] description (A short description..): This actions says Hello to you!
[4/7] author_name (John Doe):
[5/7] Select open_source_license
  1 - mit
  2 - bsd
  3 - apache
  4 - gplv3
  5 - notopensource
  Choose from [1/2/3/4/5] (1):
[6/7] include_dependencies (n):
[7/7] include_cicd_testing (n):
pyaction-hello-world is created successfully! ✅
```

| Prompt                 | Description                       | Example                           |
| ---------------------- | --------------------------------- | --------------------------------- |
| `action_name`          | Your action name                  | `PyAction Hello World`            |
| `action_slug`          | Slugged action name               | `<better-left-empty>`             |
| `description`          | Action description                | `This actions says Hello to you!` |
| `author_name`          | Your name                         | `John Doe`                        |
| `open_source_license`  | OS license                        | `1` = (mit)                       |
| `include_dependencies` | Using `requirements.txt`          | `y` = (action has requirements)   |
| `include_cicd_testing` | A workflow for testing the action | `n`                               |


!!! Note "If you want to publish to the marketplace.."
    [GitHub Marketplace](https://github.com/marketplace) is a platform where thousands of actions and GitHub Apps are being hosted and developed. You can also publish your actions and third-party applications there too.

    To do so, make sure that `action_slug` is a unique phrase. Thus, we have to check the following URLs and make sure they all end up being 404 pages.

    * `https://github.com/<action_slug>`
    * `https://github.com/orgs/<action_slug>`
    * `https://github.com/marketplace/actions/<action_slug>`

Here is a tree-look of what have so far. We'll go through the necessary files and develop our action.

```.plaintext
pyaction-hello-world
├── .dockerignore
├── .env
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── action.yml
├── actions
│   ├── __init__.py
│   └── io.py
└── main.py
```

## Development
Once we get our action initialized, it's time to initialize a Git directory so that we can push it to a GitHub repository and track all the changes.

```bash
cd pyaction-hello-world && git init && git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:<username>/pyaction-hello-world.git # (1)
```

1.  Replace `<username>` with your GitHub username or organization.

There are a few files that you need to update in order to make your action properly work. That's what our next sub-sections are about.

### `action.yml`
This YAML file indicates the basic configurations of our action. We can define our action name, description, and branding there. More importantly, this is where we declare the inputs and outputs of our action. So head over to the `# == inputs and outputs ==` line where you should define the inputs and outputs.

Since our action has only one `name` input, simply declare it as follows.

```yaml title="pyaction-hello-world/action.yml" linenums="1"
# == inputs and outputs ==

inputs:
  name:
    required: false
    description: the person/thing you want to greet
    default: World
```

Our action has an output `phrase` too. Define this in the following way.

```yaml linenums="8"
outputs:
  phrase:
    description: output message
```

### `main.py`
This is the main file of our action. In this file, we have access to all the inputs that users have passed to us as well as the outputs that we can send back to the workflow. All we need to do is to retrieve the `name` and return the `phrase` that contains the greeting message.

```python title="pyaction-hello-world/main.py" linenums="1"
import sys
from typing import List

from actions import io


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    # reading the name variable from `with`
    name = io.read("name")
    message = f"Hello {name}!"

    # writing to the buffer
    io.write({"phrase": message})

    # now, people can $echo `phrase`


if __name__ == "__main__":
    main(sys.argv)

```

## Dependencies
Follow this section if your action needs some additional packages installed in order to work.

??? Note "Using a virtual environment"
    This step is optional. If you want to, you can install the dependencies inside a virtual-env other than your global site packages. Make sure that you've activated your environment.

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

```bash
pip install PACK1 PACK2==v1.2.3 PACK3
```

Finally, update the `requirements.txt` file.

```bash
pip freeze > requirements.txt
```

Since the `pyaction-hello-world` doesn't need any requirements, answering `n` to the `include_dependencies` prompt is enough.

!!! Danger "If your action has dependencies.."
    If your action has dependencies, you must answer `y` to the `include_dependencies` prompt or it won't work as expected.

## Testing Locally
To test our action locally, there is a `.env` file included in our action directory. We have to add the `INPUT_NAME` environment variable to it and run our `main.py` file with this variable declared in a session. To make sure that `message` has the exact content that we want, I put a temporary `print(message)` at the end of the `main()` function and drop it after testing my action locally.

```sh title="pyaction-hello-world/.env" hl_lines="3 4"
GITHUB_OUTPUT=/dev/null

INPUT_NAME=Armita
```

```python title="pyaction-hello-world/main.py" hl_lines="3"
def main(args: List[str]) -> None:
    ...
    print(message)
```

In order to test the action, run the following command and you'll see the content of `message`.

```bash
env $(cat .env | xargs) python main.py
```

```plaintext
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

If you want to self-test your action on each `git push` event, you simply need to answer `y` to `include_cicd_testing` prompt so it'll create a workflow for your action. Make sure to modify it and update its inputs in `.github/workflows/test.yml`.

!!! Tip "This demo is also live.."
    The `pyaction-hello-world` implementation in this tutorial is available [here](https://github.com/lnxpy/pyaction-hello-world). Feel free to look over it.

## Publish to Marketplace
For more information about how you can ship your actions to the GitHub Marketplace, refer to the [official docs](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace).
