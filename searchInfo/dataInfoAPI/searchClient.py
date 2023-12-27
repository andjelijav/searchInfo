from opensearchpy import OpenSearch

class SearchClient():
    def __init__(self, url, port, username, password):
        self.url=url
        self.port=port
        self.username=username
        self.password=password
        self.client=self.Connect()

    def Connect(self):
        auth = (self.username, self.password)
        ca_certs_path = 'root-ca.pem'

        client = OpenSearch(            
        hosts = [{'host': self.url, 'port': self.port}],
        http_compress = True, # enables gzip compression for request bodies
        http_auth = auth,
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
        ca_certs=ca_certs_path       
        )
        return client

    def CreateIndex(self, index_name, document, id):
       

        response = self.client.index(
            index = index_name,
            body = document,
            id = id,
            refresh = True
            )

        print('\nAdding document:')
        print(response)
    