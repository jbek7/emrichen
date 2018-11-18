import json

import pyaml
import yaml


def render_json(data):
    if not isinstance(data, list) or len(data) != 1:
        raise TypeError(
            "JSON output can only handle a single document. "
            "A common cause for this error is trying to render a multi-document "
            "YAML template into JSON. If you use a YAML template with JSON output, "
            "it may only contain a single document. !Defaults documents do not count "
            "as they are stripped from the output."
        )

    return json.dumps(data[0], ensure_ascii=False, indent=2)


RENDERERS = {
    'yaml': lambda data: yaml.dump_all(data, Dumper=pyaml.PrettyYAMLDumper, default_flow_style=False),
    'json': render_json,
}


def render(data, format):
    if format in RENDERERS:
        return RENDERERS[format](data)
    else:
        raise ValueError('No renderer for format {format}'.format(format=format))
