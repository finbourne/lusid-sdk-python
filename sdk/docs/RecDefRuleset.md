# RecDefRuleset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rec_type** | **str** | The type of reconciliation this entry configures. Must be valid for the definitionType, and must match the reconciliationType of the referenced matching ruleset. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. | 
**matching_ruleset_id** | [**ResourceId**](ResourceId.md) |  | 
**relational_data_filter** | **str** | Selects the slice of the relational dataset this definition draws from, e.g. \&quot;custodian eq &#39;NT&#39;\&quot;. Only permitted when the referenced ruleset declares a relational side, and combined with AND at run time with that ruleset&#39;s own filter for the side. | [optional] 
## Example

```python
from lusid.models.rec_def_ruleset import RecDefRuleset
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rec_type: StrictStr = "example_rec_type"
matching_ruleset_id: ResourceId = # Replace with your value
relational_data_filter: Optional[StrictStr] = "example_relational_data_filter"
rec_def_ruleset_instance = RecDefRuleset(rec_type=rec_type, matching_ruleset_id=matching_ruleset_id, relational_data_filter=relational_data_filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

