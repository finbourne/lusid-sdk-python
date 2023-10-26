# AccountProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Account properties. These will be from the &#39;Account&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.account_properties import AccountProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AccountProperties from a JSON string
account_properties_instance = AccountProperties.from_json(json)
# print the JSON string representation of the object
print AccountProperties.to_json()

# convert the object into a dict
account_properties_dict = account_properties_instance.to_dict()
# create an instance of AccountProperties from a dict
account_properties_form_dict = account_properties.from_dict(account_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


