#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import pypegasus.base.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class partition_configuration:
  """
  Attributes:
   - pid
   - ballot
   - max_replica_count
   - primary
   - secondaries
   - last_drops
   - last_committed_decree
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'pid', (pypegasus.base.ttypes.gpid, pypegasus.base.ttypes.gpid.thrift_spec), None, ), # 1
    (2, TType.I64, 'ballot', None, None, ), # 2
    (3, TType.I32, 'max_replica_count', None, None, ), # 3
    (4, TType.STRUCT, 'primary', (pypegasus.base.ttypes.rpc_address, pypegasus.base.ttypes.rpc_address.thrift_spec), None, ), # 4
    (5, TType.LIST, 'secondaries', (TType.STRUCT,(pypegasus.base.ttypes.rpc_address, pypegasus.base.ttypes.rpc_address.thrift_spec)), None, ), # 5
    (6, TType.LIST, 'last_drops', (TType.STRUCT,(pypegasus.base.ttypes.rpc_address, pypegasus.base.ttypes.rpc_address.thrift_spec)), None, ), # 6
    (7, TType.I64, 'last_committed_decree', None, None, ), # 7
  )

  def __init__(self, pid=None, ballot=None, max_replica_count=None, primary=None, secondaries=None, last_drops=None, last_committed_decree=None,):
    self.pid = pid
    self.ballot = ballot
    self.max_replica_count = max_replica_count
    self.primary = primary
    self.secondaries = secondaries
    self.last_drops = last_drops
    self.last_committed_decree = last_committed_decree

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.pid = pypegasus.base.ttypes.gpid()
          self.pid.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.ballot = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.max_replica_count = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.primary = pypegasus.base.ttypes.rpc_address()
          self.primary.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.secondaries = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = pypegasus.base.ttypes.rpc_address()
            _elem5.read(iprot)
            self.secondaries.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.last_drops = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = pypegasus.base.ttypes.rpc_address()
            _elem11.read(iprot)
            self.last_drops.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.last_committed_decree = iprot.readI64()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('partition_configuration')
    if self.pid is not None:
      oprot.writeFieldBegin('pid', TType.STRUCT, 1)
      self.pid.write(oprot)
      oprot.writeFieldEnd()
    if self.ballot is not None:
      oprot.writeFieldBegin('ballot', TType.I64, 2)
      oprot.writeI64(self.ballot)
      oprot.writeFieldEnd()
    if self.max_replica_count is not None:
      oprot.writeFieldBegin('max_replica_count', TType.I32, 3)
      oprot.writeI32(self.max_replica_count)
      oprot.writeFieldEnd()
    if self.primary is not None:
      oprot.writeFieldBegin('primary', TType.STRUCT, 4)
      self.primary.write(oprot)
      oprot.writeFieldEnd()
    if self.secondaries is not None:
      oprot.writeFieldBegin('secondaries', TType.LIST, 5)
      oprot.writeListBegin(TType.STRUCT, len(self.secondaries))
      for iter12 in self.secondaries:
        iter12.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.last_drops is not None:
      oprot.writeFieldBegin('last_drops', TType.LIST, 6)
      oprot.writeListBegin(TType.STRUCT, len(self.last_drops))
      for iter13 in self.last_drops:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.last_committed_decree is not None:
      oprot.writeFieldBegin('last_committed_decree', TType.I64, 7)
      oprot.writeI64(self.last_committed_decree)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.pid)
    value = (value * 31) ^ hash(self.ballot)
    value = (value * 31) ^ hash(self.max_replica_count)
    value = (value * 31) ^ hash(self.primary)
    value = (value * 31) ^ hash(self.secondaries)
    value = (value * 31) ^ hash(self.last_drops)
    value = (value * 31) ^ hash(self.last_committed_decree)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class query_cfg_request:
  """
  Attributes:
   - app_name
   - partition_indices
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'app_name', None, None, ), # 1
    (2, TType.LIST, 'partition_indices', (TType.I32,None), None, ), # 2
  )

  def __init__(self, app_name=None, partition_indices=None,):
    self.app_name = app_name
    self.partition_indices = partition_indices

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.app_name = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.partition_indices = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = iprot.readI32()
            self.partition_indices.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('query_cfg_request')
    if self.app_name is not None:
      oprot.writeFieldBegin('app_name', TType.STRING, 1)
      oprot.writeString(self.app_name)
      oprot.writeFieldEnd()
    if self.partition_indices is not None:
      oprot.writeFieldBegin('partition_indices', TType.LIST, 2)
      oprot.writeListBegin(TType.I32, len(self.partition_indices))
      for iter20 in self.partition_indices:
        oprot.writeI32(iter20)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.app_name)
    value = (value * 31) ^ hash(self.partition_indices)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class query_cfg_response:
  """
  Attributes:
   - err
   - app_id
   - partition_count
   - is_stateful
   - partitions
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'err', (pypegasus.base.ttypes.error_code, pypegasus.base.ttypes.error_code.thrift_spec), None, ), # 1
    (2, TType.I32, 'app_id', None, None, ), # 2
    (3, TType.I32, 'partition_count', None, None, ), # 3
    (4, TType.BOOL, 'is_stateful', None, None, ), # 4
    (5, TType.LIST, 'partitions', (TType.STRUCT,(partition_configuration, partition_configuration.thrift_spec)), None, ), # 5
  )

  def __init__(self, err=None, app_id=None, partition_count=None, is_stateful=None, partitions=None,):
    self.err = err
    self.app_id = app_id
    self.partition_count = partition_count
    self.is_stateful = is_stateful
    self.partitions = partitions

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.err = pypegasus.base.ttypes.error_code()
          self.err.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.app_id = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.partition_count = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.is_stateful = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.partitions = []
          (_etype24, _size21) = iprot.readListBegin()
          for _i25 in xrange(_size21):
            _elem26 = partition_configuration()
            _elem26.read(iprot)
            self.partitions.append(_elem26)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('query_cfg_response')
    if self.err is not None:
      oprot.writeFieldBegin('err', TType.STRUCT, 1)
      self.err.write(oprot)
      oprot.writeFieldEnd()
    if self.app_id is not None:
      oprot.writeFieldBegin('app_id', TType.I32, 2)
      oprot.writeI32(self.app_id)
      oprot.writeFieldEnd()
    if self.partition_count is not None:
      oprot.writeFieldBegin('partition_count', TType.I32, 3)
      oprot.writeI32(self.partition_count)
      oprot.writeFieldEnd()
    if self.is_stateful is not None:
      oprot.writeFieldBegin('is_stateful', TType.BOOL, 4)
      oprot.writeBool(self.is_stateful)
      oprot.writeFieldEnd()
    if self.partitions is not None:
      oprot.writeFieldBegin('partitions', TType.LIST, 5)
      oprot.writeListBegin(TType.STRUCT, len(self.partitions))
      for iter27 in self.partitions:
        iter27.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.err)
    value = (value * 31) ^ hash(self.app_id)
    value = (value * 31) ^ hash(self.partition_count)
    value = (value * 31) ^ hash(self.is_stateful)
    value = (value * 31) ^ hash(self.partitions)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
