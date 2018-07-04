from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import unquote
from urllib.request import pathname2url
from urllib.request import url2pathname
import os
from os.path import split, join


def filename_to_uri(path: str) -> str:
    return urljoin('file:', pathname2url(path))


def uri_to_filename(uri: str) -> str:
    if os.name == 'nt':
        # url2pathname does not understand %3A (VS Code's encoding forced on all servers :/)
        filename = url2pathname(urlparse(uri).path).strip('\\')
    else:
        filename = url2pathname(urlparse(uri).path)
    base, name = split(filename)
    return join(base, name.lower())