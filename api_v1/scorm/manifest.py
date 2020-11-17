class ManifestResourceEntity(object):
    def __init__(self, identifier, resourceType, materialType, href, title = '', linkTarget = ''):
        self.identifier = identifier
        self.resourceType = resourceType
        self.materialType = materialType
        self.href = href
        self.title = title
        self.linkTarget = linkTarget

class ManifestEntity(object):
    resources = []

    def __init__(self):
        del self.resources[:]
        
    def addResource(self, manifestResourceEntity):
        self.resources.append(manifestResourceEntity)

