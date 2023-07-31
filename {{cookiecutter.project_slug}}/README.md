## {{ cookiecutter.action_name }}

{%- if cookiecutter.include_badges|lower == "y" %}

<img alt="action-badge" src="https://img.shields.io/badge/{{ cookiecutter.action_name }}-white?logo=github-actions&label=GitHub%20Action&labelColor=white&color=0064D7"> <a href="https://github.com/lnxpy/cookiecutter-pyaction"><img alt="cookiecutter-pyaction" src="https://img.shields.io/badge/cookiecutter--pyaction-white?logo=cookiecutter&label=Made%20with&labelColor=white&color=0064D7"></a>

{%- endif %}

{{ cookiecutter.description }}

### Usage
<!-- use code-blocks to indicate how others can use the action -->

{%- if cookiecutter.open_source_license != "notopensource" %}

### License
This action is licensed under some specific terms. Check [here](LICENSE) for more information.

{%- endif %}