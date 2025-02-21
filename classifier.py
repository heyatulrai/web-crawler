class Classifier:
    def classify(self, metadata: dict) -> list:
        # Simple classification based on the presence of certain keywords
        if 'toaster' in metadata.get('title', '').lower():
            return ['Kitchen', 'Appliances']
        elif 'outdoors' in metadata.get('title', '').lower():
            return ['Outdoors', 'Camping']
        elif 'politics' in metadata.get('title', '').lower():
            return ['Politics', 'News']
        else:
            return ['Unclassified']