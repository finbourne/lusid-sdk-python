# FundDefinitionRequest

The request used to create a Fund.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Fund. | 
**display_name** | **str** | The name of the Fund. | 
**description** | **str** | A description for the Fund. | [optional] 
**base_currency** | **str** | The base currency of the Fund in ISO 4217 currency code format. All portfolios must be of a matching base currency. | 
**investor_structure** | **str** | The Investor structure to be used by the Fund. Supported values are &#39;NonUnitised&#39;, &#39;Classes&#39; and &#39;Custom&#39;. | [optional] 
**portfolio_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | A list of the Portfolio IDs associated with the fund, which are part of the Fund. Note: These must all have the same base currency, which must also much the Fund Base Currency. | 
**fund_configuration_id** | [**ResourceId**](ResourceId.md) |  | 
**share_class_instrument_scopes** | **List[str]** | The scopes in which the instruments lie, currently limited to one. | [optional] 
**share_class_instruments** | [**List[InstrumentResolutionDetail]**](InstrumentResolutionDetail.md) | Details the user-provided instrument identifiers and the instrument resolved from them. | [optional] 
**type** | **str** | The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39; | [optional] 
**inception_date** | **datetime** | Inception date of the Fund | 
**decimal_places** | **int** | Number of decimal places for reporting | [optional] 
**primary_nav_type** | [**NavTypeDefinition**](NavTypeDefinition.md) |  | 
**additional_nav_types** | [**List[NavTypeDefinition]**](NavTypeDefinition.md) | The definitions for any additional NAVs on the Fund. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund. | [optional] 
## Example

```python
from lusid.models.fund_definition_request import FundDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
base_currency: StrictStr = "example_base_currency"
investor_structure: Optional[StrictStr] = "example_investor_structure"
portfolio_ids: List[PortfolioEntityId] = # Replace with your value
fund_configuration_id: ResourceId = # Replace with your value
share_class_instrument_scopes: Optional[List[StrictStr]] = # Replace with your value
share_class_instruments: Optional[List[InstrumentResolutionDetail]] = # Replace with your value
type: Optional[StrictStr] = "example_type"
inception_date: datetime = # Replace with your value
decimal_places: Optional[StrictInt] = # Replace with your value
decimal_places: Optional[StrictInt] = None
primary_nav_type: NavTypeDefinition = # Replace with your value
additional_nav_types: Optional[List[NavTypeDefinition]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
fund_definition_request_instance = FundDefinitionRequest(code=code, display_name=display_name, description=description, base_currency=base_currency, investor_structure=investor_structure, portfolio_ids=portfolio_ids, fund_configuration_id=fund_configuration_id, share_class_instrument_scopes=share_class_instrument_scopes, share_class_instruments=share_class_instruments, type=type, inception_date=inception_date, decimal_places=decimal_places, primary_nav_type=primary_nav_type, additional_nav_types=additional_nav_types, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

