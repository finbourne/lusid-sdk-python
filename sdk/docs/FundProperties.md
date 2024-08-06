# FundProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Fund properties. These will be from the &#39;Fund&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.fund_properties import FundProperties

# TODO update the JSON string below
json = "{}"
# create an instance of FundProperties from a JSON string
fund_properties_instance = FundProperties.from_json(json)
# print the JSON string representation of the object
print FundProperties.to_json()

# convert the object into a dict
fund_properties_dict = fund_properties_instance.to_dict()
# create an instance of FundProperties from a dict
fund_properties_form_dict = fund_properties.from_dict(fund_properties_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


