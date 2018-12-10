# -*-coding:utf-8-*-

import uuid

if __name__ == "__main__":
    name = 'test_name'
    print(name)
    namespace = uuid.NAMESPACE_URL
    print(namespace)

    print("1:", uuid.uuid1())
    print("3:", uuid.uuid3(namespace, name))
    print("变化4:", uuid.uuid4())
    print("5:", uuid.uuid5(namespace, name))
