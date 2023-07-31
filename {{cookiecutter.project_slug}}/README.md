## {{ cookiecutter.action_name }}
{{ cookiecutter.description }}

{%- if cookiecutter.include_badge|lower == "y" %}

<img alt="Static Badge" src="https://img.shields.io/badge/{{ cookiecutter.action_name }}-white?logo=github-actions&label=GitHub%20Action&labelColor=white&color=0064D7">

{%- endif %}

### Usage
<!-- use code-blocks to indicate how others can use the action -->

{%- if cookiecutter.open_source_license != "notopensource" %}

### License
This action is licensed under the terms of [{{ cookiecutter.open_source_license }}](LICENSE) license.

{%- endif %}