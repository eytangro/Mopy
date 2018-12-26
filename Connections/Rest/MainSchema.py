from marshmallow import Schema, fields, post_load

from Mopy.Connections.Rest.RestManager import RestManager


class RequestSchema(Schema):
    def __init__(self, data):
        super(RequestSchema, self).__init__()
        self.name = data["jobId"]
        self.type = data["timestamp"]
        self.url = data["pipeline"]
        self.js = data["status"]
        self.data = data["data"]
        self.params = data["timeTook"]
        self.apiParams = data["storageModule"]
        self.dataItem = data
        self.rest = RestManager()

    name = fields.Str()
    type = fields.Str()
    url = fields.Str()
    js = fields.Dict()
    data = fields.Str()
    params = fields.Dict()
    apiParams = fields.Str()

    @post_load
    def make_obj(self, data=None):
        print("im in " + self.type)
        if self.type == "post":
            return self.rest.Post(self.dataItem)
        elif self.type == "get":
            return self.rest.Get(self.dataItem)
        elif self.type == "delete":
            return self.rest.Delete(self.dataItem)
