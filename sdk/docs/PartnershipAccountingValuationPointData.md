# PartnershipAccountingValuationPointData

The partnership accounting view of a valuation point: what is left on the income summary to allocate to the  partners, and the configuration pack the allocation books under.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unallocated_income_summary** | **float** | The profit and loss of the valuation point&#39;s period that has not yet been allocated to the partners: what the period&#39;s income, gain and expense lines would pool, less what the partner allocation has posted for the period. Must be zero before the valuation point can be finalised. | 
**config_pack_scope** | **str** | The scope of the configuration pack. | 
**config_pack_code** | **str** | The code of the configuration pack. | 
## Example

```python
from lusid.models.partnership_accounting_valuation_point_data import PartnershipAccountingValuationPointData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

unallocated_income_summary: Union[StrictFloat, StrictInt] = # Replace with your value
config_pack_scope: StrictStr = "example_config_pack_scope"
config_pack_code: StrictStr = "example_config_pack_code"
partnership_accounting_valuation_point_data_instance = PartnershipAccountingValuationPointData(unallocated_income_summary=unallocated_income_summary, config_pack_scope=config_pack_scope, config_pack_code=config_pack_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

