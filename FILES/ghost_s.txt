Option Explicit

Dim objShell
Set objShell = CreateObject("WScript.Shell")

Sub HideFilesAndFoldersInSpecificDirs()
    Dim userName, folder, folderPath
    userName = objShell.ExpandEnvironmentStrings("%USERNAME%")
    folderPath = Array("C:\Users\" & userName & "\Pictures", _
                       "C:\Users\" & userName & "\Music", _
                       "C:\Users\" & userName & "\Desktop", _
                       "C:\Users\" & userName & "\Downloads", _
                       "C:\Users\" & userName & "\Documents")
    
    For Each folder In folderPath
        HideFilesAndFoldersRecursively folder
    Next
End Sub

Sub HideFilesAndFoldersRecursively(path)
    On Error Resume Next
    Dim objFSO, objFolder, objFile
    Set objFSO = CreateObject("Scripting.FileSystemObject")
    Set objFolder = objFSO.GetFolder(path)
    
    ' إخفاء الملفات والمجلدات في المجلد الحالي
    For Each objFile In objFolder.Files
        objShell.Run "cmd /c attrib -h -s -a """ & objFile.Path & """", 0, True
    Next
    
    ' دخول المجلدات الفرعية وإخفاء الملفات والمجلدات فيها
    For Each objSubFolder In objFolder.SubFolders
        HideFilesAndFoldersRecursively objSubFolder.Path
    Next
End Sub

' الدالة الرئيسية
Sub Main()
    HideFilesAndFoldersInSpecificDirs
End Sub

Main
