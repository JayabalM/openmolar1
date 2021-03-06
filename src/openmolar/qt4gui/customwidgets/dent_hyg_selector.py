#! /usr/bin/python

# ########################################################################### #
# #                                                                         # #
# # Copyright (c) 2009-2016 Neil Wallace <neil@openmolar.com>               # #
# #                                                                         # #
# # This file is part of OpenMolar.                                         # #
# #                                                                         # #
# # OpenMolar is free software: you can redistribute it and/or modify       # #
# # it under the terms of the GNU General Public License as published by    # #
# # the Free Software Foundation, either version 3 of the License, or       # #
# # (at your option) any later version.                                     # #
# #                                                                         # #
# # OpenMolar is distributed in the hope that it will be useful,            # #
# # but WITHOUT ANY WARRANTY; without even the implied warranty of          # #
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           # #
# # GNU General Public License for more details.                            # #
# #                                                                         # #
# # You should have received a copy of the GNU General Public License       # #
# # along with OpenMolar.  If not, see <http://www.gnu.org/licenses/>.      # #
# #                                                                         # #
# ########################################################################### #

from PyQt5 import QtCore
from PyQt5 import QtWidgets


class DentHygSelector(QtWidgets.QTreeWidget):
    selection_changed_signal = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QTreeWidget.__init__(self)
        self.setHeaderHidden(True)
        self.dents = []
        self.hygs = []
        self.root = QtWidgets.QTreeWidgetItem(self, ["All Clinicians"])
        self.root.setCheckState(0, QtCore.Qt.Checked)

        self.dent_root = QtWidgets.QTreeWidgetItem(self.root, ["All Dentists"])
        self.dent_root.setCheckState(0, QtCore.Qt.Checked)

        self.hyg_root = QtWidgets.QTreeWidgetItem(self.root, ["All Hygienists"])
        self.hyg_root.setCheckState(0, QtCore.Qt.Checked)

        self.dent_cbs = {}
        self.hyg_cbs = {}

        self.expandAll()
        self.signals(True)

    def set_dents(self, dents):
        self.dents = dents
        for dent in self.dents:
            i = QtWidgets.QTreeWidgetItem(self.dent_root, [dent])
            i.setCheckState(0, QtCore.Qt.Checked)
            self.dent_cbs[dent] = i

    def set_hygs(self, hygs):
        self.hygs = hygs
        for hyg in self.hygs:
            i = QtWidgets.QTreeWidgetItem(self.hyg_root, [hyg])
            i.setCheckState(0, QtCore.Qt.Checked)
            self.hyg_cbs[hyg] = i

    def signals(self, connect):
        if connect:
            self.itemChanged.connect(self.interact)
        else:
            self.itemChanged.disconnect(self.interact)

    def checkAll(self, checkstate=QtCore.Qt.Checked,
                 ignoreHygs=False, ignoreDents=False):
        if not ignoreHygs:
            for hyg in list(self.hyg_cbs.values()):
                hyg.setCheckState(0, checkstate)
        if not ignoreDents:
            for dent in list(self.dent_cbs.values()):
                dent.setCheckState(0, checkstate)

    def interact(self, item, column):
        self.signals(False)

        if item == self.root:
            self.checkAll(self.root.checkState(0))
        elif item == self.dent_root:
            self.checkAll(self.dent_root.checkState(0), ignoreHygs=True)
        elif item == self.hyg_root:
            self.checkAll(self.hyg_root.checkState(0), ignoreDents=True)

        allDentsChecked = QtCore.Qt.Checked
        for dent in self.dent_cbs:
            if not self.dent_cbs[dent].checkState(0):
                allDentsChecked = QtCore.Qt.Unchecked

        allHygsChecked = QtCore.Qt.Checked
        for hyg in self.hyg_cbs:
            if not self.hyg_cbs[hyg].checkState(0):
                allHygsChecked = QtCore.Qt.Unchecked

        self.dent_root.setCheckState(0, allDentsChecked)
        self.hyg_root.setCheckState(0, allHygsChecked)

        if allDentsChecked and allHygsChecked:
            allClinicians = QtCore.Qt.Checked
        else:
            allClinicians = QtCore.Qt.Unchecked

        self.root.setCheckState(0, allClinicians)

        self.signals(True)
        self.selection_changed_signal.emit()

    @property
    def selectedDents(self):
        for initials, cb in self.dent_cbs.items():
            if cb.checkState(0):
                yield initials

    @property
    def selectedHygs(self):
        for initials, cb in self.hyg_cbs.items():
            if cb.checkState(0):
                yield initials

    @property
    def selectedClinicians(self):
        for clinician in self.selectedDents:
            yield clinician
        for clinician in self.selectedHygs:
            yield clinician

    def allChecked(self):
        return self.root.checkState(0) == QtCore.Qt.Checked


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dents = ["Neil", "Bea", "Helen"]
    hygs = ["Rosie", "Sally", "Ariana"]
    w = DentHygSelector()
    w.set_dents(dents)
    w.set_hygs(hygs)
    w.show()
    app.exec_()
    print(list(w.selectedClinicians))
