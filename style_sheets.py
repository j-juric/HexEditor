verticalScrollBarStyle = """
QScrollBar:vertical {
	border: none;
    background: rgb(200, 200, 200);
    width: 14px;
    margin: 15px 0 15px 0;
	border-radius: 0px;
 }

/*  HANDLE BAR VERTICAL */
QScrollBar::handle:vertical {	
	background-color: rgb(80, 80, 192);
	min-height: 30px;
	border-radius: 7px;
}
QScrollBar::handle:vertical:hover{	
	background-color: rgb(40, 40, 152);
}
QScrollBar::handle:vertical:pressed {	
	background-color: rgb(172, 40, 40);
}

/* BTN TOP - SCROLLBAR */
QScrollBar::sub-line:vertical {
	border: none;
	background-color: rgb(79, 79, 110);
	height: 15px;
	border-top-left-radius: 7px;
	border-top-right-radius: 7px;
	subcontrol-position: top;
	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover {	
	background-color: rgb(39, 39, 70);
}
QScrollBar::sub-line:vertical:pressed {	
	background-color: rgb(172, 40, 40);
}

/* BTN BOTTOM - SCROLLBAR */
QScrollBar::add-line:vertical {
	border: none;
	background-color: rgb(79, 79, 110);
	height: 15px;
	border-bottom-left-radius: 7px;
	border-bottom-right-radius: 7px;
	subcontrol-position: bottom;
	subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover {	
	background-color: rgb(39, 39, 70);
}
QScrollBar::add-line:vertical:pressed {	
	background-color: rgb(172, 40, 40);
}

/* RESET ARROW */
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	background: none;
}
"""
textEditLightStyle = """
QTextEdit {
	border: 2px solid;
 	border-radius: 2px;
}
"""