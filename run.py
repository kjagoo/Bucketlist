from app.smain import Index
from app.auth import Login, UserRegister
from app.bucketlist import Buckets, BucketsId, BucketItemsAdd, BucketItemsGetPutDel
from app import api, app

""" Defining the API endpoints """
api.add_resource(Index, "/")
api.add_resource(UserRegister, "/auth/register/")
api.add_resource(Login, "/auth/login/")
api.add_resource(Buckets, "/bucketlists/")
api.add_resource(BucketsId, "/bucketlists/<id>")
api.add_resource(BucketItemsAdd, "/bucketlists/<id>/items/")
api.add_resource(BucketItemsGetPutDel, "/bucketlists/<id>/items/<item_id>")

if __name__ == "__main__":
    app.run()
