# setting the base-image to alpine
FROM python:{{ cookiecutter.python_version }}-slim

# importing the action
COPY . /action

{%- if cookiecutter.include_dependencies|lower == "y" %}

# installing the requirements
RUN pip install -U pip -r /action/requirements.txt

{%- endif %}

# running the main.py file
CMD [ "python", "/action/main.py" ]
