# BondConversionEntry

Information required to specify a conversion event for a convertible bond.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date at which the bond can be converted | [optional] 
**denomination** | **float** | The number of shares to be issued on conversion will be equal to the denomination of the bond divided by the conversion price. Two (and only two) entries out of (Price, Ratio, Denomination) must be provided. So, to allow one entry out of the three to not be provided, we make all the three nullable defaulting to zero and during validation we check if there is exactly one of the three equal to zero. | [optional] 
**price** | **float** | The conversion price Two (and only two) entries out of (Price, Ratio, Denomination) must be provided. So, to allow one entry out of the three to not be provided, we make all the three nullable defaulting to zero and during validation we check if there is exactly one of the three equal to zero. | [optional] 
**ratio** | **float** | The number of common shares received at the time of conversion for each convertible bond Two (and only two) entries out of (Price, Ratio, Denomination) must be provided. So, to allow one entry out of the three to not be provided, we make all the three nullable defaulting to zero and during validation we check if there is exactly one of the three equal to zero. | [optional] 
## Example

```python
from lusid.models.bond_conversion_entry import BondConversionEntry
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt
from datetime import datetime
var_date: Optional[datetime] = # Replace with your value
denomination: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
ratio: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bond_conversion_entry_instance = BondConversionEntry(var_date=var_date, denomination=denomination, price=price, ratio=ratio)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

