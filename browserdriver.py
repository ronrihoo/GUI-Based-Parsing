import pyautogui as pag 

browserLogging = True
focusShifting = False


def setLogging(state):
	browserLogging = state


def flipFocusShifting():
	global focusShifting
	focusShifting = not focusShifting
	print("SHIFT_TAB: ", focusShifting)


def startNewPrivateTab():
	if browserLogging: print('starting new private tab in browser')
	pag.hotkey('ctrl', 't')


def invokeSourcePage(shiftTab=False):
	if browserLogging: 
		print('opening source-page for the current webpage')
		print('*note: if source-page is not opening, then try invokeSourcePage(shiftTab=True)')
	if shiftTab and not focusShifting: 
		flipFocusShifting()
		shiftElementFocusBack()
	pag.hotkey('ctrl', 'u')


def shiftElementFocusBack():
	print("focusShifting: {}".format(shiftTab))
	pag.hotkey('shift', 'tab')


def findTargetKeyword(keyword):
	if browserLogging: print('finding \'{}\' in page'.format(keyword))
	pag.hotkey('ctrl', 'f')
	pag.typewrite(keyword)
	pag.press('enter')
	pag.press('esc')


def copy():
	if browserLogging: print('copying selection in browser')
	pag.hotkey('ctrl', 'c')


def copyLine():
	if browserLogging: print('copying selected line in browser page')
	pag.hotkey('shift', 'end')
	pag.hotkey('ctrl', 'c')


def paste():
	if browserLogging: print('pasting in browser')
	pag.hotkey('ctrl', 'v')


def pasteAndEnter():
	paste()
	pag.press('enter')


def loadAddressInBrowser():
	startNewPrivateTab()
	pasteAndEnter()


def tabShiftRight(x=1):
	'''
		Shifts to browser tab on the right
	'''
	if browserLogging: 
		print('shifting to the right browser tab {} times'.format(x))
	for i in range(x):
		pag.hotkey('ctrl', 'tab')


def tabShiftLeft(x=1):
	'''
		Shifts to browser tab on the left
	'''
	if browserLogging: 
		print('shifting to the left browser tab {} times'.format(x))
	for i in range(x):
		pag.hotkey('ctrl', 'shift', 'tab')


def reopenPreviouslyClosedTab():
	'''
		Reopens in order of: last closed, first opened
	'''
	pag.hotkey('ctrl', 'shift', 't')


def closeTab(x=1):
	'''
		Closes current browser tab
	'''
	if browserLogging: 
		print('closing {} browser tab(s)'.format(x))
	for i in range(x):
		pag.hotkey('ctrl', 'w')


def closeBrowser():
	if browserLogging: 
		print('closing browser')
	pag.hotkey('ctrl', 'q')

