# RecActivityWindow

Base class for the activity windows that give the date range a rec definition's activity-based  reconciliations cover. Polymorphic by windowType; each supported type has a corresponding inherited class.
## Example

```python
from lusid.models.rec_activity_window import RecActivityWindow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with RecActivityWindow 

contiguous_activity_window_instance = lusid.models.contiguous_activity_window.ContiguousActivityWindow(
                        initial_activity_since_effective_at = lusid.models.rec_activity_since_effective_at.RecActivitySinceEffectiveAt(
                            left = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            right = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        window_type = '', )

rec_activity_window_instance = RecActivityWindow(contiguous_activity_window_instance)

```
See all compatible oneOf types with RecActivityWindow


[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

