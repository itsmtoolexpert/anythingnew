import platform
  def kernel_info():
     kernel_info = platform.uname()
  return {'release': kernel_info.release, 'version':kernel_info.version}
