# HoldingContributor

A list of transactions contributed to a holding.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**Transaction**](Transaction.md) |  | 

## Example

```python
from lusid.models.holding_contributor import HoldingContributor

# TODO update the JSON string below
json = "{}"
# create an instance of HoldingContributor from a JSON string
holding_contributor_instance = HoldingContributor.from_json(json)
# print the JSON string representation of the object
print HoldingContributor.to_json()

# convert the object into a dict
holding_contributor_dict = holding_contributor_instance.to_dict()
# create an instance of HoldingContributor from a dict
holding_contributor_form_dict = holding_contributor.from_dict(holding_contributor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


