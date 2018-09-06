#!/usr/bin/env python3
import os
import sys
from PyQt5 import sip
from PyQt5.QtCore import (QEvent, QFile, QFileInfo, QIODevice, QRegExp,
                          QTextStream,Qt)
from PyQt5.QtWidgets import (QAction, QApplication,  QFileDialog,
                             QMainWindow, QMessageBox, QTextEdit)
from PyQt5.QtGui import QFont, QIcon,QColor,QKeySequence,QSyntaxHighlighter,QTextCharFormat,QTextCursor
# import qrc_resources

# __version__ = "1.1.0"

class PythonHighlighter(QSyntaxHighlighter):

    Rules = []
    Formats = {}

    def __init__(self, parent=None):
        super(PythonHighlighter, self).__init__(parent)
        self.initializeFormats()

        #python关键字
        KEYWORDS = ["and", "as", "assert", "break", "class",
                "continue", "def", "del", "elif", "else", "except",
                "exec", "finally", "for", "from", "global", "if",
                "import", "in", "is", "lambda", "not", "or", "pass",
                "print", "raise", "return", "try", "while", "with",
                "yield"]
        BUILTINS = ["abs", "all", "any", "basestring", "bool",
                "callable", "chr", "classmethod", "cmp", "compile",
                "complex", "delattr", "dict", "dir", "divmod",
                "enumerate", "eval", "execfile", "exit", "file",
                "filter", "float", "frozenset", "getattr", "globals",
                "hasattr", "hex", "id", "int", "isinstance",
                "issubclass", "iter", "len", "list", "locals", "map",
                "max", "min", "object", "oct", "open", "ord", "pow",
                "property", "range", "reduce", "repr", "reversed",
                "round", "set", "setattr", "slice", "sorted",
                "staticmethod", "str", "sum", "super", "tuple", "type",
                "vars", "zip"]
        CONSTANTS = ["False", "True", "None", "NotImplemented",
                     "Ellipsis"]

        #语法高亮匹配规则
        PythonHighlighter.Rules.append((QRegExp(
                "|".join([r"\b%s\b" % keyword for keyword in KEYWORDS])),
                "keyword"))
        PythonHighlighter.Rules.append((QRegExp(
                "|".join([r"\b%s\b" % builtin for builtin in BUILTINS])),
                "builtin"))
        PythonHighlighter.Rules.append((QRegExp(
                "|".join([r"\b%s\b" % constant
                for constant in CONSTANTS])), "constant"))
        PythonHighlighter.Rules.append((QRegExp(
                r"\b[+-]?[0-9]+[lL]?\b"
                r"|\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b"
                r"|\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b"),
                "number"))
        PythonHighlighter.Rules.append((QRegExp(
                r"\bPyQt4\b|\bQt?[A-Z][a-z]\w+\b"), "pyqt"))
        PythonHighlighter.Rules.append((QRegExp(r"\b@\w+\b"),
                "decorator"))
        stringRe = QRegExp(r"""(?:'[^']*'|"[^"]*")""")
        stringRe.setMinimal(True)
        PythonHighlighter.Rules.append((stringRe, "string"))
        self.stringRe = QRegExp(r"""(:?"["]".*"["]"|'''.*''')""")
        self.stringRe.setMinimal(True)
        PythonHighlighter.Rules.append((self.stringRe, "string"))
        self.tripleSingleRe = QRegExp(r"""'''(?!")""")
        self.tripleDoubleRe = QRegExp(r'''"""(?!')''')
        PythonHighlighter.Rules.append((QRegExp(r"#.*"), "comment"))

    #语法高亮颜色匹配初始化
    @staticmethod
    def initializeFormats():
        baseFormat = QTextCharFormat()
        baseFormat.setFontFamily("consolas")
        baseFormat.setFontPointSize(12)
        for name, color in (("normal", Qt.black),
                ("keyword", Qt.blue), ("builtin", Qt.darkRed),
                ("constant", Qt.darkGreen),
                ("decorator", Qt.darkBlue), ("comment", Qt.green),
                ("string", Qt.darkGreen), ("number", Qt.darkMagenta),
                ("error", Qt.darkRed), ("pyqt", Qt.darkCyan)):
            format = QTextCharFormat(baseFormat)
            format.setForeground(QColor(color))
            if name in ("keyword", "decorator"):
                format.setFontWeight(QFont.Bold)
            if name == "comment":
                format.setFontItalic(True)
            PythonHighlighter.Formats[name] = format


    def highlightBlock(self, text):
        NORMAL, TRIPLESINGLE, TRIPLEDOUBLE, ERROR = range(4)

        textLength = len(text)
        prevState = self.previousBlockState()

        self.setFormat(0, textLength,
                            PythonHighlighter.Formats["normal"])

        if text.startswith("Traceback") or text.startswith("Error: "):
            self.setCurrentBlockState(ERROR)
            self.setFormat(0, textLength,
                           PythonHighlighter.Formats["error"])
            return
        if (prevState == ERROR and
            not (text.startswith(sys.ps1) or text.startswith("#"))):
            self.setCurrentBlockState(ERROR)
            self.setFormat(0, textLength,
                           PythonHighlighter.Formats["error"])
            return

        for regex, format in PythonHighlighter.Rules:
            i = regex.indexIn(text)
            while i >= 0:
                length = regex.matchedLength()
                self.setFormat(i, length,
                               PythonHighlighter.Formats[format])
                i = regex.indexIn(text, i + length)

        # Slow but good quality highlighting for comments. For more
        # speed, comment this out and add the following to __init__:
        # PythonHighlighter.Rules.append((QRegExp(r"#.*"), "comment"))
        # if not text:
        #     pass
        # elif text[0] == "#":
        #     self.setFormat(0, len(text),
        #                    PythonHighlighter.Formats["comment"])
        # else:
        #     stack = []
        #     for i, c in enumerate(text):
        #         if c in ('"', "'"):
        #             if stack and stack[-1] == c:
        #                 stack.pop()
        #             else:
        #                 stack.append(c)
        #         elif c == "#" and len(stack) == 0:
        #             self.setFormat(i, len(text),
        #                            PythonHighlighter.Formats["comment"])
        #             break

        self.setCurrentBlockState(NORMAL)

        if self.stringRe.indexIn(text) != -1:
            return
        # This is fooled by triple quotes inside single quoted strings

        for i, state in ((self.tripleSingleRe.indexIn(text),
                          TRIPLESINGLE),
                         (self.tripleDoubleRe.indexIn(text),
                          TRIPLEDOUBLE)):
            if self.previousBlockState() == state:
                if i == -1:
                    i = text.length()
                    self.setCurrentBlockState(state)
                self.setFormat(0, i + 3,
                               PythonHighlighter.Formats["string"])
            elif i > -1:
                self.setCurrentBlockState(state)
                self.setFormat(i, text.length(),
                               PythonHighlighter.Formats["string"])


    def rehighlight(self):
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        QSyntaxHighlighter.rehighlight(self)
        QApplication.restoreOverrideCursor()

