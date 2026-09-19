# BucketSetNode

One node within a bucket set result: the fund aggregate or a single share class. Both carry NAV and buckets; the  capital ratio, the unit counts and the per-unit values belong to share class nodes and are omitted on the fund node.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** | The kind of node: the fund aggregate or a single share class. Available values: Fund, Class. | 
**share_class_short_code** | **str** | The short code of the share class this node is for. Omitted on the fund node. | [optional] 
**nav** | **float** | The net asset value at this node, in the fund currency. | [optional] 
**capital_ratio** | **float** | The share class&#39;s capital ratio (its share of the fund NAV). Omitted on the fund node. | [optional] 
**buckets** | [**List[BucketSetResultBucket]**](BucketSetResultBucket.md) | The buckets on this node, each with its period movement and cumulative values. | 
**per_unit_value** | **float** | The share class&#39;s NAV per unit in issue, in the fund currency, rounded to the share class&#39;s PricePrecision (left unrounded where the share class declares none). Omitted on the fund node, for a share class that is not unitised, and for a unitised share class with no units in issue to divide by (SharesInIssue is then reported as zero). The dealing price - in the share class currency, with its instrument&#39;s rounding convention applied - is on the share class breakdown&#39;s unitisation data. | [optional] 
**shares_in_issue** | **float** | The share class&#39;s units in issue at the end of the period. Omitted on the fund node and for a share class that is not unitised. | [optional] 
**previous_per_unit_value** | **float** | The share class&#39;s NAV per unit at the previous valuation point, on the same basis as PerUnitValue. Omitted on the fund node, for a share class that is not unitised, and where the share class had no units in issue at the previous valuation point (including the fund&#39;s first valuation point). | [optional] 
**previous_shares_in_issue** | **float** | The share class&#39;s units in issue at the start of the period. Omitted on the fund node and for a share class that is not unitised; zero at the fund&#39;s first valuation point. | [optional] 
**label** | **str** | A display label for the node: the fund&#39;s display name on the fund node, the share class&#39;s name on a share class node. | [optional] 
**previous_nav** | **float** | The net asset value this node carried at the previous valuation point, in the fund currency. Zero at the fund&#39;s first valuation point. | [optional] 
**net_dealing_units** | **float** | The net units dealt for the share class over the period, so that the shares in issue are the previous shares in issue plus this. Omitted on the fund node and where the bucket set is not unitised. | [optional] 
**share_class_details** | [**BucketSetShareClassDetails**](BucketSetShareClassDetails.md) |  | [optional] 
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
label: Optional[StrictStr] = "example_label"
previous_nav: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_dealing_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
share_class_details: Optional[BucketSetShareClassDetails] = # Replace with your value
bucket_set_node_instance = BucketSetNode(node_type=node_type, share_class_short_code=share_class_short_code, nav=nav, capital_ratio=capital_ratio, buckets=buckets, per_unit_value=per_unit_value, shares_in_issue=shares_in_issue, previous_per_unit_value=previous_per_unit_value, previous_shares_in_issue=previous_shares_in_issue, label=label, previous_nav=previous_nav, net_dealing_units=net_dealing_units, share_class_details=share_class_details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

