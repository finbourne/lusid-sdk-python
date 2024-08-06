# ExecutionSetRequest

A request to create or update multiple Executions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[ExecutionRequest]**](ExecutionRequest.md) | A collection of ExecutionRequests. | [optional] 

## Example

```python
from lusid.models.execution_set_request import ExecutionSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionSetRequest from a JSON string
execution_set_request_instance = ExecutionSetRequest.from_json(json)
# print the JSON string representation of the object
print ExecutionSetRequest.to_json()

# convert the object into a dict
execution_set_request_dict = execution_set_request_instance.to_dict()
# create an instance of ExecutionSetRequest from a dict
execution_set_request_form_dict = execution_set_request.from_dict(execution_set_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


