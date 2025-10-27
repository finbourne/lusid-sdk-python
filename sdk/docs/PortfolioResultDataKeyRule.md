# PortfolioResultDataKeyRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier** | **str** | the result resource supplier (where the data comes from) | 
**data_scope** | **str** | which is the scope in which the data should be found | 
**document_code** | **str** | document code that defines which document is desired | 
**quote_interval** | **str** | Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example &#39;5D.0D&#39; to look back 5 days from today (0 days ago). | [optional] 
**as_at** | **datetime** | The AsAt predicate specification. | [optional] 
**portfolio_code** | **str** |  | [optional] 
**portfolio_scope** | **str** |  | [optional] 
**result_key_rule_type** | **str** | The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule | 
## Example

```python
from lusid.models.portfolio_result_data_key_rule import PortfolioResultDataKeyRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

supplier: StrictStr = "example_supplier"
data_scope: StrictStr = "example_data_scope"
document_code: StrictStr = "example_document_code"
quote_interval: Optional[StrictStr] = "example_quote_interval"
as_at: Optional[datetime] = # Replace with your value
portfolio_code: Optional[StrictStr] = "example_portfolio_code"
portfolio_scope: Optional[StrictStr] = "example_portfolio_scope"
result_key_rule_type: StrictStr = "example_result_key_rule_type"
portfolio_result_data_key_rule_instance = PortfolioResultDataKeyRule(supplier=supplier, data_scope=data_scope, document_code=document_code, quote_interval=quote_interval, as_at=as_at, portfolio_code=portfolio_code, portfolio_scope=portfolio_scope, result_key_rule_type=result_key_rule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

