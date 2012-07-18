from django.conf import settings

#
# Utility methods for transforming shapefile columns into useful representations
# supplementing the functions that come with the boundary service.
#

class simple_index_namer():
    """
    Name features with a joined combination of attributes, optionally passing 
    the result through a normalizing function.  Adds an additonal suffix if
    multiple values are used.
    """
    def __init__(self, attribute_names, seperator='-', normalizer=None):
        self.attribute_names = attribute_names
        self.seperator = seperator
        self.normalizer = normalizer
        self.found = {}

    def __call__(self, feature):
        attribute_values = map(str, map(feature.get, self.attribute_names))
        name = self.seperator.join(attribute_values).strip()
        
        if self.normalizer:
            normed = self.normalizer(name)
            if not normed:
                raise ValueError('Failed to normalize \"%s\".' % name)
            else:
                name = normed
        
        # Check if found already
        if name in self.found:
          self.found[name] = self.found[name] + 1
          name = name + self.seperator + str(self.found[name])
        else:
          self.found[name] = 0
          
        return name

