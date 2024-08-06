# FlowConventionName

Representation of an abstract definition of a flow convention set consisting of currency, tenor and an index name (arbitrary string but likely something like \"IBOR\").

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of the flow convention name. | 
**index_name** | **str** | The index, if present, that is required. e.g. \&quot;IBOR\&quot;, \&quot;OIS\&quot; or \&quot;SONIA\&quot;. | [optional] 
**tenor** | **str** | Tenor for the convention name.    For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | 

## Example

```python
from lusid.models.flow_convention_name import FlowConventionName

# TODO update the JSON string below
json = "{}"
# create an instance of FlowConventionName from a JSON string
flow_convention_name_instance = FlowConventionName.from_json(json)
# print the JSON string representation of the object
print FlowConventionName.to_json()

# convert the object into a dict
flow_convention_name_dict = flow_convention_name_instance.to_dict()
# create an instance of FlowConventionName from a dict
flow_convention_name_form_dict = flow_convention_name.from_dict(flow_convention_name_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


