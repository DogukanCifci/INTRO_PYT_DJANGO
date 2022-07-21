import sys 
#from importlib.machinery import SourceFileLoader  

sys.path.append('/Module-Package/my_package/my_subpack/asya')
sys.path.append("/numpy")

from numpy import matrix
matrix.örnek_sil()

from asya import kore

kore.kore_func()


#BU YÖNTEM CALISIYOR BIR SIKINTI YOK: 

#matrix = SourceFileLoader("matrix", "./numpy/matrix.py").load_module()

#matrix.örnek_sil()