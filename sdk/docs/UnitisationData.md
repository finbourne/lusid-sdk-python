# UnitisationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares_in_issue** | **float** | The number of shares in issue at a valuation point. | 
**unit_price** | **float** | The price of one unit of the share class at a valuation point. | 
**net_dealing_units** | **float** | The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units). | 
**bid_price** | **float** | The price of one unit of the share class on the bid side at a valuation point: the class&#39;s NAV with the fund&#39;s holdings marked at their bid prices. Equal to the unit price when the fund is struck on the bid. Absent when a holding&#39;s bid could not be priced. | [optional] 
**offer_price** | **float** | The price of one unit of the share class on the offer side at a valuation point: the class&#39;s NAV with the fund&#39;s holdings marked at their ask prices. Equal to the unit price when the fund is struck on the ask. Absent when a holding&#39;s ask could not be priced. | [optional] 
**bid_price_inc_ndc** | **float** | The bid price of one unit of the share class less the class&#39;s share of the notional dealing costs of selling the fund&#39;s holdings, at a valuation point. Absent when the NAV type has no notional dealing cost table. | [optional] 
**offer_price_inc_ndc** | **float** | The offer price of one unit of the share class plus the class&#39;s share of the notional dealing costs of buying the fund&#39;s holdings, at a valuation point. Absent when the NAV type has no notional dealing cost table. | [optional] 
## Example

```python
from lusid.models.unitisation_data import UnitisationData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

shares_in_issue: Union[StrictFloat, StrictInt] = # Replace with your value
unit_price: Union[StrictFloat, StrictInt] = # Replace with your value
net_dealing_units: Union[StrictFloat, StrictInt] = # Replace with your value
bid_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
offer_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bid_price_inc_ndc: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
offer_price_inc_ndc: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
unitisation_data_instance = UnitisationData(shares_in_issue=shares_in_issue, unit_price=unit_price, net_dealing_units=net_dealing_units, bid_price=bid_price, offer_price=offer_price, bid_price_inc_ndc=bid_price_inc_ndc, offer_price_inc_ndc=offer_price_inc_ndc)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

