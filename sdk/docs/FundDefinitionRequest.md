# FundDefinitionRequest

The request used to create a Fund.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Fund. | 
**short_code** | **str** | A short code for the Fund. A fund structure tags journal entry lines with the short code of the member they originated from, so it should be unique across the funds of one structure. Optional. | [optional] 
**display_name** | **str** | The name of the Fund. | 
**description** | **str** | A description for the Fund. | [optional] 
**base_currency** | **str** | The base currency of the Fund in ISO 4217 currency code format. All portfolios must be of a matching base currency. | 
**investor_structure** | **str** | The Investor structure to be used by the Fund. Available values: NonUnitised, Classes. | [optional] 
**portfolio_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | A list of the Portfolio IDs associated with the fund, which are part of the Fund. Note: These must all have the same base currency, which must also match the Fund Base Currency. | 
**fund_configuration_id** | [**ResourceId**](ResourceId.md) |  | 
**share_class_instrument_scopes** | **List[str]** | The scopes in which the instruments lie, currently limited to one. | [optional] 
**share_class_instruments** | [**List[InstrumentResolutionDetail]**](InstrumentResolutionDetail.md) | Details the user-provided instrument identifiers and the instrument resolved from them. These would be decommissioned in favour of the new AllocationGroups and ShareClasses structures. | [optional] 
**type** | **str** | The kind of vehicle the fund is, one of the values of the system/fundVehicleType data type. Master and Feeder are deprecated: the structural role of a fund now lives on its fund structure node, and a fund with either type cannot be a member of a fund structure. Available values: Standalone, Master, Feeder, SPV, AIV, TaxBlocker, CarryVehicle, SponsorCommitmentVehicle, CoInvestVehicle, GPInterestHolder, SMA, CTA. | [optional] 
**tax_transparency** | **str** | Whether the Fund is looked through for tax: Transparent passes its income and gains to its holders as their own, Opaque is taxed in its own right. Optional; if not set, a TaxBlocker is Opaque and a CarryVehicle or GPInterestHolder is Transparent. A fund structure requires it on every SPV and AIV member. Available values: Transparent, Opaque. | [optional] 
**inception_date** | **datetime** | Inception date of the Fund | 
**decimal_places** | **int** | Number of decimal places for reporting | [optional] 
**primary_nav_type** | [**NavTypeDefinition**](NavTypeDefinition.md) |  | 
**additional_nav_types** | [**List[NavTypeDefinition]**](NavTypeDefinition.md) | The definitions for any additional NAVs on the Fund. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund. | [optional] 
**create_instrument** | **bool** | Whether to create instruments for the Fund&#39;s share classes, series, or partner classes upon creation. Defaults to false. | [optional] 
**share_classes** | [**List[ShareClassDefinition]**](ShareClassDefinition.md) | An optional list of Share Class definitions for the Fund. | [optional] 
**pricing_methodology** | [**PricingMethodology**](PricingMethodology.md) |  | [optional] 
**reporting_prices** | [**List[ReportingPrice]**](ReportingPrice.md) | Share class prices the Fund publishes at each valuation point under labels of its own, alongside the dealing price, for example a mid price for performance reporting. Optional. Each source other than Mid must be published by the valuation recipe of every active NAV type. Labels must be unique and cannot be dealingPrice, dealingBid or dealingOffer. Patch the list whole at /reportingPrices. | [optional] 
## Example

```python
from lusid.models.fund_definition_request import FundDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
short_code: Optional[StrictStr] = "example_short_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
base_currency: StrictStr = "example_base_currency"
investor_structure: Optional[StrictStr] = "example_investor_structure"
portfolio_ids: List[PortfolioEntityId] = # Replace with your value
fund_configuration_id: ResourceId = # Replace with your value
share_class_instrument_scopes: Optional[List[StrictStr]] = # Replace with your value
share_class_instruments: Optional[List[InstrumentResolutionDetail]] = # Replace with your value
type: Optional[StrictStr] = "example_type"
tax_transparency: Optional[StrictStr] = "example_tax_transparency"
inception_date: datetime = # Replace with your value
decimal_places: Optional[StrictInt] = # Replace with your value
decimal_places: Optional[StrictInt] = None
primary_nav_type: NavTypeDefinition = # Replace with your value
additional_nav_types: Optional[List[NavTypeDefinition]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
create_instrument: Optional[StrictBool] = # Replace with your value
create_instrument:Optional[StrictBool] = None
share_classes: Optional[List[ShareClassDefinition]] = # Replace with your value
pricing_methodology: Optional[PricingMethodology] = # Replace with your value
reporting_prices: Optional[List[ReportingPrice]] = # Replace with your value
fund_definition_request_instance = FundDefinitionRequest(code=code, short_code=short_code, display_name=display_name, description=description, base_currency=base_currency, investor_structure=investor_structure, portfolio_ids=portfolio_ids, fund_configuration_id=fund_configuration_id, share_class_instrument_scopes=share_class_instrument_scopes, share_class_instruments=share_class_instruments, type=type, tax_transparency=tax_transparency, inception_date=inception_date, decimal_places=decimal_places, primary_nav_type=primary_nav_type, additional_nav_types=additional_nav_types, properties=properties, create_instrument=create_instrument, share_classes=share_classes, pricing_methodology=pricing_methodology, reporting_prices=reporting_prices)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

