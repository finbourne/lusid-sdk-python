# GeneralLedgerProfileMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping_filter** | **str** | The filter syntax for the Mapping filter. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax | 
**levels** | **List[str]** | References fields and properties on the associated Journal Entry Line and graph of associated objects. | 
## Example

```python
from lusid.models.general_ledger_profile_mapping import GeneralLedgerProfileMapping
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

mapping_filter: StrictStr = "example_mapping_filter"
levels: conlist(StrictStr, max_items=5) = Field(..., description="References fields and properties on the associated Journal Entry Line and graph of associated objects.")
general_ledger_profile_mapping_instance = GeneralLedgerProfileMapping(mapping_filter=mapping_filter, levels=levels)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