#文本编辑类
class TextEdit(QTextEdit):

    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)


    def event(self, event):
        if (event.type() == QEvent.KeyPress and
            event.key() == Qt.Key_Tab):
            cursor = self.textCursor()
            cursor.insertText("    ")
            return True
        return QTextEdit.event(self, event)

#主要窗口类
class MainWindow(QMainWindow):

    def __init__(self, filename=None, parent=None):
        super(MainWindow, self).__init__(parent)

        font = QFont("Consolas", 11)
        font.setFixedPitch(True)
        self.editor = TextEdit()
        self.editor.setFont(font)
        self.highlighter = PythonHighlighter(self.editor.document())
        self.setCentralWidget(self.editor)

        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.showMessage("Ready", 5000)

        #文本编辑器的各种操作
        fileNewAction = self.createAction("新建...", self.fileNew,
                QKeySequence.New, "filenew", "创建一个新文件")
        fileOpenAction = self.createAction("打开...", self.fileOpen,
                QKeySequence.Open, "fileopen",
                "打开一个文件")
        self.fileSaveAction = self.createAction("&保存", self.fileSave,
                QKeySequence.Save, "filesave", "保存这个文件")
        self.fileSaveAsAction = self.createAction("另存 &作为...",
                self.fileSaveAs, icon="filesaveas",
                tip="用一个名字另存这个文件")
        fileQuitAction = self.createAction("&退出", self.close,
                "Ctrl+Q", "filequit", "关闭编辑器")
        self.editCopyAction = self.createAction("&复制",
                self.editor.copy, QKeySequence.Copy, "editcopy",
                "复制文本到剪切板")
        self.editCutAction = self.createAction("剪切", self.editor.cut,
                QKeySequence.Cut, "editcut",
                "剪切文本到剪切板")
        self.editPasteAction = self.createAction("&粘贴",
                self.editor.paste, QKeySequence.Paste, "editpaste",
                "粘贴剪切板上的文本")
        # self.editIndentAction = self.createAction("&Indent",
        #         self.editIndent, "Ctrl+]", "editindent",
        #         "Indent the current line or selection")
        # self.editUnindentAction = self.createAction("&Unindent",
        #         self.editUnindent, "Ctrl+[", "editunindent",
        #         "Unindent the current line or selection")

        #菜单栏的功能绑定
        fileMenu = self.menuBar().addMenu("&文件")
        self.addActions(fileMenu, (fileNewAction, fileOpenAction,
                self.fileSaveAction, self.fileSaveAsAction, None,
                fileQuitAction))
        editMenu = self.menuBar().addMenu("&编辑")
        self.addActions(editMenu, (self.editCopyAction,
                self.editCutAction, self.editPasteAction, None))

        # fileToolbar = self.addToolBar("File")
        # fileToolbar.setObjectName("FileToolBar")
        # self.addActions(fileToolbar, (fileNewAction, fileOpenAction,
        #                               self.fileSaveAction))
        # editToolbar = self.addToolBar("Edit")
        # editToolbar.setObjectName("EditToolBar")
        # self.addActions(editToolbar, (self.editCopyAction,
        #         self.editCutAction, self.editPasteAction, None))


        self.editor.selectionChanged.connect(self.updateUi)
        self.editor.document().modificationChanged.connect(self.updateUi)
        QApplication.clipboard().dataChanged.connect(self.updateUi)

        self.resize(800, 600)
        self.setWindowTitle("Python 编辑器")
        self.setWindowIcon(QIcon('icon.png'))
        self.filename = filename
        if self.filename is not None:
            self.loadFile()
        self.updateUi()

    #更新ui
    def updateUi(self, arg=None):
        self.fileSaveAction.setEnabled(
                self.editor.document().isModified())
        enable = not self.editor.document().isEmpty()
        self.fileSaveAsAction.setEnabled(enable)
        # self.editIndentAction.setEnabled(enable)
        # self.editUnindentAction.setEnabled(enable)
        enable = self.editor.textCursor().hasSelection()
        self.editCopyAction.setEnabled(enable)
        self.editCutAction.setEnabled(enable)
        self.editPasteAction.setEnabled(self.editor.canPaste())

    #创建动作
    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/{0}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    #添加动作
    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    #关闭事件
    def closeEvent(self, event):
        if not self.okToContinue():
            event.ignore()

    #关闭确认事件
    def okToContinue(self):
        if self.editor.document().isModified():
            reply = QMessageBox.question(self,
                            "Python 编辑器 --选择",
                            "有文本改变，要保存吗?",
                            QMessageBox.Yes|QMessageBox.No|
                            QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Yes:
                return self.fileSave()
        return True

    #新文件
    def fileNew(self):
        if not self.okToContinue():
            return
        document = self.editor.document()
        document.clear()
        document.setModified(False)
        self.filename = None
        self.setWindowTitle("Python 编辑器 - 未命名")
        self.updateUi()

    #打开文件
    def fileOpen(self):
        if not self.okToContinue():
            return
        dir = (os.path.dirname(self.filename)
               if self.filename is not None else ".")
        fname = str(QFileDialog.getOpenFileName(self,
                "Python 编辑器 - 选择文件", dir,
                "Python 文件 (*.py *.pyw)")[0])
        if fname:
            self.filename = fname
            self.loadFile()

    #加载文件
    def loadFile(self):
        fh = None
        try:
            fh = QFile(self.filename)
            if not fh.open(QIODevice.ReadOnly):
                raise IOError(str(fh.errorString()))
            stream = QTextStream(fh)
            stream.setCodec("UTF-8")
            self.editor.setPlainText(stream.readAll())
            self.editor.document().setModified(False)
        except EnvironmentError as e:
            QMessageBox.warning(self, "Python 编辑器 -- 加载错误",
                    "加载 {0} 文件失败，错误: {1}".format(self.filename, e))
        finally:
            if fh is not None:
                fh.close()
        self.setWindowTitle("Python 编辑器 - {0}".format(
                QFileInfo(self.filename).fileName()))

    #保存文件
    def fileSave(self):
        if self.filename is None:
            return self.fileSaveAs()
        fh = None
        try:
            fh = QFile(self.filename)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError(str(fh.errorString()))
            stream = QTextStream(fh)
            stream.setCodec("UTF-8")
            stream << self.editor.toPlainText()
            self.editor.document().setModified(False)
        except EnvironmentError as e:
            QMessageBox.warning(self, "Python 编辑器 -- 保存失败",
                    "保存 {0} 失败，错误: {1}".format(self.filename, e))
            return False
        finally:
            if fh is not None:
                fh.close()
        return True

    #保存文件为...
    def fileSaveAs(self):
        filename = self.filename if self.filename is not None else "."
        filename,filetype = QFileDialog.getSaveFileName(self,
                "Python 编辑器 -- 存文件为", filename,
                "Python 文件 (*.py *.pyw)")
        if filename:
            self.filename = filename
            self.setWindowTitle("Python 编辑器 - {0}".format(
                    QFileInfo(self.filename).fileName()))
            return self.fileSave()
        return False

    # #编辑缩进
    # def editIndent(self):
    #     cursor = self.editor.textCursor()
    #     cursor.beginEditBlock()
    #     if cursor.hasSelection():
    #         start = pos = cursor.anchor()
    #         end = cursor.position()
    #         if start > end:
    #             start, end = end, start
    #             pos = start
    #         cursor.clearSelection()
    #         cursor.setPosition(pos)
    #         cursor.movePosition(QTextCursor.StartOfLine)
    #         while pos <= end:
    #             cursor.insertText("    ")
    #             cursor.movePosition(QTextCursor.Down)
    #             cursor.movePosition(QTextCursor.StartOfLine)
    #             pos = cursor.position()
    #         cursor.setPosition(start)
    #         cursor.movePosition(QTextCursor.NextCharacter,
    #                             QTextCursor.KeepAnchor, end - start)
    #     else:
    #         pos = cursor.position()
    #         cursor.movePosition(QTextCursor.StartOfBlock)
    #         cursor.insertText("    ")
    #         cursor.setPosition(pos + 4)
    #     cursor.endEditBlock()

    # #编辑取消缩进
    # def editUnindent(self):
    #     cursor = self.editor.textCursor()
    #     cursor.beginEditBlock()
    #     if cursor.hasSelection():
    #         start = pos = cursor.anchor()
    #         end = cursor.position()
    #         if start > end:
    #             start, end = end, start
    #             pos = start
    #         cursor.setPosition(pos)
    #         cursor.movePosition(QTextCursor.StartOfLine)
    #         while pos <= end:
    #             cursor.clearSelection()
    #             cursor.movePosition(QTextCursor.NextCharacter,
    #                                 QTextCursor.KeepAnchor, 4)
    #             if cursor.selectedText() == "    ":
    #                 cursor.removeSelectedText()
    #             cursor.movePosition(QTextCursor.Down)
    #             cursor.movePosition(QTextCursor.StartOfLine)
    #             pos = cursor.position()
    #         cursor.setPosition(start)
    #         cursor.movePosition(QTextCursor.NextCharacter,
    #                             QTextCursor.KeepAnchor, end - start)
    #     else:
    #         cursor.clearSelection()
    #         cursor.movePosition(QTextCursor.StartOfBlock)
    #         cursor.movePosition(QTextCursor.NextCharacter,
    #                             QTextCursor.KeepAnchor, 4)
    #         if cursor.selectedText() == "    ":
    #             cursor.removeSelectedText()
    #     cursor.endEditBlock()

#主入口函数
def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.png'))
    fname = None
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    form = MainWindow(fname)
    form.show()
    app.exec_()


#从main入口启动
main()