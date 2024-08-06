# CustodianAccountProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Custodian Account properties. These will be from the &#39;CustodianAccount&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.custodian_account_properties import CustodianAccountProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CustodianAccountProperties from a JSON string
custodian_account_properties_instance = CustodianAccountProperties.from_json(json)
# print the JSON string representation of the object
print CustodianAccountProperties.to_json()

# convert the object into a dict
custodian_account_properties_dict = custodian_account_properties_instance.to_dict()
# create an instance of CustodianAccountProperties from a dict
custodian_account_properties_form_dict = custodian_account_properties.from_dict(custodian_account_properties_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


