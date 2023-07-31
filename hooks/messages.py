TEMPLATE_CREATION = "\n\r{project_slug} is created successfully! \U0001F525"

FURTHER_INSTRUCTIONS = """
Now you can start working on your action:
    $ cd {project_slug} && git init

Make a commit and upload initial code to GitHub:
    $ git add .
    $ git commit -m "Initial commit"
    $ git tag v{version}
    $ git branch -M main
    $ git remote add origin https://github.com/{github_username}/{project_slug}.git
    $ git push -u origin main --tags"""
