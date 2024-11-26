# RiskModelFactorSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | Factor Set name. | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.risk_model_factor_set import RiskModelFactorSet

# TODO update the JSON string below
json = "{}"
# create an instance of RiskModelFactorSet from a JSON string
risk_model_factor_set_instance = RiskModelFactorSet.from_json(json)
# print the JSON string representation of the object
print RiskModelFactorSet.to_json()

# convert the object into a dict
risk_model_factor_set_dict = risk_model_factor_set_instance.to_dict()
# create an instance of RiskModelFactorSet from a dict
risk_model_factor_set_form_dict = risk_model_factor_set.from_dict(risk_model_factor_set_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


