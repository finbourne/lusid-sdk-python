# WhtParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wht_config** | [**ResourceId**](ResourceId.md) |  | 
**tax_country** | **str** | The holder&#39;s country of tax residence, matched against the taxCountry field of the rate datasets. | 
**profile_type** | **str** | The holder&#39;s tax profile, matched against the profileType field of the rate datasets. | 
## Example

```python
from lusid.models.wht_parameters import WhtParameters
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

wht_config: ResourceId = # Replace with your value
tax_country: StrictStr = "example_tax_country"
profile_type: StrictStr = "example_profile_type"
wht_parameters_instance = WhtParameters(wht_config=wht_config, tax_country=tax_country, profile_type=profile_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

