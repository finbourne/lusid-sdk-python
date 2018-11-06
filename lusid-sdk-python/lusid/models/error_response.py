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
from msrest.exceptions import HttpOperationError


class ErrorResponse(Model):
    """ErrorResponse.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar status:
    :vartype status: int
    :ivar code: Possible values include: 'Unknown', 'PersonalisationNotFound',
     'NonRecursivePersonalisation', 'VersionNotFound', 'InstrumentNotFound',
     'PropertyNotFound', 'PortfolioRecursionDepth', 'GroupNotFound',
     'PortfolioNotFound', 'PropertySchemaNotFound',
     'PortfolioAncestryNotFound', 'PortfolioWithIdAlreadyExists',
     'OrphanedPortfolio', 'MissingBaseClaims', 'PropertyNotDefined',
     'CannotDeleteSystemProperty', 'CannotModifyImmutablePropertyField',
     'PropertyAlreadyExists', 'InvalidPropertyLifeTime',
     'CannotModifyDefaultDataType', 'GroupAlreadyExists', 'NoSuchDataType',
     'ValidationError', 'LoopDetectedInGroupHierarchy',
     'SubGroupAlreadyExists', 'PriceSourceNotFound', 'AnalyticStoreNotFound',
     'AnalyticStoreAlreadyExists', 'ClientInstrumentAlreadyExists',
     'DuplicateInParameterSet', 'ResultsNotFound', 'OrderFieldNotInResultSet',
     'OperationFailed', 'ElasticSearchError', 'InvalidParameterValue',
     'CommandProcessingFailure', 'EntityStateConstructionFailure',
     'EntityTimelineDoesNotExist', 'EventPublishFailure',
     'InvalidRequestFailure', 'EventPublishUnknown', 'EventQueryFailure',
     'BlobDidNotExistFailure', 'SubSystemRequestFailure',
     'SubSystemConfigurationFailure', 'FailedToDelete',
     'UpsertClientInstrumentFailure', 'IllegalAsAtInterval',
     'IllegalBitemporalQuery', 'InvalidAlternateId',
     'CannotAddSourcePortfolioPropertyExplicitly',
     'EntityAlreadyExistsInGroup', 'EntityWithIdAlreadyExists',
     'PortfolioDetailsDoNotExist', 'PortfolioWithNameAlreadyExists',
     'InvalidTransactions', 'ReferencePortfolioNotFound', 'DuplicateIdFailure',
     'CommandRetrievalFailure', 'DataFilterApplicationFailure', 'SearchFailed',
     'MovementsEngineConfigurationKeyFailure', 'FxRateSourceNotFound',
     'AccrualSourceNotFound', 'EntitlementsFailure', 'InvalidIdentityToken',
     'InvalidRequestHeaders', 'PriceNotFound', 'InvalidSubHoldingKeysProvided',
     'DuplicateSubHoldingKeysProvided', 'CutDefinitionNotFound',
     'CutDefinitionInvalid', 'ServerConfigurationError',
     'InvalidUnitForDataType', 'InvalidTypeForDataType',
     'InvalidValueForDataType', 'UnitNotDefinedForDataType',
     'UnitsNotSupportedOnDataType', 'CannotSpecifyUnitsOnDataType',
     'UnitSchemaInconsistentWithDataType', 'UnitDefinitionNotSpecified',
     'DuplicateUnitDefinitionsSpecified', 'InvalidUnitsDefinition',
     'InvalidInstrumentIdentifierUnit', 'HoldingsAdjustmentDoesNotExist',
     'CouldNotBuildExcelUrl', 'CouldNotGetExcelVersion',
     'InstrumentByCodeNotFound', 'EntitySchemaDoesNotExist',
     'FeatureNotSupportedOnPortfolioType', 'QuoteNotFoundFailure',
     'ReferencePortfolioRequestNotSupported',
     'TransactionPortfolioRequestNotSupported', 'InvalidInstrumentDefinition',
     'InstrumentUpsertFailure', 'TransactionTypeNotFound',
     'TransactionTypeDuplication', 'InvalidPropertyValueAssignment',
     'PortfolioDoesNotExistAtGivenDate'
    :vartype code: str or ~lusid.models.enum
    :ivar message:
    :vartype message: str
    :ivar detailed_message:
    :vartype detailed_message: str
    :param items:
    :type items: list[~lusid.models.ErrorDetailBase]
    :ivar more_info:
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
        'items': {'key': 'items', 'type': '[ErrorDetailBase]'},
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


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)
