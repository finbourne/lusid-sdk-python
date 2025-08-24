# ResultDataKeyRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier** | **str** | the result resource supplier (where the data comes from) | 
**data_scope** | **str** | which is the scope in which the data should be found | 
**document_code** | **str** | document code that defines which document is desired | 
**quote_interval** | **str** | Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example &#39;5D.0D&#39; to look back 5 days from today (0 days ago). | [optional] 
**as_at** | **datetime** | The AsAt predicate specification. | [optional] 
**resource_key** | **str** | The result data key that identifies the address pattern that this is a rule for | 
**document_result_type** | **str** |  | 
**use_document_to_infer_holdings** | **bool** | Indicates whether the relevant document should be used to infer the set of holdings in the valuation. | [optional] 
**result_key_rule_type** | **str** | The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule | 
## Example

```python
from lusid.models.result_data_key_rule import ResultDataKeyRule
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictBool, StrictStr, constr, validator
from datetime import datetime
supplier: StrictStr = "example_supplier"
data_scope: StrictStr = "example_data_scope"
document_code: StrictStr = "example_document_code"
quote_interval: Optional[StrictStr] = "example_quote_interval"
as_at: Optional[datetime] = # Replace with your value
resource_key: StrictStr = "example_resource_key"
document_result_type: StrictStr = "example_document_result_type"
use_document_to_infer_holdings: Optional[StrictBool] = # Replace with your value
use_document_to_infer_holdings:Optional[StrictBool] = None
result_key_rule_type: StrictStr = "example_result_key_rule_type"
result_data_key_rule_instance = ResultDataKeyRule(supplier=supplier, data_scope=data_scope, document_code=document_code, quote_interval=quote_interval, as_at=as_at, resource_key=resource_key, document_result_type=document_result_type, use_document_to_infer_holdings=use_document_to_infer_holdings, result_key_rule_type=result_key_rule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

