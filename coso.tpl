{%- extends 'markdown.tpl' -%}

{%- block any_cell -%}
{{ super() }}
{%- if 'outputs' in cell -%}
{%- for output in cell['outputs'] -%}
{%- if output.output_type == 'display_data' and 'image/png' in output.data -%}
![Image]({{ "data:image/png;base64," + output.data['image/png'] }})
{%- endif -%}
{%- endfor -%}
{%- endif -%}
{%- endblock any_cell -%}
