# setting the base-image to alpine
FROM python:{{ cookiecutter.python_version }}-slim

# importing the action
ADD . /action
WORKDIR /action

{%- if cookiecutter.has_dependencies == "y" %}

# installing the requirements
RUN pip install -U pip -r requirements.txt

{%- endif %}

# running the main.py file
ENTRYPOINT [ "python", "main.py" ]
