# KeyedMarketDataKeyRule

One keyed rule of an MdkrGroup shift: the key names the result column (scenario:key) and the rule  is a standard market data key rule resolved for that column.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key naming this rule&#39;s result column, e.g. \&quot;bid\&quot;. | 
**rule** | [**MarketDataKeyRule**](MarketDataKeyRule.md) |  | 
## Example

```python
from lusid.models.keyed_market_data_key_rule import KeyedMarketDataKeyRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
rule: MarketDataKeyRule
keyed_market_data_key_rule_instance = KeyedMarketDataKeyRule(key=key, rule=rule)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

