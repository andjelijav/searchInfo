import seafileapi

class SClient:
    def __init__(self, url, username, password):
        self.url=url
        self.username=username
        self.password=password
        self.client=self.Connect()

    
    def Connect(self):
        client = seafileapi.connect(self.url, self.username, self.password)
        return client
    
    def UploadFile(self, repoID, document):
        
        repo = self.client.repos.get_repo(repoID)
        seafdir = repo.get_dir('/root')
	
        file = seafdir.upload_local_file(document)
        return file