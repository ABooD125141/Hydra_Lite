Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' احصل على المسار الحالي من حيث تم تشغيل البرنامج
strCurrentDirectory = objFSO.GetParentFolderName(WScript.ScriptFullName)

' المسار إلى مجلد الوجهة على القرص C:
strDestinationFolder = "C:\MyApp"

' إذا لم يكن المجلد موجودًا على القرص C:، قم بإنشاءه
If Not objFSO.FolderExists(strDestinationFolder) Then
    objFSO.CreateFolder strDestinationFolder
End If

' اسم الملف الذي سيتم نسخه
strFileName = objFSO.GetFileName(WScript.ScriptFullName)

' المسار الكامل للملف الذي سيتم نسخه
strSourceFile = objFSO.BuildPath(strCurrentDirectory, strFileName)

' المسار الكامل للملف الذي سيتم إنشاءه على القرص C:
strDestinationFile = objFSO.BuildPath(strDestinationFolder, strFileName)

' نسخ الملف إلى القرص C:
objFSO.CopyFile strSourceFile, strDestinationFile, True

' المسار إلى مجلد بدء التشغيل
strStartupFolder = objShell.SpecialFolders("Startup")

' إسم الملف الذي سيتم إنشاءه في مجلد بدء التشغيل
strShortcutName = "MyApp.lnk"

' المسار الكامل للملف المختصر
strShortcutFile = objFSO.BuildPath(strStartupFolder, strShortcutName)

' إنشاء اختصار من الملف على القرص C: في مجلد بدء التشغيل
Set objShortcut = objShell.CreateShortcut(strShortcutFile)
objShortcut.TargetPath = strDestinationFile
objShortcut.Save

' إعادة تشغيل الكمبيوتر
objShell.Run "shutdown /r /t 0", 0, True
