class Ioc(object):
    def __init__(self, intel):
        self.intel = intel

    @property
    def reported_by(self):
        '''Which data source categorized this IOC
        This could be a feed or another provider of threat intelligence.
        '''
        reported_by = []
        if 'context' not in self.intel:
            return reported_by
        reported_by = self.intel[u'context'][u'categories'].keys()
        return reported_by

    def _namespaced_values(self, kind):
        '''Extract all the namespaced values (internal use)
        To keep track of what source said what each field in the context is
        namespaced by the source who reported it.
        '''
        values = []
        if 'context' not in self.intel:
            return values
        context = self.intel[u'context']
        values = set([v
                     for src, value in context[kind].items()
                     for v in value])
        return list(values)

    @property
    def categories(self):
        '''All the categories associated with this IOC'''
        return self._namespaced_values(u'categories')

    @property
    def identifiers(self):
        '''All the identifiers associated with this IOC
        This could be the name of the threat actor, tool or exploit type'''
        return self._namespaced_values(u'identifiers')

    @property
    def reasons(self):
        '''Additional data associated with categorization'''
        return self._namespaced_values(u'reasons')

    @property
    def source_urls(self):
        '''These are URLs you can get more detailed info on this IOC'''
        return self._namespaced_values(u'source_urls')

    @property
    def passive_dns(self):
        '''Passive DNS data for this IOC'''
        return self.intel[u'passive_dns']

    @property
    def ioc_type(self):
        '''The kind of IOC represented in the report
        This could be IP, CIDR, ASN, Host or File'''
        return self.intel[u'type']

    @property
    def ioc_id(self):
        '''The IOC'''
        return self.intel[u'id']
