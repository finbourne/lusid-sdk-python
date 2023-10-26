# Package

A structure used to describe the structure of an order or orders that make up a non-trivial trade.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**order_ids** | [**List[ResourceId]**](ResourceId.md) | Related order ids. | 
**order_instruction_ids** | [**List[ResourceId]**](ResourceId.md) | Related order instruction ids. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.package import Package

# TODO update the JSON string below
json = "{}"
# create an instance of Package from a JSON string
package_instance = Package.from_json(json)
# print the JSON string representation of the object
print Package.to_json()

# convert the object into a dict
package_dict = package_instance.to_dict()
# create an instance of Package from a dict
package_form_dict = package.from_dict(package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


