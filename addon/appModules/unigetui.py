#appModules/unigetui.py
# Ein Teil von NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2025 NVDA Mitwirkende
# Diese Datei unterliegt der GNU General Public License.
# Weitere Informationen finden Sie in der Datei COPYING.
from NVDAObjects.UIA import ListItem,UIA
import appModuleHandler
import controlTypes
import api
from scriptHandler import script
import addonHandler
# Entfernen Sie das Kommentarzeichen (#) aus der nächsten Zeile, wenn (und sobald) die Datei zu einem Addon gehört. Dadurch werden Lokalisierungsfunktionen (Übersetzungsfunktionen) in Ihrer Datei aktiviert. Weitere Informationen finden Sie im Entwicklungshandbuch für NVDA-Addons.
addonHandler.initTranslation()
class AppModule(appModuleHandler.AppModule):
	unigetitemnames = ['UniGetUI.Interface.IgnoredPackageEntry',
	'UniGetUI.Interface.Widgets.SourceItem',
	'NavigationViewItem'
	]
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.name in self.unigetitemnames:
			clslist.insert(0, unigetuiListItem)
		elif obj.name == '':
			clslist.insert(0, unigetuiUnlabeledcontrol)
class unigetuiUnlabeledcontrol(UIA):
	def _get_name(self):
		l = list()
		for x in self.children:
			if x.name and x.role == controlTypes.ROLE_STATICTEXT: l.append(x.name)
		innerlabel = "; ".join(l)
		if innerlabel: ret = innerlabel
		else: ret = self.UIAAutomationId
		return ret


class unigetuiListItem(ListItem):
	def _get_name(self):
		l = list()
		for x in self.children:
			if x.name: l.append(x.name)
		return "; ".join(l)
