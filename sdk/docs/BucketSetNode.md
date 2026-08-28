# BucketSetNode

One node within a bucket set result: the fund aggregate or a single share class. Both carry NAV and buckets; the  capital ratio, the unit counts and the per-unit values are set only on share class nodes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** | The kind of node: the fund aggregate or a single share class. Available values: Fund, Class. | 
**share_class_short_code** | **str** | The short code of the share class this node is for, or null for the fund node. | [optional] 
**nav** | **float** | The net asset value at this node, in the fund currency, or null where it does not apply to the node type. | [optional] 
**capital_ratio** | **float** | The share class&#39;s capital ratio (its share of the fund NAV), set only on share class nodes. | [optional] 
**buckets** | [**List[BucketSetResultBucket]**](BucketSetResultBucket.md) | The buckets on this node, each with its period movement and cumulative values. | 
**per_unit_value** | **float** | The share class&#39;s NAV per unit in issue, in the fund currency, rounded to the share class&#39;s PricePrecision (left unrounded where the share class declares none). Reported only for a share class that is unitised and has units in issue to divide by. The dealing price - in the share class currency, with its instrument&#39;s rounding convention applied - is on the share class breakdown&#39;s unitisation data. | [optional] 
**shares_in_issue** | **float** | The share class&#39;s units in issue at the end of the period. Reported only for a share class that is unitised. | [optional] 
**previous_per_unit_value** | **float** | The share class&#39;s NAV per unit at the previous valuation point, on the same basis as PerUnitValue. | [optional] 
**previous_shares_in_issue** | **float** | The share class&#39;s units in issue at the start of the period. Reported only for a share class that is unitised. | [optional] 
## Example

```python
from lusid.models.bucket_set_node import BucketSetNode
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

node_type: StrictStr = "example_node_type"
share_class_short_code: Optional[StrictStr] = "example_share_class_short_code"
nav: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
capital_ratio: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
buckets: List[BucketSetResultBucket] = # Replace with your value
per_unit_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
shares_in_issue: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_per_unit_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_shares_in_issue: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bucket_set_node_instance = BucketSetNode(node_type=node_type, share_class_short_code=share_class_short_code, nav=nav, capital_ratio=capital_ratio, buckets=buckets, per_unit_value=per_unit_value, shares_in_issue=shares_in_issue, previous_per_unit_value=previous_per_unit_value, previous_shares_in_issue=previous_shares_in_issue)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

