# Person


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the Person | [optional] 
**description** | **str** | The description of the Person | [optional] 
**href** | **str** | The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**lusid_person_id** | **str** | The unique LUSID Person Identifier of the Person. | [optional] 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Person. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Person. There can be multiple properties associated with a property key. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the Person. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print Person.to_json()

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_form_dict = person.from_dict(person_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


