# BucketSetResultBucket

One bucket's values within a bucket set node: the movement in the period plus the cumulative values before  and after it (CumulativeValue = Value + PreviousCumulativeValue), and - on share class nodes - the breakdown  of the movement by the source that contributed it and the same values restated per unit in issue.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | The identifier of the bucket. | 
**bucket_type** | **str** | The type of the bucket (for example Dealing or PnL). | 
**value** | **float** | The movement in the bucket over the valuation point&#39;s period. | 
**previous_cumulative_value** | **float** | The cumulative value of the bucket up to the start of the period. | 
**cumulative_value** | **float** | The cumulative value of the bucket up to the end of the period (Value + PreviousCumulativeValue). | 
**source_breakdown** | **Dict[str, float]** | The bucket&#39;s movement broken down by the source that contributed it, which always sums to Value. Reported on share class nodes and omitted on the fund node; on a share class node it is present even when nothing contributed in the period, as an empty map. The keys are &#39;classSpecific&#39; for amounts booked directly to the share class, &#39;nonClassSpecific&#39; for fund-level amounts apportioned to it, and an allocation group&#39;s code for amounts allocated to that group and apportioned to the share class. Sources contributing nothing to the bucket are omitted. | [optional] 
**per_unit_value** | **float** | The bucket&#39;s movement over the period per unit in issue (Value divided by UnitsInIssue), in the fund currency, rounded to the share class&#39;s PricePrecision. Omitted where either the share class or the bucket is not unitised, and where a unitised share class has no units in issue to divide by (UnitsInIssue is then reported as zero). | [optional] 
**units_in_issue** | **float** | The share class&#39;s units in issue at the end of the period. Omitted where either the share class or the bucket is not unitised. | [optional] 
**previous_cumulative_per_unit_value** | **float** | The bucket&#39;s cumulative value at the start of the period, per unit in issue at that point - so it reads as it did at the previous valuation point rather than being restated at this period&#39;s unit count. Omitted where the bucket had no per-unit value at the previous valuation point: on the fund node, where the share class or the bucket is not unitised, where the share class then had no units in issue, and at the fund&#39;s first valuation point. | [optional] 
**cumulative_per_unit_value** | **float** | The bucket&#39;s cumulative value at the end of the period per unit in issue (CumulativeValue divided by UnitsInIssue). Omitted where either the share class or the bucket is not unitised, and where a unitised share class has no units in issue to divide by. | [optional] 
**display_name** | **str** | The display name of the bucket, as configured on the fund configuration. | [optional] 
## Example

```python
from lusid.models.bucket_set_result_bucket import BucketSetResultBucket
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_id: StrictStr = "example_bucket_id"
bucket_type: StrictStr = "example_bucket_type"
value: Union[StrictFloat, StrictInt] = # Replace with your value
previous_cumulative_value: Union[StrictFloat, StrictInt] = # Replace with your value
cumulative_value: Union[StrictFloat, StrictInt] = # Replace with your value
source_breakdown: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
per_unit_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
units_in_issue: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_cumulative_per_unit_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cumulative_per_unit_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
bucket_set_result_bucket_instance = BucketSetResultBucket(bucket_id=bucket_id, bucket_type=bucket_type, value=value, previous_cumulative_value=previous_cumulative_value, cumulative_value=cumulative_value, source_breakdown=source_breakdown, per_unit_value=per_unit_value, units_in_issue=units_in_issue, previous_cumulative_per_unit_value=previous_cumulative_per_unit_value, cumulative_per_unit_value=cumulative_per_unit_value, display_name=display_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

