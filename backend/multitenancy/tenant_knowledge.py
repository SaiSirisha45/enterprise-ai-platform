class TenantKnowledgeBase:


    def __init__(self):

        self.documents = {}



    def add_document(
        self,
        tenant_id,
        document
    ):

        if tenant_id not in self.documents:

            self.documents[tenant_id] = []


        self.documents[tenant_id].append(
            document
        )



    def search(
        self,
        tenant_id,
        query
    ):

        tenant_docs = self.documents.get(
            tenant_id,
            []
        )


        results = []


        for doc in tenant_docs:

            if query.lower() in doc.lower():

                results.append(doc)


        return results



knowledge_base = TenantKnowledgeBase() 