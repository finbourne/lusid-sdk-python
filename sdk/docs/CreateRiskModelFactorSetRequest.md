# CreateRiskModelFactorSetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** | Factor Set name. | 

## Example

```python
from lusid.models.create_risk_model_factor_set_request import CreateRiskModelFactorSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRiskModelFactorSetRequest from a JSON string
create_risk_model_factor_set_request_instance = CreateRiskModelFactorSetRequest.from_json(json)
# print the JSON string representation of the object
print CreateRiskModelFactorSetRequest.to_json()

# convert the object into a dict
create_risk_model_factor_set_request_dict = create_risk_model_factor_set_request_instance.to_dict()
# create an instance of CreateRiskModelFactorSetRequest from a dict
create_risk_model_factor_set_request_form_dict = create_risk_model_factor_set_request.from_dict(create_risk_model_factor_set_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


