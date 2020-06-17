from arch.api import _EGGROLL_VERSION

if _EGGROLL_VERSION < 1:
    from eggroll.api.proto import basic_meta_pb2
    from eggroll.api.proto import proxy_pb2, proxy_pb2_grpc
    from eggroll.api.proto import proxy_pb2_grpc
else:
    from arch.api.proto import fate_meta_pb2 as basic_meta_pb2
    from arch.api.proto import proxy_pb2
    from arch.api.proto import proxy_pb2_grpc
