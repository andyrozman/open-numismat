from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from Collection.CollectionFields import CollectionFields

class SelectColumnsDialog(QtGui.QDialog):
    DataRole = 16
    
    def __init__(self, listParam, parent=None):
        super(SelectColumnsDialog, self).__init__(parent)
        
        self.listParam = listParam
        
        self.listWidget = QtGui.QListWidget(self)
        # TODO: Disable resizing
        self.listWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.listWidget.setDropIndicatorShown(True) 
        self.listWidget.setWrapping(True)
        
        collectionFields = CollectionFields().fields
        for param in listParam.columns:
            field = collectionFields[param[0]]
            item = QtGui.QListWidgetItem(field.title, self.listWidget)
            item.setData(SelectColumnsDialog.DataRole, field.id)
            checked = Qt.Unchecked
            if param[1]:
                checked = Qt.Checked
            item.setCheckState(checked)
            self.listWidget.addItem(item)

        # TODO: Process missed columns

        # TODO: Add buttons SelectAll, ClearAll, EnabledToTop
        
        buttonBox = QtGui.QDialogButtonBox(Qt.Horizontal);
        buttonBox.addButton(QtGui.QDialogButtonBox.Ok);
        buttonBox.addButton(QtGui.QDialogButtonBox.Cancel);
        buttonBox.accepted.connect(self.save);
        buttonBox.rejected.connect(self.reject);

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.listWidget)
        layout.addWidget(buttonBox)

        self.setLayout(layout)

    def save(self):
        self.listParam.columns = []
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            filedId = item.data(SelectColumnsDialog.DataRole)
            enabled = (item.checkState() == Qt.Checked)
            self.listParam.columns.append((filedId, enabled))
        
        self.accept()
