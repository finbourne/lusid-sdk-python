# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FileResponse(Model):
    """Allows a file (represented as a stream) to be returned from an Api call.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar file_stream:
    :vartype file_stream: ~lusid.models.Stream
    :ivar content_type:
    :vartype content_type: str
    :ivar downloaded_filename:
    :vartype downloaded_filename: str
    """

    _validation = {
        'file_stream': {'readonly': True},
        'content_type': {'readonly': True},
        'downloaded_filename': {'readonly': True},
    }

    _attribute_map = {
        'file_stream': {'key': 'fileStream', 'type': 'Stream'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'downloaded_filename': {'key': 'downloadedFilename', 'type': 'str'},
    }

    def __init__(self):
        super(FileResponse, self).__init__()
        self.file_stream = None
        self.content_type = None
        self.downloaded_filename = None
