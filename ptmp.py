import generic

def options(opt):
    generic._options(opt, 'ptmp')

def configure(cfg):
    generic._configure(cfg, 'ptmp', incs=('ptmp/api.h',), libs=('ptmp',),
                       pcname='libptmp',
                       uses = 'LIBCZMQ PROTOBUF', mandatory=True)