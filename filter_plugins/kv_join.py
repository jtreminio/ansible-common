# Converts one-dimensional dict into a list with
# "key value" strings
# ex:
# {
#     proxy_buffers: '4 256k',
#     proxy_buffer_size: 128k,
#     proxy_connect_timeout: 600s,
#     proxy_send_timeout: 600s,
# }
# becomes:
# [
#     proxy_buffers '4 256k',
#     proxy_buffer_size 128k,
#     proxy_connect_timeout 600s,
#     proxy_send_timeout 600s,
#     proxy_read_timeout 600s,
# ]
def kv_join(collection):
    result = []

    for key, value in collection.items():
        result.append(key + " " + value)

    return result

class FilterModule(object):
    def filters(self):
        return {
            'kv_join': kv_join
        }
