# WithholdingTaxRateTiers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_rate** | **float** | The statutory rate of the matched row, before relief. | 
**treaty_rate** | **float** | The treaty rate of the matched row. Null when the tier does not apply. | [optional] 
**better_rate** | **float** | The better rate of the matched row. Null when the tier does not apply. | [optional] 
**enhanced_rate** | **float** | The enhanced rate of the matched row. Null when the tier does not apply. | [optional] 
## Example

```python
from lusid.models.withholding_tax_rate_tiers import WithholdingTaxRateTiers
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

country_rate: Union[StrictFloat, StrictInt] = # Replace with your value
treaty_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
better_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
enhanced_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
withholding_tax_rate_tiers_instance = WithholdingTaxRateTiers(country_rate=country_rate, treaty_rate=treaty_rate, better_rate=better_rate, enhanced_rate=enhanced_rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

