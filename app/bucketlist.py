from flask import g, request
from flask_restful import Resource, marshal
from flask_restful import reqparse
from .inputfields import bucket_item_inputs, bucket_inputs
from .model import BucketListItems, Bucket
from .smain import unauthorized, add_item, delete_item, edit_item
from .smain import authorized_user_bucketlist, authorized_user_item
from .config_bucket import Config


class Buckets(Resource):
    """ URL: /bucketlists/  Request methods: GET, POST """
    def get(self):
        """ Get all bucket lists belonging to the current user with pagination
        """

        args = request.args.to_dict()
        page = int(args.get("page", 1))
        limit = int(args.get("limit", 20))
        search = args.get("q")
        kwargs = {"created_by": g.user.id}

        if search:
            kwargs.update({"title": search})
            error_message = {"message": "The bucketlist '" + search +
                             "' does not exist."}

        bucketlists = Bucket.query.filter_by(**kwargs
                                             ).paginate(page=page,
                                                        per_page=limit,
                                                        error_out=False)
        total_pages = bucketlists.pages
        has_next_page = bucketlists.has_next
        has_previous_page = bucketlists.has_prev

        next_page = "None"
        previous_page = "None"
        if has_next_page:
            next_page = str(request.url_root) + "/bucketlists?" + \
                "limit=" + str(limit) + "&page=" + str(page + 1)

        if has_previous_page:
            previous_page = request.url_root + "/bucketlists?" + \
                "limit=" + str(limit) + "&page=" + str(page - 1)

        bucketlists = bucketlists.items

        output = {"bucketlists": marshal(bucketlists, bucket_inputs),
                  "has_next_page": has_next_page,
                  "total_pages": total_pages,
                  "previous_pagea": previous_page,
                  "next_page": next_page
                  }
        error_message = {"bucketlists": [{"message":
                                          "Bucket Lists are Empty"}],
                         "has_next_page": has_next_page,
                         "total_pages": total_pages,
                         "previous_pagea": previous_page,
                         "next_page": next_page}

        if bucketlists:
            return output
        else:
            return error_message

    def post(self):
        """ Add a bucket list """
        parser = reqparse.RequestParser()
        parser.add_argument("title", required=True, help="No title provided.")
        parser.add_argument("description", type=str, default="")
        args = parser.parse_args()
        title, description = args["title"], args["description"]
        bucketlist = Bucket(title=title,
                            description=description,
                            created_by=g.user.id)

        return add_item(name="title",
                        item=bucketlist,
                        serializer=bucket_inputs,
                        is_user=False,
                        is_bucket=True,
                        is_item=False)


class BucketsId(Resource):
    """ URL: /bucketlists/<id>   Request methods: GET, PUT, DELETE   """
    @authorized_user_bucketlist
    def get(self, id):
        """ Get a bucket list """
        return marshal(g.bucketlist, bucket_inputs)

    @authorized_user_bucketlist
    def put(self, id):
        """ Edit a bucket list """
        parser = reqparse.RequestParser()
        parser.add_argument("title",
                            required=True,
                            help="No title provided.")
        parser.add_argument("description", type=str, default="")
        args = parser.parse_args()
        title, description = args["title"], args["description"]
        g.bucketlist.title = title
        g.bucketlist.description = description
        return edit_item(name="title",
                         item=g.bucketlist,
                         serializer=bucket_inputs,
                         is_user=False,
                         is_bucket=True,
                         is_item=False)

    @authorized_user_bucketlist
    def delete(self, id):
        """ Delete a bucket list """
        return delete_item(g.bucketlist,
                           g.bucketlist.title,
                           is_user=False,
                           is_bucket=True,
                           is_item=False)


class BucketItemsAdd(Resource):
    """ URL: /bucketlists/<id>/items/   Request methods: GET, POST """

    def post(self, id):
        """ Add a new item to a bucket list """
        bucket = Bucket.query.get(id)
        if bucket:
            if bucket.created_by == g.user.id:
                parser = reqparse.RequestParser()
                parser.add_argument("title",
                                    required=True,
                                    help="No title provided.")
                parser.add_argument("description", type=str, default="")
                args = parser.parse_args()
                title, description = args["title"], args["description"]
                item = BucketListItems(title=title,
                                       description=description,
                                       bucket_id=id,
                                       created_by=g.user.id)
                return add_item(name="title",
                                item=item,
                                serializer=bucket_item_inputs,
                                is_user=False,
                                is_bucket=False,
                                is_item=True)
            else:
                return unauthorized()
        else:
            return unauthorized("empty")


class BucketItemsGetPutDel(Resource):
    """ URL: /bucketlists/<id>/items/<item_id> Request methods: GET, PUT, DELETE
    """
    @authorized_user_item
    @authorized_user_bucketlist
    def get(self, id, item_id):
        """ Get a bucket list item """
        return marshal(g.item, bucket_item_inputs)

    @authorized_user_item
    @authorized_user_bucketlist
    def put(self, id, item_id):
        """ Update a bucket list item """
        parser = reqparse.RequestParser()
        parser.add_argument("title",
                            required=True,
                            help="No title provided.")
        parser.add_argument("description", type=str, default="")
        args = parser.parse_args()
        title, description = args["title"], args["description"]
        g.item.title = title
        g.item.description = description
        g.item.bucketlist_id = id
        return edit_item(name="title",
                         item=g.item,
                         serializer=bucket_item_inputs,
                         is_user=False,
                         is_bucket=False,
                         is_item=True)

    @authorized_user_item
    @authorized_user_bucketlist
    def delete(self, id, item_id):
        """ Delete a bucket list item """
        return delete_item(g.item,
                           g.item.title,
                           is_user=False,
                           is_bucket=False,
                           is_item=True)
