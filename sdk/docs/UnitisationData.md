# UnitisationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares_in_issue** | **float** | The number of shares in issue at a valuation point. | 
**unit_price** | **float** | The price of one unit of the share class at a valuation point. | 
**net_dealing_units** | **float** | The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units). | 
## Example

```python
from lusid.models.unitisation_data import UnitisationData
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

shares_in_issue: Union[StrictFloat, StrictInt] = # Replace with your value
unit_price: Union[StrictFloat, StrictInt] = # Replace with your value
net_dealing_units: Union[StrictFloat, StrictInt] = # Replace with your value
unitisation_data_instance = UnitisationData(shares_in_issue=shares_in_issue, unit_price=unit_price, net_dealing_units=net_dealing_units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

