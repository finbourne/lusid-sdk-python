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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

currency: StrictStr = "example_currency"
index_name: Optional[StrictStr] = "example_index_name"
tenor: StrictStr = "example_tenor"
flow_convention_name_instance = FlowConventionName(currency=currency, index_name=index_name, tenor=tenor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

