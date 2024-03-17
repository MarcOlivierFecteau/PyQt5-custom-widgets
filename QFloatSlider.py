from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

class QFloatSlider(qtw.QSlider):

    # Create our own signal that we can connect to if necessary
    doubleValueChanged = qtc.pyqtSignal(float)

    def __init__(self, decimals=2, *args, **kargs):
        super(QFloatSlider, self).__init__(*args, **kargs)
        self._multiple = 10 ** decimals

    def emitDoubleValueChanged(self):
        value = float(super(QFloatSlider, self).value()) / self._multiple
        self.doubleValueChanged.emit(value)
    
    def setMinimum(self, value: float) -> None:
        return super(QFloatSlider, self).setMinimum(value * self._multiple)
    
    def setMaximum(self, value: float) -> None:
        return super(QFloatSlider, self).setMaximum(value * self._multiple)
    
    def setValue(self, value: float) -> None:
        super(QFloatSlider, self).setValue(int(value * self._multiple))
    
    def setSingleStep(self, value: float) -> None:
        return super(QFloatSlider, self).setSingleStep(value * self._multiple)

    def getValue(self) -> float:
        return float(super(QFloatSlider, self).value()).value() / self._multiple
    
    def getSingleStep(self) -> float:
        return float(super(QFloatSlider, self).singleStep()).value() / self._multiple
    
