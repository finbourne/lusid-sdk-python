# PopulateResultProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The property the formula populates. Must be an existing, single-valued property in the RecResult domain, and may appear only once. | 
**formula** | **str** | The formula whose value populates the property; a null value means the property has no value. | 
**overwrite_manual_edits_on_re_run** | **bool** | Whether a value edited since the property was last populated is replaced. Defaults to false, so manual edits are kept. | [optional] 
## Example

```python
from lusid.models.populate_result_property import PopulateResultProperty
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_key: StrictStr = "example_property_key"
formula: StrictStr = "example_formula"
overwrite_manual_edits_on_re_run: Optional[StrictBool] = # Replace with your value
overwrite_manual_edits_on_re_run:Optional[StrictBool] = None
populate_result_property_instance = PopulateResultProperty(property_key=property_key, formula=formula, overwrite_manual_edits_on_re_run=overwrite_manual_edits_on_re_run)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

