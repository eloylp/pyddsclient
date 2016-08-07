import urllib3

from client.httpdao.batchdao import BatchDAO
from client.httpdao.batchqueuedao import BatchQueueDAO
from client.httpdao.messagedao import MessageDAO
from client.httpdao.messagequeuedao import MessageQueueDAO
from client.client import Client
from client.requestsadapter import RequestsAdapter


class ClientFactory(object):

    def get_http_client(self, node_id, auth_token):

        request_manager = RequestsAdapter(node_id, auth_token, urllib3.PoolManager())
        message_dao = MessageDAO(request_manager)
        message_queue_dao = MessageQueueDAO(request_manager)
        batch_dao = BatchDAO(request_manager)
        batch_queue_dao = BatchQueueDAO(request_manager)

        client = Client(message_dao, message_queue_dao, batch_dao, batch_queue_dao)

        return client

    def get_mongo_client(self):

        # TODO IMPLEMENT THIS FOR A DIRECT DB CLIENT. ONLY FOR INTERNAL PROECESS ACTIONS.
        raise NotImplementedError

