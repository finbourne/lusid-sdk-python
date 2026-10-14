# CollateralAgreement

A collateral agreement: who it covers, how exposure is valued, and the variation and initial margin  arrangements collateral is called and returned under.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**counterparty_id** | [**CounterpartyIdentifier**](CounterpartyIdentifier.md) |  | [optional] 
**applicability_filter** | **str** | A filter selecting the portfolios and trades the agreement covers. Checked for structure only when the agreement is stored. | [optional] 
**base_currency** | **str** | The currency margin is calculated and called in. Filterable. | [optional] 
**cut_label** | **str** | The cut label naming the market data that margin is valued at. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**minimum_transfer_amount** | **float** | The smallest margin movement that is called. Optional. | [optional] 
**rounding** | [**MarginRounding**](MarginRounding.md) |  | [optional] 
**settlement_lag** | [**MarginSettlementLag**](MarginSettlementLag.md) |  | [optional] 
**match_tolerance** | **float** | The tolerance within which our margin figure and the counterparty&#39;s are considered to match. Optional. | [optional] 
**variation_margin** | [**List[MarginItem]**](MarginItem.md) | The variation margin arrangements under the agreement. | [optional] 
**initial_margin** | [**List[MarginItem]**](MarginItem.md) | The initial margin arrangements under the agreement. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties to decorate onto the Collateral Agreement. Filterable. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.collateral_agreement import CollateralAgreement
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
counterparty_id: Optional[CounterpartyIdentifier] = # Replace with your value
applicability_filter: Optional[StrictStr] = "example_applicability_filter"
base_currency: Optional[StrictStr] = "example_base_currency"
cut_label: Optional[StrictStr] = "example_cut_label"
recipe_id: Optional[ResourceId] = # Replace with your value
minimum_transfer_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
rounding: Optional[MarginRounding] = None
settlement_lag: Optional[MarginSettlementLag] = # Replace with your value
match_tolerance: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
variation_margin: Optional[List[MarginItem]] = # Replace with your value
initial_margin: Optional[List[MarginItem]] = # Replace with your value
version: Optional[Version] = None
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
links: Optional[List[Link]] = None
collateral_agreement_instance = CollateralAgreement(href=href, id=id, counterparty_id=counterparty_id, applicability_filter=applicability_filter, base_currency=base_currency, cut_label=cut_label, recipe_id=recipe_id, minimum_transfer_amount=minimum_transfer_amount, rounding=rounding, settlement_lag=settlement_lag, match_tolerance=match_tolerance, variation_margin=variation_margin, initial_margin=initial_margin, version=version, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

