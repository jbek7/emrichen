import base64
import os
from typing import TextIO

from ..context import Context
from ..template import Template
from ..void import Void
from .base import BaseTag
import glob

class MultiInclude(BaseTag):
    """
    arguments: Path to templates to include
    example: "`!MultiInclude ../*.in.yml`"
    description: Renders the requested templates at this location. Both absolute and relative paths work.
    """

    def enrich(self, context: Context):
        files = self.list_files(context)
        enriched = []
        for f in files:
            include_file = self._open_file(f)
            template = Template.parse(include_file)
            result = template.enrich(context)
            if len(result) == 0:
                continue
            if len(result) > 1:
                raise ValueError('!Include can only include single-document templates')
            entry = result[0]
            if isinstance(entry, list):
               for r in entry :
                   enriched.append(r)
            else:
                enriched.append(entry)

        return enriched

    def list_files(self, context):
        include_path = os.path.join(os.path.dirname(context['__file__']), self.data)
        files = glob.glob(include_path)
        return files

    def _open_file(self, path, mode: str = 'r') -> TextIO:
        return open(path, mode)