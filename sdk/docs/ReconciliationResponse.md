# ReconciliationResponse

Class representing the set of comparisons that result from comparing holdings and their valuations between two separate evaluations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparisons** | [**List[ReconciliationLine]**](ReconciliationLine.md) | List of comparisons of left to right hand sides. | [optional] 
**data_schema** | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 

## Example

```python
from lusid.models.reconciliation_response import ReconciliationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationResponse from a JSON string
reconciliation_response_instance = ReconciliationResponse.from_json(json)
# print the JSON string representation of the object
print ReconciliationResponse.to_json()

# convert the object into a dict
reconciliation_response_dict = reconciliation_response_instance.to_dict()
# create an instance of ReconciliationResponse from a dict
reconciliation_response_form_dict = reconciliation_response.from_dict(reconciliation_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


