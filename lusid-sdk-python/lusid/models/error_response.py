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


class ErrorResponse(Model):
    """ErrorResponse.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar status: The status code that will be returned to the client
    :vartype status: int
    :ivar code: The Finbourne specific error-code that encapsulates the
     specific issue encountered. Possible values include:
     'PersonalisationNotFound', 'NonRecursivePersonalisation',
     'VersionNotFound', 'SecurityNotFound', 'SecurityByCodeNotFound',
     'PropertyNotFound', 'PortfolioRecursionDepth', 'GroupNotFound',
     'PortfolioNotFound', 'PropertySchemaNotFound',
     'PortfolioWithIdAlreadyExists', 'OrphanedPortfolio', 'MissingBaseClaims',
     'PropertyNotDefined', 'CannotDeleteSystemProperty',
     'CannotModifyImmutablePropertyField', 'PropertyAlreadyExists',
     'InvalidPropertyLifeTime', 'CannotModifyDefaultPropertyFormat',
     'GroupAlreadyExists', 'NoSuchPropertyDataFormat', 'ValidationError',
     'LoopDetectedInGroupHierarchy', 'SubGroupAlreadyExists',
     'PriceSourceNotFound', 'AnalyticStoreNotFound',
     'AnalyticStoreAlreadyExists', 'ClientSecurityAlreadyExists',
     'DuplicateInParameterSet', 'ResultsNotFound', 'OrderFieldNotInResultSet',
     'OperationFailed', 'ElasticSearchError', 'InvalidParameterValue',
     'ServerConfigurationError', 'CommandProcessingFailure',
     'EntityStateConstructionFailure', 'EntityTimelineDoesNotExist',
     'EventPublishFailure', 'InvalidRequestFailure', 'EventPublishUnknown',
     'EventQueryFailure', 'BlobDidNotExistFailure', 'SubSystemRequestFailure',
     'SubSystemConfigurationFailure', 'FailedToDelete',
     'UpsertClientSecurityFailure', 'IllegalAsAtInterval',
     'IllegalBitemporalQuery', 'InvalidAlternateId',
     'CannotAddSourcePortfolioPropertyExplicitly',
     'EntityAlreadyExistsInGroup', 'EntityWithIdAlreadyExists',
     'PortfolioDetailsDoNotExist', 'PortfolioWithNameAlreadyExists',
     'InvalidTrades', 'ReferencePortfolioNotFound', 'DuplicateIdFailure',
     'CommandRetrievalFailure', 'DataFilterApplicationFailure', 'SearchFailed',
     'MovementsEngineConfigurationKeyFailure', 'Unknown'
    :vartype code: str or ~lusid.models.enum
    :ivar message: The non-technical-user friendly message describing the
     error and how it might be remedied.
    :vartype message: str
    :ivar detailed_message: A technical error message that contains the
     details of the issue and how it might be fixed.
    :vartype detailed_message: str
    :param items: Any action specific item specific sub errors (e.g. per-trade
     validation errors)
    :type items: list[~lusid.models.ErrorDetail]
    :ivar more_info: A link to the endpoint that can provide the dev with more
     information about that class of error.
    :vartype more_info: str
    """

    _validation = {
        'status': {'readonly': True},
        'code': {'readonly': True},
        'message': {'readonly': True},
        'detailed_message': {'readonly': True},
        'more_info': {'readonly': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'detailed_message': {'key': 'detailedMessage', 'type': 'str'},
        'items': {'key': 'items', 'type': '[ErrorDetail]'},
        'more_info': {'key': 'moreInfo', 'type': 'str'},
    }

    def __init__(self, items=None):
        super(ErrorResponse, self).__init__()
        self.status = None
        self.code = None
        self.message = None
        self.detailed_message = None
        self.items = items
        self.more_info = None
