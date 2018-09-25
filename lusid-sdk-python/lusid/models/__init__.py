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

from .create_analytic_store_request import CreateAnalyticStoreRequest
from .analytic_store_key_dto import AnalyticStoreKeyDto
from .link import Link
from .analytic_store_dto import AnalyticStoreDto
from .error_detail_base import ErrorDetailBase
from .error_response import ErrorResponse, ErrorResponseException
from .resource_list_of_analytic_store_key_dto import ResourceListOfAnalyticStoreKeyDto
from .deleted_entity_response import DeletedEntityResponse
from .instrument_analytic_data_dto import InstrumentAnalyticDataDto
from .corporate_action_transition_component_dto import CorporateActionTransitionComponentDto
from .corporate_action_transition_dto import CorporateActionTransitionDto
from .upsert_corporate_action_request import UpsertCorporateActionRequest
from .resource_id import ResourceId
from .corporate_action_event_dto import CorporateActionEventDto
from .error_detail import ErrorDetail
from .try_upsert_corporate_actions_dto import TryUpsertCorporateActionsDto
from .create_unit_definition import CreateUnitDefinition
from .create_data_type_request import CreateDataTypeRequest
from .iunit_definition_dto import IUnitDefinitionDto
from .data_type_dto import DataTypeDto
from .update_data_type_request import UpdateDataTypeRequest
from .resource_list_of_data_type_dto import ResourceListOfDataTypeDto
from .create_derived_transaction_portfolio_request import CreateDerivedTransactionPortfolioRequest
from .version_dto import VersionDto
from .portfolio_dto import PortfolioDto
from .portfolio_group_dto import PortfolioGroupDto
from .resource_list_of_portfolio_group_dto import ResourceListOfPortfolioGroupDto
from .create_property_request import CreatePropertyRequest
from .instrument_definition_dto import InstrumentDefinitionDto
from .create_client_instrument_request import CreateClientInstrumentRequest
from .property_dto import PropertyDto
from .instrument_dto import InstrumentDto
from .try_add_client_instruments_dto import TryAddClientInstrumentsDto
from .try_delete_client_instruments_dto import TryDeleteClientInstrumentsDto
from .try_lookup_instruments_from_codes_dto import TryLookupInstrumentsFromCodesDto
from .create_instrument_property import CreateInstrumentProperty
from .instrument_property_dto import InstrumentPropertyDto
from .upsert_instrument_properties_dto import UpsertInstrumentPropertiesDto
from .version_summary_dto import VersionSummaryDto
from .personalisation_dto import PersonalisationDto
from .resource_list_of_personalisation_dto import ResourceListOfPersonalisationDto
from .upsert_personalisations_response import UpsertPersonalisationsResponse
from .create_group_request import CreateGroupRequest
from .update_group_request import UpdateGroupRequest
from .aggregate_spec import AggregateSpec
from .property_filter import PropertyFilter
from .aggregation_request import AggregationRequest
from .field_schema import FieldSchema
from .key_value_pair_of_property_key_to_field_schema import KeyValuePairOfPropertyKeyToFieldSchema
from .result_data_schema import ResultDataSchema
from .list_aggregation_response import ListAggregationResponse
from .user_id_dto import UserIdDto
from .processed_command_dto import ProcessedCommandDto
from .resource_list_of_processed_command_dto import ResourceListOfProcessedCommandDto
from .complete_portfolio_dto import CompletePortfolioDto
from .expanded_group_dto import ExpandedGroupDto
from .resource_list_of_scope import ResourceListOfScope
from .resource_list_of_portfolio_dto import ResourceListOfPortfolioDto
from .update_portfolio_request import UpdatePortfolioRequest
from .portfolio_properties_dto import PortfolioPropertiesDto
from .portfolio_search_result import PortfolioSearchResult
from .resource_list_of_portfolio_search_result import ResourceListOfPortfolioSearchResult
from .property_definition_dto import PropertyDefinitionDto
from .resource_list_of_property_definition_dto import ResourceListOfPropertyDefinitionDto
from .create_property_definition_request import CreatePropertyDefinitionRequest
from .update_property_definition_request import UpdatePropertyDefinitionRequest
from .reconciliation_request import ReconciliationRequest
from .reconciliation_break_dto import ReconciliationBreakDto
from .resource_list_of_reconciliation_break_dto import ResourceListOfReconciliationBreakDto
from .create_reference_portfolio_request import CreateReferencePortfolioRequest
from .create_perpetual_property_request import CreatePerpetualPropertyRequest
from .reference_portfolio_constituent_request import ReferencePortfolioConstituentRequest
from .upsert_reference_portfolio_constituents_dto import UpsertReferencePortfolioConstituentsDto
from .reference_portfolio_constituent_dto import ReferencePortfolioConstituentDto
from .resource_list_of_reference_portfolio_constituent_dto import ResourceListOfReferencePortfolioConstituentDto
from .create_results_request import CreateResultsRequest
from .results_dto import ResultsDto
from .resource_list_of_string import ResourceListOfString
from .key_value_pair_of_string_to_field_schema import KeyValuePairOfStringToFieldSchema
from .schema_dto import SchemaDto
from .property_schema_dto import PropertySchemaDto
from .resource_list_of_value_type import ResourceListOfValueType
from .transaction_type_alias_dto import TransactionTypeAliasDto
from .transaction_property_mapping_request import TransactionPropertyMappingRequest
from .transaction_movement_meta_data_request import TransactionMovementMetaDataRequest
from .transaction_meta_data_request import TransactionMetaDataRequest
from .transaction_property_mapping_dto import TransactionPropertyMappingDto
from .transaction_movement_meta_data_dto import TransactionMovementMetaDataDto
from .transaction_meta_data_dto import TransactionMetaDataDto
from .resource_list_of_transaction_meta_data_dto import ResourceListOfTransactionMetaDataDto
from .create_transaction_portfolio_request import CreateTransactionPortfolioRequest
from .portfolio_details_dto import PortfolioDetailsDto
from .portfolio_details_request import PortfolioDetailsRequest
from .nullable_of_currency import NullableOfCurrency
from .perpetual_property_dto import PerpetualPropertyDto
from .transaction_dto import TransactionDto
from .holding_dto import HoldingDto
from .versioned_resource_list_of_holding_dto import VersionedResourceListOfHoldingDto
from .target_tax_lot_request import TargetTaxLotRequest
from .adjust_holding_request import AdjustHoldingRequest
from .adjust_holdings_dto import AdjustHoldingsDto
from .holdings_adjustment_header_dto import HoldingsAdjustmentHeaderDto
from .holdings_adjustment_dto import HoldingsAdjustmentDto
from .versioned_resource_list_of_transaction_dto import VersionedResourceListOfTransactionDto
from .transaction_request import TransactionRequest
from .upsert_portfolio_transactions_dto import UpsertPortfolioTransactionsDto
from .add_transaction_property_dto import AddTransactionPropertyDto
from .transaction_query_parameters import TransactionQueryParameters
from .transaction_price import TransactionPrice
from .currency_and_amount import CurrencyAndAmount
from .realised_gain_loss_dto import RealisedGainLossDto
from .output_transaction_dto import OutputTransactionDto
from .versioned_resource_list_of_output_transaction_dto import VersionedResourceListOfOutputTransactionDto

