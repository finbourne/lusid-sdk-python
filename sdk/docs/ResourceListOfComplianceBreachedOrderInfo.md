# ResourceListOfComplianceBreachedOrderInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ComplianceBreachedOrderInfo]**](ComplianceBreachedOrderInfo.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_compliance_breached_order_info import ResourceListOfComplianceBreachedOrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfComplianceBreachedOrderInfo from a JSON string
resource_list_of_compliance_breached_order_info_instance = ResourceListOfComplianceBreachedOrderInfo.from_json(json)
# print the JSON string representation of the object
print ResourceListOfComplianceBreachedOrderInfo.to_json()

# convert the object into a dict
resource_list_of_compliance_breached_order_info_dict = resource_list_of_compliance_breached_order_info_instance.to_dict()
# create an instance of ResourceListOfComplianceBreachedOrderInfo from a dict
resource_list_of_compliance_breached_order_info_form_dict = resource_list_of_compliance_breached_order_info.from_dict(resource_list_of_compliance_breached_order_info_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


