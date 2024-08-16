# ShareClassDealingBreakdown

The breakdown of Dealing for a Share Class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_dealing** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for any &#39;Dealing&#39; specific to the share class that has occured inside the queried period. | 
**class_dealing_units** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for any &#39;Dealing&#39; units specific to the share class that has occured inside the queried period. | 

## Example

```python
from lusid.models.share_class_dealing_breakdown import ShareClassDealingBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ShareClassDealingBreakdown from a JSON string
share_class_dealing_breakdown_instance = ShareClassDealingBreakdown.from_json(json)
# print the JSON string representation of the object
print ShareClassDealingBreakdown.to_json()

# convert the object into a dict
share_class_dealing_breakdown_dict = share_class_dealing_breakdown_instance.to_dict()
# create an instance of ShareClassDealingBreakdown from a dict
share_class_dealing_breakdown_form_dict = share_class_dealing_breakdown.from_dict(share_class_dealing_breakdown_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