__all__ = [
    'CreateAnalyticStoreRequest',
    'AnalyticStoreKeyDto',
    'Link',
    'AnalyticStoreDto',
    'ErrorDetailBase',
    'ErrorResponse', 'ErrorResponseException',
    'ResourceListOfAnalyticStoreKeyDto',
    'DeletedEntityResponse',
    'InstrumentAnalyticDataDto',
    'CorporateActionTransitionComponentDto',
    'CorporateActionTransitionDto',
    'UpsertCorporateActionRequest',
    'ResourceId',
    'CorporateActionEventDto',
    'ErrorDetail',
    'TryUpsertCorporateActionsDto',
    'CreateUnitDefinition',
    'CreateDataTypeRequest',
    'IUnitDefinitionDto',
    'DataTypeDto',
    'UpdateDataTypeRequest',
    'ResourceListOfDataTypeDto',
    'CreateDerivedTransactionPortfolioRequest',
    'VersionDto',
    'PortfolioDto',
    'PortfolioGroupDto',
    'ResourceListOfPortfolioGroupDto',
    'CreatePropertyRequest',
    'InstrumentDefinitionDto',
    'CreateClientInstrumentRequest',
    'PropertyDto',
    'InstrumentDto',
    'TryAddClientInstrumentsDto',
    'TryDeleteClientInstrumentsDto',
    'TryLookupInstrumentsFromCodesDto',
    'CreateInstrumentProperty',
    'InstrumentPropertyDto',
    'UpsertInstrumentPropertiesDto',
    'VersionSummaryDto',
    'PersonalisationDto',
    'ResourceListOfPersonalisationDto',
    'UpsertPersonalisationsResponse',
    'CreateGroupRequest',
    'UpdateGroupRequest',
    'AggregateSpec',
    'PropertyFilter',
    'AggregationRequest',
    'FieldSchema',
    'KeyValuePairOfPropertyKeyToFieldSchema',
    'ResultDataSchema',
    'ListAggregationResponse',
    'UserIdDto',
    'ProcessedCommandDto',
    'ResourceListOfProcessedCommandDto',
    'CompletePortfolioDto',
    'ExpandedGroupDto',
    'ResourceListOfScope',
    'ResourceListOfPortfolioDto',
    'UpdatePortfolioRequest',
    'PortfolioPropertiesDto',
    'PortfolioSearchResult',
    'ResourceListOfPortfolioSearchResult',
    'PropertyDefinitionDto',
    'ResourceListOfPropertyDefinitionDto',
    'CreatePropertyDefinitionRequest',
    'UpdatePropertyDefinitionRequest',
    'ReconciliationRequest',
    'ReconciliationBreakDto',
    'ResourceListOfReconciliationBreakDto',
    'CreateReferencePortfolioRequest',
    'CreatePerpetualPropertyRequest',
    'ReferencePortfolioConstituentRequest',
    'UpsertReferencePortfolioConstituentsDto',
    'ReferencePortfolioConstituentDto',
    'ResourceListOfReferencePortfolioConstituentDto',
    'CreateResultsRequest',
    'ResultsDto',
    'ResourceListOfString',
    'KeyValuePairOfStringToFieldSchema',
    'SchemaDto',
    'PropertySchemaDto',
    'ResourceListOfValueType',
    'TransactionTypeAliasDto',
    'TransactionPropertyMappingRequest',
    'TransactionMovementMetaDataRequest',
    'TransactionMetaDataRequest',
    'TransactionPropertyMappingDto',
    'TransactionMovementMetaDataDto',
    'TransactionMetaDataDto',
    'ResourceListOfTransactionMetaDataDto',
    'CreateTransactionPortfolioRequest',
    'PortfolioDetailsDto',
    'PortfolioDetailsRequest',
    'NullableOfCurrency',
    'PerpetualPropertyDto',
    'TransactionDto',
    'HoldingDto',
    'VersionedResourceListOfHoldingDto',
    'TargetTaxLotRequest',
    'AdjustHoldingRequest',
    'AdjustHoldingsDto',
    'HoldingsAdjustmentHeaderDto',
    'HoldingsAdjustmentDto',
    'VersionedResourceListOfTransactionDto',
    'TransactionRequest',
    'UpsertPortfolioTransactionsDto',
    'AddTransactionPropertyDto',
    'TransactionQueryParameters',
    'TransactionPrice',
    'CurrencyAndAmount',
    'RealisedGainLossDto',
    'OutputTransactionDto',
    'VersionedResourceListOfOutputTransactionDto',
]
