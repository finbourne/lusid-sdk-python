{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   :members:
   
   {% block attributes %}
   {% if attributes %}
   .. rubric:: {{ _('Attributes') }}
   This is a Pydantic class. For now, click on the green [source] link in the class signature above to see descriptions/allowed values for these attributes.
   
   .. autosummary::
   {% for item in attributes %}
      ~{{ name }}.{{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}
   
   
   {%- if not fullname.startswith('sdk.lusid.models') %}
   {% block methods %}
   {% if methods %}
   .. rubric:: {{ _('Methods') }}

   .. autosummary::
      :nosignatures:
   {% for item in methods %}
      {%- if not item.startswith('_') %}
      ~{{ name }}.{{ item }}
      {%- endif -%}
   {%- endfor %}
   {% endif %}
   {% endblock %}
   {%- endif -%}
