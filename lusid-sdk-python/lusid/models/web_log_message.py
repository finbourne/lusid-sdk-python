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


class WebLogMessage(Model):
    """A log message structured for provision by a web project.

    :param version: The semantic version of the remote application submitting
     the log
    :type version: str
    :param url: The url of the resource from which the message originated
    :type url: str
    :param message: The body of the message
    :type message: str
    :param context: Context as to the occurance of the message
    :type context: str
    :param severity: The severity of the message. Possible values include:
     'Warn', 'Error'
    :type severity: str or ~lusid.models.enum
    :param stacktrace: Any stacktrace that may be relavent
    :type stacktrace: str
    :param browser: Any browser/user-agent/os related context
    :type browser: str
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'context': {'key': 'context', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'str'},
        'stacktrace': {'key': 'stacktrace', 'type': 'str'},
        'browser': {'key': 'browser', 'type': 'str'},
    }

    def __init__(self, version=None, url=None, message=None, context=None, severity=None, stacktrace=None, browser=None):
        super(WebLogMessage, self).__init__()
        self.version = version
        self.url = url
        self.message = message
        self.context = context
        self.severity = severity
        self.stacktrace = stacktrace
        self.browser = browser
