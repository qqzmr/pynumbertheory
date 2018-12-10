# -*-coding:utf-8-*-

import uuid

if __name__ == "__main__":
    name = 'test_name'
    print(name)
    namespace = uuid.NAMESPACE_URL
    print(namespace)

    print(uuid.uuid1())
    print(uuid.uuid3(namespace, name))
    print(uuid.uuid4())
    print(uuid.uuid5(namespace, name))
